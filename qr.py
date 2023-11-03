import qrcode
from qrcode.image.styledpil import StyledPilImage

def generate_qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )

    url = input('Insert URL or text: ')
    user_have_logo = input('Want to add a logo to your QR code? (Y/N): ').strip().lower()

    qr.add_data(url)
    qr.make(fit=True)

    if user_have_logo == 'y':
        logo = input('Insert your logo file name: ')
        qr_img = qr.make_image(image_factory=StyledPilImage, embedded_image_path=logo)
    else:
        custom_color = input('Want to customize your QR Code? (Y/N): ').strip().lower()
        if custom_color == 'y':
            foreground = input('Foreground color: ')
            background = input('Background color: ')
            qr_img = qr.make_image(fill_color=foreground, back_color=background)
        else:
            qr_img = qr.make_image(fill_color='black', back_color='white')

    format_choice = input('Choose the format to save the QR code (PNG/SVG/PDF): ').strip().lower()

    if format_choice == 'png':
        qr_img.save('qrcode.png')
    elif format_choice == 'svg':
        qr_img.save('qrcode.svg')
    elif format_choice == 'pdf':
        qr_img.save('qrcode.pdf')
    else:
        print('Invalid format choice. Saving as PNG by default.')
        qr_img.save('qrcode.png')

if __name__ == '__main__':
    generate_qr_code()
