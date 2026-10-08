# Stock Analyzer

Stock Analyzer is a Python and Flask application that helps users evaluate publicly listed Indian companies using financial metrics and multiple valuation models.

The application combines company fundamentals, industry-specific analysis, and valuation assumptions to estimate a stock's fair value and compare it with its current market price.

## What It Does

The user enters an Indian stock ticker, along with valuation assumptions such as expected growth rate, discount rate, terminal growth rate, and forecast period.

The application retrieves the company's financial data and uses it to calculate estimated values through applicable valuation models. The results help the user assess whether the current market price appears reasonable relative to the assumptions used.

The application is intended as an analytical tool, not as a prediction or guarantee of future stock prices.

## Features

* Search and analyze Indian publicly listed companies using the BharatStock API.
* Retrieve financial and company information such as sector, industry, price, EPS, ROE, ROCE, debt-to-equity, growth, cash flow, and valuation multiples.
* Analyze business-quality metrics and classify them into simple categories such as Strong, Moderate, or Weak.
* Apply industry-specific analysis and select appropriate valuation models based on the company's sector and industry.
* Calculate estimated values using Graham, P/E, P/B, and DCF valuation models.
* Display valuation results visually for easier comparison.
* Calculate an average valuation across the applicable models.
* Calculate Margin of Safety by comparing the estimated average value with the current market price.
* Calculate Valuation Spread to show how much the different valuation models disagree with each other.
* Cache API responses locally to reduce unnecessary API requests.

## How It Works

1. The user enters a stock ticker or symbol.
2. The application checks its local cache for available data.
3. If fresh data is not available, the BharatStock API is used to retrieve the company's information.
4. The API provides information such as the company's sector and industry along with its financial metrics.
5. The application uses the sector and industry to determine which metrics and valuation models are applicable.
6. The selected models analyze the company using its financial data and the user's valuation assumptions.
7. The application calculates the estimated values and valuation summary.
8. A final report is presented through the Flask web application.

## Valuation Models

### Graham Valuation

The Graham valuation model provides a rough estimate of intrinsic value using earnings per share and a growth assumption. It is based on the valuation approach associated with Benjamin Graham.

### P/E Valuation

The P/E model estimates fair value using the company's earnings per share and a user-provided fair P/E multiple.

### P/B Valuation

The P/B model estimates fair value using book value per share and a user-provided fair P/B multiple. It is particularly useful for financial companies where book value can be an important valuation measure.

### DCF Valuation

The Discounted Cash Flow model estimates the present value of the company's future free cash flows. It uses assumptions such as forecast growth, discount rate, terminal growth rate, and forecast period.

The application then calculates an average across the applicable valuation models. Different industries may use different combinations of models depending on the company's business type.

## Tech Stack

* **Python** — Core application logic and financial analysis
* **Flask** — Web application framework
* **Jinja** — Dynamic HTML templating
* **HTML** — Web page structure
* **CSS** — Frontend styling
* **BharatStock API** — Company and financial data
* **JSON** — Local API response caching
* **Git & GitHub** — Version control and source management

## Limitations

* Valuation results depend heavily on the assumptions provided by the user.
* The valuation models provide estimates rather than guaranteed intrinsic values or future prices.
* Industry-specific model selection currently uses predefined rules rather than automatically comparing a company against peer-company averages.
* Historical price data is not currently available in the application because of limitations with the current data provider's historical-price endpoint.
* The application currently focuses on fundamental analysis rather than technical price-pattern analysis.
* The BharatStock API has request limits on its free plan, which is why local caching is used.
