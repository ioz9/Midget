# This file is part of Midget.
#
# Midget is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Midget is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Midget.  If not, see <http://www.gnu.org/licenses>
#
# Copyright (c) 2011, Chris Soyars <ctso@ctso.me>

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
