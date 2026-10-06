def analyze_roe(roe):
    if roe < 10:
        return "Weak"

    elif roe < 15:
        return "Moderate"

    else:
        return "Strong"


def analyze_roce(roce):
    if roce < 10:
        return "Weak"

    elif roce < 15:
        return "Moderate"

    else:
        return "Strong"


def analyze_debt_to_equity(debt_to_equity):
    if debt_to_equity is None:
        return "Not Available"

    if debt_to_equity < 0.5:
        return "Low Debt"

    elif debt_to_equity < 1:
        return "Moderate Debt"

    else:
        return "High Debt"


def analyze_profit_margin(profit_margin):
    if profit_margin < 10:
        return "Low"

    elif profit_margin < 20:
        return "Moderate"

    else:
        return "High"


def analyze_eps_growth(eps_growth):
    if eps_growth is None:
        return "Not Available"

    if eps_growth < 0:
        return "Declining"

    elif eps_growth < 10:
        return "Slow Growth"

    elif eps_growth < 20:
        return "Moderate Growth"

    else:
        return "Strong Growth"


def revenue_growth_yoy(revenue_growth_yoy):
    if revenue_growth_yoy <= 5:
        return "Low"

    elif revenue_growth_yoy <= 10:
        return "Moderate"

    else:
        return "High"


def analyze_cash_conversion(cfo_to_net_profit):
    if cfo_to_net_profit is None:
        return "Not Available"

    if cfo_to_net_profit < 0.8:
        return "Weak"

    elif cfo_to_net_profit < 1:
        return "Moderate"

    else:
        return "Strong"


def analyze_earnings_consistency(
    revenue_growth,
    profit_growth,
    eps_growth
):
    if revenue_growth is None or eps_growth is None:
        return "Insufficient Data"

    if profit_growth is None:
        if revenue_growth > 0 and eps_growth > 0:
            if eps_growth < revenue_growth * 0.5:
                return "Revenue/EPS Growth Mismatch"

            else:
                return "Positive Growth"

        elif revenue_growth > 0 and eps_growth < 0:
            return "Earnings Concern"

        else:
            return "Weak Growth"

    if revenue_growth > 0 and profit_growth > 0 and eps_growth > 0:
        if eps_growth < revenue_growth * 0.5:
            return "Growth Mismatch"

        return "Consistent Growth"

    elif revenue_growth < 0 and profit_growth < 0 and eps_growth < 0:
        return "Declining"

    else:
        return "Mixed Growth"


def analyze_pe(pe):
    if pe is None:
        return "Not Available"

    if pe < 15:
        return "Low"

    elif pe < 25:
        return "Moderate"

    elif pe < 40:
        return "High"

    else:
        return "Very High"


def analyze_pb(pb):
    if pb is None:
        return "Not Available"

    if pb < 1:
        return "Low"

    elif pb < 3:
        return "Moderate"

    elif pb < 6:
        return "High"

    else:
        return "Very High"


def analyze_ev_to_ebitda(ev_to_ebitda):
    if ev_to_ebitda is None:
        return "Not Available"

    if ev_to_ebitda < 10:
        return "Low"

    elif ev_to_ebitda < 15:
        return "Moderate"

    elif ev_to_ebitda < 25:
        return "High"

    else:
        return "Very High"


def analyze_peg(peg):
    if peg is None:
        return "Not Available"

    if peg < 1:
        return "Low"

    elif peg < 2:
        return "Moderate"

    elif peg < 3:
        return "High"

    else:
        return "Very High"