import datetime


def main():
    float_value = 3.14159
    int_value = 100
    scientific_value = float(6.02214076e23)
    emoji = "🐧"
    string = "cat good"

    value1 = "I hate the number"
    value2 = 11

    date = datetime.datetime.utcnow()
    n = 10

    print(f'{float_value = }')                                      # ‘float_value = x'
    print(f'float_value is {float_value} :)')                       # in a string
    print(f'{value1} {value2}!')                                    # multiple variables
    print(f'Formatted float: {float_value:.2f}')                    # float format
    print(f'Hex Value of 100: {int_value:x}')                       # hex
    print(f'Octal Value of 100: {int_value:o}')                     # octal
    print(f'Scientific Notation of 1 mol: {scientific_value:.3e}')  # scientific
    print(f'Leading Zeroes: {int_value:05}')                        # format width 5 leading 0s
    print(f'Repr of the float: {float_value!r}')                    # repr
    print(f'Ascii of the emoji {emoji}: {emoji!a}')                 # ascii
    print(f'{string: <10}')                                         # justify float_value 10 to the left, pad with space
    print(f'{string:=^{n}}')                                        # justify float_value n to the center, pad with =
    print(f'{string:*>10}')                                         # justify float_value 10 to the right, pad with *
    print(f'{date = :%Y/%m/%d}')                                    # datetime format


if __name__ == "__main__":
    main()
