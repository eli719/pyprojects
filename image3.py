from PIL import Image
image_name=r'D://picture/1.jpg'
image = Image.open(image_name) #type:Image.Image
image=image.convert('RGB')
image=image.save('1.jpg')
def plx(data, address):
    w = data.width
    h = data.height

    for x in range(1, w - 1):
        if x > 1 and x != w - 2:
            # 获取目标像素点左右位置
            left = x - 1
            right = x + 1
        for y in range(1, h - 1):
            # 获取目标像素点上下位置
            up = y - 1
            down = y + 1

            if x <= 2 or x >= (w - 2):
                data.putpixel((x, y), 255)
            elif y <= 2 or y >= (h - 2):
                data.putpixel((x, y), 255)
            elif data.getpixel((x, y)) == 0:
                if y > 1 and y != h - 1:
                    # 以目标像素点为中心店,获取周围像素点颜色
                    # 0为黑色  255为白色
                    up_color = data.getpixel((x, up))
                    down_color = data.getpixel((x, down))
                    left_color = data.getpixel((left, y))
                    left_down_color = data.getpixel((left, down))
                    right_color = data.getpixel((right, y))
                    right_up_color = data.getpixel((right, up))
                    right_down_color = data.getpixel((right, down))

                    # 去除竖线干扰
                    if down_color == 0:
                        if left_color == 255 and left_down_color == 255 and right_color == 255 and right_down_color == 255:
                            data.putpixel((x, y), 255)

                    # 去除横干扰线
                    elif right_color == 0:
                        if down_color == 255 and right_down_color == 255 and up_color == 255 and right_up_color == 255:
                            data.putpixel((x, y), 255)

                        # 去除斜干扰线
                if left_color == 255 and right_color == 255 \
                        and up_color == 255 and down_color == 255:
                    data.putpixel((x, y), 255)
            else:
                pass

            # 保存去除干扰线后的图片
            data.save(address, "png")
plx(image,'c.png')