from PIL import Image


def remove_border1(image, image_del):
    w = image.width
    h = image.height
    for x in range(0, 1):
        for y in range(h):
            image.putpixel((x, y), 255)

    for x in range(w - 1, w):
        for y in range(h):
            image.putpixel((x, y), 255)

    for y in range(0, 1):
        for x in range(w):
            image.putpixel((x, y), 255)

    for y in range(h - 1, h):
        for x in range(w):
            image.putpixel((x, y), 255)
    image.save(image_del)
    s = Image.open(image_del)
    return s


def remove_border(image, image_del):
    w = image.width
    h = image.height
    for x in range(0, 20):
        for y in range(h):
            image.putpixel((x, y), 255)

    for x in range(115, 135):
        for y in range(h):
            image.putpixel((x, y), 255)

    for y in range(0, 4):
        for x in range(w):
            image.putpixel((x, y), 255)

    for y in range(33, 40):
        for x in range(w):
            image.putpixel((x, y), 255)
    image.save(image_del)
    s = Image.open(image_del)
    return s


def del_noise_num(image, image_del, white, black):
    w = image.width
    h = image.height
    for x in range(1, w - 1):
        # 获取目标像素点左右位置
        left = x - 1
        right = x + 1
        for y in range(1, h - 1):
            def val(color):
                if color > 127:  # 0为白色，1为黑色
                    return 0
                else:
                    return 1

            # 获取目标像素点上下位置
            black_point = 0

            up = y - 1
            down = y + 1
            self_color = image.getpixel((x, y))

            up_color = image.getpixel((x, up))  # 上
            down_color = image.getpixel((x, down))  # 下
            left_color = image.getpixel((left, y))  # 左
            left_up_color = image.getpixel((left, up))  # 左上
            left_down_color = image.getpixel((left, down))  # 左下
            right_color = image.getpixel((right, y))  # 右
            right_up_color = image.getpixel((right, up))  # 右上
            right_down_color = image.getpixel((right, down))  # 右下

            if val(up_color) == 1:
                black_point += 1
            if val(down_color) == 1:
                black_point += 1
            if val(left_color) == 1:
                black_point += 1
            if val(left_up_color) == 1:
                black_point += 1
            if val(left_down_color) == 1:
                black_point += 1
            if val(right_color) == 1:
                black_point += 1
            if val(right_up_color) == 1:
                black_point += 1
            if val(right_down_color) == 1:
                black_point += 1
            # 白色像素： 若周围的8个像素中黑色像素数量大于6个，则应填充为黑色
            # print('black_point:'+str(black_point))
            white_point = 8 - black_point
            # print('white_point:'+white_point.__str__())
            if val(self_color) == 0:
                if black_point >= black:
                    image.putpixel((x, y), 0)
            else:
                # 黑色像素： 若周围的8个像素中白色像素数量大于6个，则应填充为白色
                if white_point >= white:
                    image.putpixel((x, y), 255)
    image.save(image_del)


def del_noise(image, image_del):
    w = image.width
    h = image.height
    for x in range(1, w - 1):
        # 获取目标像素点左右位置
        left = x - 1
        right = x + 1
        for y in range(1, h - 1):
            def val(color):
                if color > 127:  # 0为白色，1为黑色
                    return 0
                else:
                    return 1

            # 获取目标像素点上下位置
            black_point = 0

            up = y - 1
            down = y + 1
            self_color = image.getpixel((x, y))

            up_color = image.getpixel((x, up))  # 上
            down_color = image.getpixel((x, down))  # 下
            left_color = image.getpixel((left, y))  # 左
            left_up_color = image.getpixel((left, up))  # 左上
            left_down_color = image.getpixel((left, down))  # 左下
            right_color = image.getpixel((right, y))  # 右
            right_up_color = image.getpixel((right, up))  # 右上
            right_down_color = image.getpixel((right, down))  # 右下

            if val(up_color) == 1:
                black_point += 1
            if val(down_color) == 1:
                black_point += 1
            if val(left_color) == 1:
                black_point += 1
            if val(left_up_color) == 1:
                black_point += 1
            if val(left_down_color) == 1:
                black_point += 1
            if val(right_color) == 1:
                black_point += 1
            if val(right_up_color) == 1:
                black_point += 1
            if val(right_down_color) == 1:
                black_point += 1
            # 白色像素： 若周围的8个像素中黑色像素数量大于6个，则应填充为黑色
            # print('black_point:'+str(black_point))
            white_point = 8 - black_point
            # print('white_point:'+white_point.__str__())
            if val(self_color) == 0:
                if black_point >= 7:
                    image.putpixel((x, y), 0)
            else:
                # 黑色像素： 若周围的8个像素中白色像素数量大于6个，则应填充为白色
                if white_point >= 6 :
                    image.putpixel((x, y), 255)
    image.save(image_del)


