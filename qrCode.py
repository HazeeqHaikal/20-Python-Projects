import qrcode

if __name__ == '__main__':
    def generateQR(text):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("./image/qr.png")
        
    url = input("Enter the URL: ")
    generateQR(url)