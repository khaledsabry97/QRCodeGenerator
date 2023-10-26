# import modules
import qrcode
from PIL import Image
from QrCodeHelpers import *

logo_name = 'bing-logo.png'
tuples = [
        ('14c4j8oa_14fx5fxz', 'bingapp.microsoft.com/bing?adjust=14c4j8oa_14fx5fxz'),
        ('148846oq_14oca1gt', 'bingapp.microsoft.com/bing?adjust=148846oq_14oca1gt')
        ]


def StartExperience():
    for i in range(len(tuples)):
        nameFile = tuples[i][0]
        url = tuples[i][1]

        Process(nameFile= nameFile,
                URL= url,
                logo_name=logo_name,
                dots_color= BLACK,
                background_color= WHITE,
                out_file_color= 'black'
                )
        
        Process(nameFile= nameFile,
                URL= url,
                logo_name=logo_name,
                dots_color= WHITE,
                background_color= BLACK,
                out_file_color= 'white'
                )

def Process(nameFile, URL, logo_name, dots_color, background_color, out_file_color):
    logo = ReadImg(logo_name, 170)
    logo = ChangeBackgroundColor(logo, dots_color, background_color)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=30,
        border=0)
 
    QRimg = AddURL(QRcode, URL, dots_color, background_color)
    QRimg = AddLogoToQR(QRimg, logo)
    
    # save the QR code generated
    qrcode_img_path = './output/'+ nameFile+"-" + out_file_color +'.png'
    QRimg.save(qrcode_img_path)

    QRimg_transparent = MakeImageTransparent(qrcode_img_path, background_color)
    qrcode_img_transparent_path = 'output/'+ nameFile+"-" + out_file_color + "-" +  'transparent.png'
    QRimg_transparent.save(qrcode_img_transparent_path, "PNG")

    print(nameFile + 'QR code generated!')


StartExperience()