def horizontal_del(image, image_del):
    w = image.width
    h = image.height
    for x in range(1, w - 1):
        # 获取目标像素点左右位置
        left = x - 1
        right = x + 1
        for y in range(1, h - 1):
            def val(color):
                if color > 127:  # 0为白色，1为黑色
                    return 0
                else:
                    return 1

            # 获取目标像素点上下位置
            black_point = 0
            left_right = 0

            up = y - 1
            down = y + 1
            self_color = image.getpixel((x, y))

            up_color = image.getpixel((x, up))  # 上
            down_color = image.getpixel((x, down))  # 下
            left_color = image.getpixel((left, y))  # 左
            right_color = image.getpixel((right, y))  # 右

            if val(up_color) == 1:
                black_point += 1
            if val(down_color) == 1:
                black_point += 1
            if val(left_color) == 1:
                left_right += 1
            if val(right_color) == 1:
                left_right += 1
            # 白色像素： 若上下像素都为黑色，则应填充为黑色
            white_point = 2 - black_point
            if val(self_color) == 0:
                if black_point >= 1 and left_right == 2:
                    image.putpixel((x, y), 0)
            # else:
            #     # 黑色像素： 若周围的8个像素中白色像素数量大于6个，则应填充为白色
            #     if white_point == 2 and left_right >= 2:
            #         image.putpixel((x, y), 255)
    image.save(image_del)


def vertical_del(image, image_del):
    w = image.width
    h = image.height
    for x in range(1, w - 1):
        # 获取目标像素点左右位置
        left = x - 1
        right = x + 1
        for y in range(1, h - 1):
            def val(color):
                if color > 127:  # 0为白色，1为黑色
                    return 0
                else:
                    return 1

            # 获取目标像素点上下位置
            black_point = 0
            left_right = 0

            up = y - 1
            down = y + 1
            self_color = image.getpixel((x, y))

            up_color = image.getpixel((x, up))  # 上
            down_color = image.getpixel((x, down))  # 下
            left_color = image.getpixel((left, y))  # 左
            if left > 1:
                left_left_color = image.getpixel((left - 1, y))  # 左左
            right_color = image.getpixel((right, y))  # 右
            if right < w - 1:
                right_right_color = image.getpixel((right + 1, y))  # 右右

            if val(up_color) == 1:
                black_point += 1
            if val(down_color) == 1:
                black_point += 1
            if val(left_color) == 1:
                left_right += 1
            if val(right_color) == 1:
                left_right += 1

            white_point = 2 - black_point
            if val(self_color) == 1:
                if white_point == 2 and left_right > 0:
                    image.putpixel((x, y), 255)
            else:
                if black_point == 2 and left_right >= 1:
                    image.putpixel((x, y), 0)
    image = image.save(image_del)
    return image


def main():
    for i in range(1, 5):
        image_name = 'verify_1_crop' + str(i) + '.jpg'
        image_del = 'verify_del_crop' + str(i) + '.jpg'
        im = Image.open(image_name)  # type:Image.Image
        remove_border1(im, image_del)
        for j in range(3):
            del_noise(im, image_del)
        horizontal_del(im, image_del)
        vertical_del(im, image_del)
