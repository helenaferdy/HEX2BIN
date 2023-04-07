from lib.hex2bin import helenamain

print('''
        *** HEX2BIN ***
-- Convert Hex file into Binary --
''')

im_file = input('Enter the name of hex file [hex.txt] : ')
ex_file = input('Enter the name of the output file [leave empty for auto] : ')

print("")
if im_file == "":
    im_file = "hex.txt"

helenamain(im_file, ex_file)