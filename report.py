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


def generate_report(stock, industry_metrics, models, valuations):
    print("\n" + "=" * 50)
    print("              STOCK FINANCIAL ANALYSIS")
    print("=" * 50)

    print(f"\nCompany: {stock['name']}")
    print(f"Symbol: {stock['symbol']}")
    print(f"Sector: {stock['sector']}")
    print(f"Industry: {stock['industry']}")
    print(f"Current Price: ₹{stock['price']:.2f}")

    print("\n" + "-" * 18 + " BUSINESS QUALITY " + "-" * 18)

    if "ROE" in industry_metrics:
        if stock["roe"] is None:
            print("ROE: Not Available")
        else:
            roe_analysis = analyze_roe(stock["roe"])
            print(f"ROE: {stock['roe']:.2f}%")
            print(f"ROE Analysis: {roe_analysis}")

    if "ROCE" in industry_metrics:
        if stock["roce"] is None:
            print("ROCE: Not Available")
        else:
            roce_analysis = analyze_roce(stock["roce"])
            print(f"ROCE: {stock['roce']:.2f}%")
            print(f"ROCE Analysis: {roce_analysis}")

    if "Profit Growth" in industry_metrics:
        if stock["profit_growth_yoy"] is None:
            print("Profit Growth YOY: Not Available")
        else:
            print(
                f"Profit Growth YOY: "
                f"{stock['profit_growth_yoy']:.2f}%"
            )

    if "Revenue Growth" in industry_metrics:
        if stock["revenue_growth_yoy"] is None:
            print("Revenue Growth YOY: Not Available")
        else:
            revenue_analysis = revenue_growth_yoy(
                stock["revenue_growth_yoy"]
            )
            print(
                f"Revenue Growth YOY: "
                f"{stock['revenue_growth_yoy']:.2f}%"
            )
            print(
                f"Revenue Growth Analysis: "
                f"{revenue_analysis}"
            )

    if "EPS Growth" in industry_metrics:
        if stock["eps_growth_yoy"] is None:
            print("EPS Growth: Not Available")
        else:
            eps_analysis = analyze_eps_growth(
                stock["eps_growth_yoy"]
            )
            print(
                f"EPS Growth YOY: "
                f"{stock['eps_growth_yoy']:.2f}%"
            )
            print(
                f"EPS Growth Analysis: "
                f"{eps_analysis}"
            )

    if "Debt" in industry_metrics:
        if stock["debt_to_equity"] is None:
            print("Debt to Equity: Not Available")
            print("Debt Analysis: Not Available")
        else:
            debt_analysis = analyze_debt_to_equity(
                stock["debt_to_equity"]
            )
            print(
                f"Debt to Equity: "
                f"{stock['debt_to_equity']}"
            )
            print(f"Debt Analysis: {debt_analysis}")

    if "FCF" in industry_metrics:
        cash_conversion_analysis = analyze_cash_conversion(
            stock["cfo_to_net_profit"]
        )

        if stock["cash_flow_operating"] is None:
            print("Operating Cash Flow: Not Available")
        else:
            print(
                f"Operating Cash Flow: "
                f"₹{stock['cash_flow_operating']}"
            )

        if stock["free_cash_flow"] is None:
            print("Free Cash Flow: Not Available")
        else:
            print(
                f"Free Cash Flow: "
                f"₹{stock['free_cash_flow']}"
            )

        if stock["cfo_to_net_profit"] is None:
            print("CFO / Net Profit: Not Available")
        else:
            print(
                f"CFO / Net Profit: "
                f"{stock['cfo_to_net_profit']}"
            )

        print(
            f"Cash Conversion Quality: "
            f"{cash_conversion_analysis}"
        )

    if "PE" in industry_metrics:
        if stock["pe_ratio"] is None:
            print("PE Ratio: Not Available")
        else:
            pe_analysis = analyze_pe(stock["pe_ratio"])
            print(f"PE Ratio: {stock['pe_ratio']:.2f}")
            print(f"PE Ratio Analysis: {pe_analysis}")

    if "P/B" in industry_metrics:
        if stock["pb_ratio"] is None:
            print("PB Ratio: Not Available")
        else:
            pb_analysis = analyze_pb(stock["pb_ratio"])
            print(f"P/B Ratio: {stock['pb_ratio']:.2f}")
            print(f"P/B Ratio Analysis: {pb_analysis}")

    print("\n" + "-" * 21 + " VALUATION " + "-" * 21)

    print("Applicable Models:")

    for model in models:
        if model == "DCF" and "DCF" not in valuations:
            print("- DCF (NOT AVAILABLE)")
        else:
            print(f"- {model}")

    if "Graham" in models:
        print(
            f"Graham Value: "
            f"₹{valuations['Graham']:.2f}"
        )

    if "PE" in models:
        print(
            f"PE Value: "
            f"₹{valuations['PE']:.2f}"
        )

    if "P/B" in models:
        print(
            f"P/B Value: "
            f"₹{valuations['P/B']:.2f}"
        )

    if "DCF" in models:
        if "DCF" in valuations:
            print(
                f"DCF Value: "
                f"₹{valuations['DCF']:.2f}"
            )
        else:
            print("DCF Value: Not Available")

    print(
        f"Average Valuation: "
        f"₹{valuations['Average']:.2f}"
    )

    print(
        f"Margin of Safety: "
        f"{valuations['Margin of Safety']:.2f}%"
    )

    print(
        f"Valuation Spread: "
        f"{valuations['Valuation Spread']:.2f}%"
    )

    if valuations["Valuation Spread"] > 100:
        print(
            "Valuation Warning: "
            "Models disagree significantly."
        )

    print("\n" + "-" * 19 + " FINAL SUMMARY " + "-" * 19)

    average = valuations["Average"]
    margin_of_safety = valuations["Margin of Safety"]

    if stock["price"] > average:
        valuation_status = "Trading above estimated value"
    elif stock["price"] < average:
        valuation_status = "Trading below estimated value"
    else:
        valuation_status = "Trading near estimated value"

    if margin_of_safety >= 25:
        valuation_summary = "Attractive margin of safety"
    elif margin_of_safety >= 10:
        valuation_summary = "Moderate margin of safety"
    else:
        valuation_summary = "Low margin of safety"

    print(f"Valuation Status: {valuation_status}")
    print(f"Margin of Safety: {valuation_summary}")