from analysis.industry import get_industry_metrics
from data import get_stock_data, process_stock_data
from report import generate_report
from valuation_sector import select_models
from valuations import (
    dcf_value,
    graham_value,
    pb_value,
    pe_value,
)


def float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Stock selection
symbol = input("Enter stock symbol: ").strip().upper()

try:
    stock_data = get_stock_data(symbol)
    stock = process_stock_data(stock_data)

except ValueError as error:
    print(error)
    exit()


industry_metrics = get_industry_metrics(
    stock["sector"],
    stock["industry"]
)

models = select_models(
    stock["sector"],
    stock["industry"]
)

print("\nAvailable Valuations:")

for model in models:
    print(f"- {model}")

print("Selected Models:", models)


current_price = stock["price"]
eps = stock["eps"]


# Valuations
valuations = {}


if "Graham" in models:
    growth = float_input("Enter fair growth rate: ")

    try:
        intrinsic_value = graham_value(eps, growth)
        valuations["Graham"] = intrinsic_value

    except ValueError as error:
        print(f"Graham valuation skipped: {error}")


if "PE" in models:
    fair_pe = float_input("Enter fair PE: ")

    try:
        pe_valuation = pe_value(eps, fair_pe)
        valuations["PE"] = pe_valuation

    except ValueError as error:
        print(f"PE valuation skipped: {error}")


if "DCF" in models:
    dcf_growth_rate = float_input(
        "Enter fair DCF growth rate: "
    )
    discount_rate = float_input(
        "Enter discount rate: "
    )
    terminal_growth_rate = float_input(
        "Enter terminal growth rate: "
    )
    forecast_years = get_int_input(
        "Enter forecast years: "
    )

    fcf = stock["free_cash_flow"]
    total_shares = stock["shares_outstanding"]

    try:
        dcf = dcf_value(
            fcf=fcf,
            growth=dcf_growth_rate,
            discount_rate=discount_rate,
            years=forecast_years,
            terminal_growth=terminal_growth_rate,
            total_shares=total_shares
        )

        valuations["DCF"] = dcf

    except ValueError as error:
        print(f"DCF valuation skipped: {error}")


if "P/B" in models:
    fair_pb = float_input("Enter Fair P/B: ")

    book_value_per_share = stock["book_value_per_share"]

    try:
        pb_valuation = pb_value(
            book_value_per_share,
            fair_pb
        )

        valuations["P/B"] = pb_valuation

    except ValueError as error:
        print(f"P/B valuation skipped: {error}")


# Calculations
if len(valuations) == 0:
    print("\nNo valid valuations could be calculated.")
    exit()


average = sum(valuations.values()) / len(valuations)

margin_of_safety = (
    (average - current_price) / average
) * 100


# Check valuation spread
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


# Generate report
generate_report(
    stock,
    industry_metrics,
    models,
    valuations
)