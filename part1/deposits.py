# usage message ================>

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""

USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    growthPerYear = (1 + per) ** (1 / fixed_period)
    growthPerTenYear = (1 + per) ** (10 / fixed_period)

    # new feature: round result

    return [[round(float(initial_sum * growth), 2), round(growth*10, 2)],
            [round(float(initial_sum * growthPerYear), 2), round(growthPerYear*10, 2)],
            [round(float(initial_sum * growthPerTenYear), 2), round(growthPerTenYear*10, 2)]]


def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]

    # new feature: check for corrent number

    for i in range(4):

        if not args[i].isdigit() or int(args[i]) < 1:

            try:
                if float(args[i]) < 1 or float(args[i]):
                    raise ValueError()

            except ValueError:
                print('ARGS ERROR: arg (', args[i], ') is NOT a correct.')
                exit()

    initial_sum, percent, fixed_period, set_period = map(float, args)
    res = deposit(initial_sum, percent, fixed_period, set_period)

    print('Your deposit:', res[0][0], ' Percents up:', res[0][1],'%')
    print('Your deposit 1 year later:', res[1][0], ' Percents up:', res[1][1],'%')
    print('Your deposit 10 years later:', res[2][0], ' Percents up:', res[2][1],'%')


# start ========================>
if __name__ == '__main__':
    import sys

    main(sys.argv)
