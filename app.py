from flask import Flask, render_template, request

from analysis.general import (
    analyze_cash_conversion,
    analyze_debt_to_equity,
    analyze_eps_growth,
    analyze_pb,
    analyze_pe,
    analyze_roce,
    analyze_roe,
    revenue_growth_yoy,
)
from analysis.industry import get_industry_metrics
from data import get_stock_data, process_stock_data
from valuation_sector import select_models
from valuations import dcf_value, graham_value, pb_value, pe_value


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    symbol = request.form["symbol"].strip().upper()

    if not symbol:
        raise ValueError("Please enter a stock symbol.")

    growth = float(request.form["growth"])
    fair_pe = float(request.form["fair_pe"])
    fair_pb = float(request.form["fair_pb"])
    dcf_growth = float(request.form["dcf_growth"])
    discount_rate = float(request.form["discount_rate"])
    terminal_growth = float(request.form["terminal_growth"])
    forecast_years = int(request.form["forecast_years"])

    # Validate user inputs
    if growth < 0:
        raise ValueError("Growth rate cannot be negative.")

    if fair_pe <= 0:
        raise ValueError("Fair PE must be greater than 0.")

    if fair_pb <= 0:
        raise ValueError("Fair P/B must be greater than 0.")

    if dcf_growth < 0:
        raise ValueError("DCF growth rate cannot be negative.")

    if discount_rate <= 0:
        raise ValueError("Discount rate must be greater than 0.")

    if terminal_growth < 0:
        raise ValueError("Terminal growth cannot be negative.")

    if discount_rate <= terminal_growth:
        raise ValueError(
            "Discount rate must be greater than terminal growth."
        )

    if forecast_years <= 0:
        raise ValueError(
            "Forecast years must be greater than 0."
        )

    # Get and process stock data
    stock_data = get_stock_data(symbol)
    stock = process_stock_data(stock_data)

    industry_metrics = get_industry_metrics(
        stock["sector"],
        stock["industry"]
    )

    models = select_models(
        stock["sector"],
        stock["industry"]
    )

    # Analyze business quality
    analysis = {}

    if stock["roe"] is not None:
        analysis["roe"] = analyze_roe(stock["roe"])
    else:
        analysis["roe"] = "Not Available"

    if stock["roce"] is not None:
        analysis["roce"] = analyze_roce(stock["roce"])
    else:
        analysis["roce"] = "Not Available"

    if stock["debt_to_equity"] is not None:
        analysis["debt"] = analyze_debt_to_equity(
            stock["debt_to_equity"]
        )
    else:
        analysis["debt"] = "Not Available"

    if stock["eps_growth_yoy"] is not None:
        analysis["eps_growth"] = analyze_eps_growth(
            stock["eps_growth_yoy"]
        )
    else:
        analysis["eps_growth"] = "Not Available"

    if stock["revenue_growth_yoy"] is not None:
        analysis["revenue_growth"] = revenue_growth_yoy(
            stock["revenue_growth_yoy"]
        )
    else:
        analysis["revenue_growth"] = "Not Available"

    if stock["cfo_to_net_profit"] is not None:
        analysis["cash_conversion"] = analyze_cash_conversion(
            stock["cfo_to_net_profit"]
        )
    else:
        analysis["cash_conversion"] = "Not Available"

    if stock["pe_ratio"] is not None:
        analysis["pe"] = analyze_pe(stock["pe_ratio"])
    else:
        analysis["pe"] = "Not Available"

    if stock["pb_ratio"] is not None:
        analysis["pb"] = analyze_pb(stock["pb_ratio"])
    else:
        analysis["pb"] = "Not Available"

    # Calculate valuations
    valuations = {}

    if "Graham" in models:
        try:
            valuations["Graham"] = graham_value(
                stock["eps"],
                growth
            )
        except ValueError:
            pass

    if "PE" in models:
        try:
            valuations["PE"] = pe_value(
                stock["eps"],
                fair_pe
            )
        except ValueError:
            pass

    if "P/B" in models:
        try:
            valuations["P/B"] = pb_value(
                stock["book_value_per_share"],
                fair_pb
            )
        except ValueError:
            pass

    if "DCF" in models:
        try:
            valuations["DCF"] = dcf_value(
                fcf=stock["free_cash_flow"],
                growth=dcf_growth,
                discount_rate=discount_rate,
                terminal_growth=terminal_growth,
                years=forecast_years,
                total_shares=stock["shares_outstanding"]
            )
        except ValueError:
            pass

    if len(valuations) == 0:
        raise ValueError(
            "No valid valuations could be calculated."
        )

    # Calculate valuation summary
    average = sum(valuations.values()) / len(valuations)

    margin_of_safety = (
        (average - stock["price"]) / average
    ) * 100

    valuation_values = list(valuations.values())

    if len(valuation_values) >= 2:
        highest_value = max(valuation_values)
        lowest_value = min(valuation_values)

        valuation_spread = (
            (highest_value - lowest_value) / lowest_value
        ) * 100
    else:
        valuation_spread = 0

    valuations["Average"] = average
    valuations["Margin of Safety"] = margin_of_safety
    valuations["Valuation Spread"] = valuation_spread

    return render_template(
        "result.html",
        stock=stock,
        industry_metrics=industry_metrics,
        models=models,
        analysis=analysis,
        valuations=valuations
    )


@app.errorhandler(ValueError)
def handle_value_error(error):
    return render_template(
        "error.html",
        message=str(error)
    ), 400


if __name__ == "__main__":
    app.run(debug=True)