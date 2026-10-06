from data import get_stock_data,process_stock_data
from valuation_sector import select_models
from valuations import graham_value, pe_value, pb_value, dcf_value

batch_list = [
    "BAJFINANCE", "BSE"
    ,"EMMVEE"
    ,"GROWW","HINDUNILVR",
    "INFY", "JPOLYINVST", 
     "LT",
    "M&M", "MAHABANK"
    ,"ONEGLOBAL", "RELIANCE"
    , "SBIN", "TATAPOWER"
    , "TCS", "VIKRAMSOLR"
    ,"WAAREERTL"
]

FAIR_GROWTH = 10
FAIR_PE = 20
FAIR_PB = 2
DCF_GROWTH = 10
DISCOUNT_RATE = 10
TERMINAL_GROWTH = 4
FORECAST_YEARS = 5


for symbol in batch_list:

    print(f"\n{'=' * 60}")
    print(f"{symbol}")
    print("=" * 60)

    try:
        data = get_stock_data(symbol)
        stock = process_stock_data(data)

        models = select_models(
            stock["sector"],
            stock["industry"]
        )

        valuations = {}

        if "Graham" in models:
            valuations["Graham"] = graham_value(
                stock["eps"],
                FAIR_GROWTH
            )

        if "PE" in models:
            valuations["PE"] = pe_value(
                stock["eps"],
                FAIR_PE
            )

        if "P/B" in models:
            valuations["P/B"] = pb_value(
                stock["book_value_per_share"],
                FAIR_PB
            )

        if "DCF" in models:

            try:
                valuations["DCF"] = dcf_value(
                    stock["free_cash_flow"],
                    DCF_GROWTH,
                    DISCOUNT_RATE,
                    TERMINAL_GROWTH,
                    FORECAST_YEARS,
                    stock["shares_outstanding"]
                )

            except ValueError:
                valuations["DCF"] = None

        available_values = [
            value for value in valuations.values()
            if value is not None
        ]

        if available_values:
            average = sum(available_values) / len(available_values)

            margin_of_safety = (
                (average - stock["price"])
                / stock["price"]
            ) * 100

        else:
            average = None
            margin_of_safety = None

        print(f"Company: {stock['name']}")
        print(f"Price: ₹{stock['price']:.2f}")
        print(f"Models: {models}")

        for model, value in valuations.items():

            if value is None:
                print(f"{model}: Not Available")
            else:
                print(f"{model}: ₹{value:.2f}")

        if average is not None:
            print(f"Average Value: ₹{average:.2f}")
            print(f"Margin of Safety: {margin_of_safety:.2f}%")
        else:
            print("Average Value: Not Available")

    except Exception as e:
        print(f"ERROR: {e}")