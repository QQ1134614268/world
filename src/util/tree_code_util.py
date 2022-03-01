import io
import urllib

import qrcode
from PIL import Image


def make_code(url_dic, url=None, img_path=None, is_show=None, img_width=None, img_height=None, ):
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    data = urllib.parse.urlencode(url_dic)
    if url:
        data = url + "?" + data
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    if img_path:
        icon = Image.open(img_path)
        # logo="D:/favicon.jpg"
        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)

    file_io = io.BytesIO()
    img.save(file_io, 'png')
    file_io.seek(0)
    return file_io


if __name__ == '__main__':
    make_code({"table_id": 1}, url="http://ggok.top")
