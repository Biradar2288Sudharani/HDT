import qrcode

# Your website URL
url = "https://belkin2288kiran.pythonanywhere.com/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("HDT_QR.png")

print("QR Code generated successfully! Saved as HDT_QR.png")
