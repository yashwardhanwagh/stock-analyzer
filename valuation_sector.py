def select_models(sector, industry):
    if sector == "Financial Services" and industry == "Banks - Regional":
        return ["P/B", "PE"]

    elif sector == "Financial Services" and industry in [
        "NBFC",
        "Credit Services"
    ]:
        return ["P/B", "PE"]

    elif sector == "Financial Services" and industry == "Insurance":
        return ["P/B", "PE"]

    elif sector == "Financial Services" and industry == "Capital Markets":
        return ["PE", "P/B"]

    elif (
        sector == "Information Technology"
        and industry == "Information Technology Services"
    ):
        return ["Graham", "PE", "DCF"]

    else:
        return ["Graham", "PE", "DCF"]