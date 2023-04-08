import binascii
import datetime
import pickle

IMPORT_PATH = "import/"
EXPORT_PATH = "export/"

def helenamain(im_file, ex_file):
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        with open(IMPORT_PATH+im_file, 'r') as infile:
            hex_string = infile.read().strip()
    except:
        print(f"file {im_file} doesn't exist")
        return

    if hex_string[:2] == "0x":
        hex_string = hex_string[2:]
    byte_data = binascii.unhexlify(hex_string)

    if ex_file == "":
        if byte_data[:4] == b'\x89PNG':
            file_format = ".png"
        elif byte_data[:2] == b'\xFF\xD8':
            file_format = ".jpg"
        elif byte_data[:4] == b'\x25\x50\x44\x46':
            file_format = ".pdf"
        elif byte_data[:3] == b'\x00\x00\x00' or byte_data[:4] == b'\x66\x74\x79\x70':
            file_format = ".mp4"
        elif byte_data[:4] == b'\x00\x00\x00\x14' or byte_data[:4] == b'\x6D\x6F\x6F\x76':
            file_format = ".mov"
        else:
            file_format = ""
    else:
        file_format = "-"+ex_file


    with open(f'{EXPORT_PATH}file-{date}{file_format}', 'wb') as outfile:
        outfile.write(byte_data)
        if file_format == ".":
            print(f"Unknown file format, saving file with no extension")
        elif file_format.startswith('.'):
            print(f"Detected file format: {file_format[1:].upper()}")
        else:
            print(f"Output name from user : {file_format[1:]}")
        print(f"File saved in {EXPORT_PATH}file-{date}{file_format}")