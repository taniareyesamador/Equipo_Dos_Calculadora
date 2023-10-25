def conv_fracc_num(num: str) -> float:
    """
    Esta función permite realiza la conversión de uns fracción a un número real

    Args:
      num: str:

    Returns: Un número real

    """
    if isinstance(num, (int, float)):
        return num

    if "/" in num:
        try:
            return float(num)
        except ValueError:
            num, denom = num.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    return float(num)
