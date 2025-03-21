def round_ans(val):
    """
    Rounds temperaure to nearest degree
    :param val: number to be rounded
    :return number rounded to nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)

def to_celcius(to_convert):
    """
    Coverts from F to C
    :param to_convert: Temperature to be converted in F
    :return: Temperature in C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)

def to_fahrenheit(to_convert):
    """
    Coverts from C to F
    :param to_convert: Temperature to be converted in C
    :return: Temperature in F
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)