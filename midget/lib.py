
def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    """
    Convert an integer to a base36 string
    """
    if not isinstance(number, int):
        number = int(number)

    base36 = ''

    signature = ''
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return signature + base36

def base36decode(number):
    return int(number, 36)

if __name__ == '__main__':
    print base36encode(1234)
    print base36decode('xyz121')
