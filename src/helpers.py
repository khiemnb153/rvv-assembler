import re


def sign_mag_2_two_comp(value, width):
    if value > 0:
        two_comp = value
    else:
        two_comp = (~abs(value) | (1 << (width - 1))) + 1

    return two_comp % (2 ** width)


def code_number(number_as_str: str, width):
    '''
    Convert number as string into int coded (two-comp) binary.
    Return a non-negative int
    '''
    number_match = re.match(r'(?P<bin>0b[01]+)|(?P<hex>0x[0-9a-fA-F]+)|(?P<dec>-?\d+)', number_as_str)

    if not number_match:
        return -1 # Error code

    if number_match.group('bin'):
        return int(number_match.group('bin'), 2)
    elif number_match.group('hex'):
        return int(number_match.group('hex'), 16)
    elif number_match.group('dec'):
        return sign_mag_2_two_comp(int(number_match.group('dec')), width)


def print_error_and_exit(line_number, statement, error_descs):
    print(f'SyntaxError at {line_number}: {statement}')
    for desc in error_descs:
        print(desc)
    exit(1)