from PIL import Image
import del_noise as dn
import crop_image as ci
import recognize_code as rc


def remove_border(image):
    w = image.width
    h = image.height
    for x in range(0, 20):
        for y in range(h):
            image.putpixel((x, y), (255, 255, 255))

    for x in range(120, 135):
        for y in range(h):
            image.putpixel((x, y), (255, 255, 255))

    for y in range(0, 5):
        for x in range(w):
            image.putpixel((x, y), (255, 255, 255))

    for y in range(30, 40):
        for x in range(w):
            image.putpixel((x, y), (255, 255, 255))
    s = image.convert('1')
    return s


def del_noise(image, image_del):
    w = image.width
    h = image.height
    for x in range(1, w - 1):
        # 获取目标像素点左右位置
        left = x - 1
        right = x + 1
        for y in range(1, h - 1):
            def num(color):
                if color == 255:
                    return 1
                else:
                    return 0

            # 获取目标像素点上下位置
            up = y - 1
            down = y + 1
            up_color = image.getpixel((x, up))  # 上
            down_color = image.getpixel((x, down))  # 下
            left_color = image.getpixel((left, y))  # 左
            left_up_color = image.getpixel((left, up))  # 左上
            left_down_color = image.getpixel((left, down))  # 左下
            right_color = image.getpixel((right, y))  # 右
            right_up_color = image.getpixel((right, up))  # 右上
            right_down_color = image.getpixel((right, down))  # 右下

            if (num(up_color)
                + num(down_color)
                + num(left_color)
                + num(left_up_color)
                + num(left_down_color)
                + num(right_color)
                + num(right_up_color)
                + num(right_down_color)) > 5:  # 如果一个黑色像素周围的8个像素中白色像素数量大于4个，则判断其为噪点，填充为白色
                image.putpixel((x, y), 255)
            elif ((num(up_color)
                   + num(down_color)
                   + num(left_color)
                   + num(left_up_color)
                   + num(left_down_color)
                   + num(right_color)
                   + num(right_up_color)
                   + num(right_down_color)) < 1):
                image.putpixel((x, y), 0)
    image.save(image_del)


def single():
    image_name = 'verify_image.jpg'
    # 读取原始图片
    image = Image.open(image_name)
    # P->RGB
    image = image.convert('RGB')
    image.save(image_name)

    image = Image.open(image_name)
    image_name_1 = 'verify_image_1.jpg'
    # RGB->1
    image = image.convert('1')
    image.save(image_name_1)

    ci.crop_img()

    crop_image0 = 'verify_image_1_crop0.jpg'
    crop_image1 = 'verify_image_1_crop1.jpg'
    crop_image2 = 'verify_image_1_crop2.jpg'
    crop_image3 = 'verify_image_1_crop3.jpg'
    crop_images = [crop_image0, crop_image1, crop_image2, crop_image3]

    for c in crop_images:
        image = Image.open(c)
        image_del = c.replace('crop', 'del')
        image.save(image_del)
        image = Image.open(image_del)
        # 缩小范围
        dn.remove_border1(image, image_del)
        for j in range(3):
            # 去除噪点
            dn.del_noise(image, image_del)
        # 水平方向噪点再去除
        dn.del_noise_num(image, image_del, 5, 8)
        dn.del_noise(image, image_del)
        # dn.del_noise_num(image, image_del, 5, 8)
        # dn.del_noise_num(image, image_del, 5, 8)
        # dn.horizontal_del(image, image_del)
        # # 垂直方向噪点再去除
        # dn.vertical_del(image, image_del)
        image = Image.open(image_del)
        image.save(image_del)


def main():
    for i in range(50):
        image_dir = 'D:/picture/'
        image_name = image_dir + 'source/' + str(i) + '.jpg'
        # 读取原始图片
        image = Image.open(image_name)
        # P->RGB
        image = image.convert('RGB')
        image.save(image_name)

        image = Image.open(image_name)
        image_name_1 = image_dir + 'format_1/' + str(i) + '.jpg'
        # RGB->1
        image = image.convert('1')
        image.save(image_name_1)

        crop_image0 = image_dir + 'crop/' + str(i) + '_0' + '.jpg'
        crop_image1 = image_dir + 'crop/' + str(i) + '_1' + '.jpg'
        crop_image2 = image_dir + 'crop/' + str(i) + '_2' + '.jpg'
        crop_image3 = image_dir + 'crop/' + str(i) + '_3' + '.jpg'
        crop_images = [crop_image0, crop_image1, crop_image2, crop_image3]

        for c in crop_images:
            image_del = c
            image = Image.open(image_del)
            # image_del = image_dir + 'del/' + str(i) + '.jpg'
            image_tif = image_del.replace('crop', 'tiff').replace('jpg', 'tif')
            # image_tif = image_dir + 'tiff/' + str(i) + '.tif'

            # # 缩小范围
            # dn.remove_border1(image, image_del)
            for j in range(3):
                # 去除噪点
                dn.del_noise(image, image_del)
            # 水平方向噪点再去除
            dn.horizontal_del(image, image_del)
            # 垂直方向噪点再去除
            dn.vertical_del(image, image_del)
            image = Image.open(image_del)
            # 保存为tif格式
            image.save(image_tif)


# main()
# single()
# rc.get_code()
