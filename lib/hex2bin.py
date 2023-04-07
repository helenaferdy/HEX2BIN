import binascii
import datetime

IMPORT_PATH = "import/"
EXPORT_PATH = "export/"

def helenamain(im_file, ex_file):
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    with open(IMPORT_PATH+im_file, 'r') as infile:
        hex_string = infile.read().strip()

    if hex_string[:2] == "0x":
        hex_string = hex_string[2:]

    byte_data = binascii.unhexlify(hex_string)

    if ex_file == "":
        if byte_data[:4] == b'\x89PNG':
            with open(f'{EXPORT_PATH}image-{date}.png', 'wb') as outfile:
                outfile.write(byte_data)
            print("Detected file format: PNG")
            print(f"File saved in {EXPORT_PATH}image-{date}.png")
        elif byte_data[:2] == b'\xFF\xD8':
            with open(f'{EXPORT_PATH}image-{date}.jpg', 'wb') as outfile:
                outfile.write(byte_data)
            print("Detected file format: JPEG")
            print(f"File saved in {EXPORT_PATH}image-{date}.jpg")
        else:
            with open(f'{EXPORT_PATH}file-{date}', 'wb') as outfile:
                outfile.write(byte_data)
            print("Unknown file format, saving it with no extension.")
            print(f"File saved in {EXPORT_PATH}file-{date}")
    else:
        with open(f"{EXPORT_PATH}{ex_file}", 'wb') as outfile:
            outfile.write(byte_data)
            print(f"File saved in {EXPORT_PATH}{ex_file}")



