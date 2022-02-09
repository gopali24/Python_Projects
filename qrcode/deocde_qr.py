from pyzbar.pyzbar import decode
from PIL import Image

file_path = input("Enter the file name or the path of the file: ")
decodeQR = decode(Image.open(file_path))
print(decodeQR[0].data.decode('ascii'))