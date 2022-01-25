import pyqrcode
import png

def generate_qr(link,name="QRCode"):
    name+=".png"
    qr_code = pyqrcode.create(link)
    qr_code.png(name,scale=5)

link = input("Enter the weblink for which you want to generate the QR code: ")
ch = input("Do you want to give a name to the QR? Enter Y for yes and N for no: ")
if ch.lower() == 'y':
    name = input("Enter a name for your QR code: ")
    generate_qr(link,name)
elif ch.lower() == 'n':
    generate_qr(link)
else:
    print("Invalid option -_-")

print("QR generated!!")