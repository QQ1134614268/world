# -*- coding:utf-8 -*-
"""
@Time: 2022/1/16
@Description:
"""
import argparse

from PIL import Image


def main(width_ratio=4, height_ratio=3):
    width = 200
    height = width / width_ratio * height_ratio
    image = Image.new(mode='RGBA', size=(int(width), int(height)))
    # draw_table = ImageDraw.Draw(im=image)
    # draw_table.text(xy=(0, 0), text=u'', fill='#008B8B', font=ImageFont.truetype('./SimHei.ttf', 50))
    image.save(f'ratio_{width_ratio}-{height_ratio}.png', 'PNG')  # 保存在当前路径下，格式为PNG
    image.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--width_ratio', help='宽比例', default=2, type=float)
    parser.add_argument('--height_ratio', help='高比例', default=1, type=float)
    args = parser.parse_args()

    main(args.width_ratio, args.height_ratio)
    # main(4, 3)
    # main(16, 9)
