import qrcode



#git repo for the qr code module: https://github.com/lincolnloop/python-qrcode

qr = qrcode.QRCode()
data = input("Enter the data to put in the QR: ")
qr.add_data(data)
qr.make()
img = qr.make_image()
fileName = input("enter file name: ")
img.save(fileName+".png")