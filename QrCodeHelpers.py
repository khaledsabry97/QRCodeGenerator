
from PIL import Image
import os

BLACK = 0
WHITE = 255

def MakeImageTransparent(img_name, detect_color=255):
    img = Image.open(img_name)
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    newData = []
    for item in datas:
        if item[0] == detect_color and item[1] == detect_color and item[2] == detect_color: # finding black color
            newData.append((255, 255, 255, 0)) # replacing it with transparent
        else:
            newData.append(item)
    rgba.putdata(newData)
    return rgba

def ChangeBackgroundColor(img, _from, _to):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == _from and item[1] == _from and item[2] == _from: # finding black color
            newData.append((_to, _to, _to)) # replacing it with transparent
        else:
            newData.append(item)
    img.putdata(newData)
    return img

def ReadImg(img_name, resize_width = 100):
        img = Image.open(img_name)
        # taking base width
        basewidth = resize_width
        
        # adjust image size
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize))

        return img

def AddURL(QRcode, url, dots_color, background_color):
    # adding URL or text to QRcode
    QRcode.add_data(url)
    
    # generating QR code
    QRcode.make()
    _dots_color = 'WHITE'
    _background_color = 'WHITE'

    if dots_color == 0: #black
        _dots_color = 'BLACK'
    
    if background_color == 0:
        _background_color = 'BLACK'
        
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=_dots_color, back_color=_background_color).convert('RGB')
    return QRimg

def AddLogoToQR(QRimg, logo):
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    return QRimg