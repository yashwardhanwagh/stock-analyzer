def graham_value(eps, growth):
    if eps <= 0:
        raise ValueError("EPS must be greater than 0.")

    if growth < 0:
        raise ValueError("Growth rate cannot be negative.")

    intrinsic_value = eps * (8.5 + 2 * growth)

    return intrinsic_value


def pe_value(eps, fair_pe):
    if eps <= 0:
        raise ValueError("EPS must be greater than 0.")

    if fair_pe <= 0:
        raise ValueError("Fair PE must be greater than 0.")

    fair_value = eps * fair_pe

    return fair_value


def dcf_value(
    fcf,
    growth,
    discount_rate,
    terminal_growth,
    years,
    total_shares
):
    if total_shares <= 0:
        raise ValueError("Total shares must be greater than 0.")

    if fcf <= 0:
        raise ValueError(
            "FCF must be greater than 0 for DCF valuation."
        )

    if years <= 0:
        raise ValueError("Forecast years must be greater than 0.")

    if discount_rate <= terminal_growth:
        raise ValueError(
            "Discount rate must be greater than terminal growth."
        )

    growth = growth / 100
    discount_rate = discount_rate / 100
    terminal_growth = terminal_growth / 100

    total_pv = 0

    for year in range(1, years + 1):
        future_fcf = fcf * (1 + growth) ** year

        pv = future_fcf / (1 + discount_rate) ** year

        total_pv += pv

    next_year_fcf = future_fcf * (1 + terminal_growth)

    denominator = discount_rate - terminal_growth

    terminal_value = next_year_fcf / denominator

    present_denominator = (1 + discount_rate) ** years

    pv_terminal = terminal_value / present_denominator

    total_dcf = total_pv + pv_terminal

    per_share_value = total_dcf / total_shares

    return per_share_value


def pb_value(book_value_per_share, fair_pb):
    if book_value_per_share <= 0:
        raise ValueError(
            "Book value per share must be greater than 0."
        )

    if fair_pb <= 0:
        raise ValueError("Fair P/B must be greater than 0.")

    fair_value = book_value_per_share * fair_pb

    return fair_value