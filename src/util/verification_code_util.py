# coding=utf-8
import base64
import io
import os
import random
import string

from PIL import Image, ImageFont, ImageDraw, ImageFilter

from config.dir_conf import RESOURCE_DIR


def rnd_color():
    """
    随机颜色
    :return:
    """
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def gene_text():
    """
       生成4位验证码
       :return:
       """
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def draw_lines(draw, num, width, height):
    """
           划线
           :return:
           """
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)


def get_verify_code(to_base64=False):
    """
       生成验证码图形
       :return:
       """
    code = gene_text()
    # 图片大小120×50
    width, height = 120, 50
    # 新图片对象
    im = Image.new('RGB', (width, height), 'white')
    # 字体
    # ImageFont.truetype  font:先按照路径找,然后去平台下字体库中找,区分大小写,,windows下文件名通过属性查看字体文件名
    font = ImageFont.truetype(os.path.join(RESOURCE_DIR, "arial.ttf"), size=40, encoding='utf-8')
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)),
                  text=code[item], fill=rnd_color(), font=font)
    # 划线
    draw_lines(draw, 2, width, height)
    # 高斯模糊
    im = im.filter(ImageFilter.GaussianBlur(radius=1.5))

    bytes_io = io.BytesIO()
    im.save(bytes_io, 'png')

    if to_base64:
        img_str = b"data:image/png;base64," + base64.b64encode(bytes_io.getvalue())
        return code, img_str

    bytes_io.seek(0)
    return code, bytes_io
