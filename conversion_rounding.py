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


to_c_test = [0, 100, -459, 60.34]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()


for item in to_c_test:
    ans = to_celcius(item)
    print(f"{item} F is {ans} C")
