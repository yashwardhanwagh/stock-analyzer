def get_industry_metrics(sector, industry):
    if sector == "Financial Services" and industry == "Banks - Regional":
        return [
            "ROE",
            "Profit Growth",
            "EPS Growth",
            "PE",
            "P/B"
        ]

    elif sector == "Financial Services" and industry in [
        "NBFC",
        "Credit Services"
    ]:
        return [
            "ROE",
            "Debt",
            "EPS Growth",
            "PE",
            "P/B"
        ]

    elif sector == "Financial Services" and industry == "Insurance":
        return [
            "ROE",
            "Profit Growth",
            "EPS Growth",
            "PE",
            "P/B"
        ]

    elif sector == "Financial Services" and industry == "Capital Markets":
        return [
            "ROE",
            "Profit Growth",
            "EPS Growth",
            "PE",
            "P/B"
        ]

    elif (
        sector == "Information Technology"
        and industry == "Information Technology Services"
    ):
        return [
            "ROE",
            "ROCE",
            "Revenue Growth",
            "EPS Growth",
            "FCF",
            "PE",
            "DCF"
        ]

    else:
        return [
            "ROE",
            "ROCE",
            "Revenue Growth",
            "EPS Growth",
            "FCF",
            "PE",
            "DCF"
        ]