import PIL.Image as img


def crop_img():
    IMG = 'verify_image_1.jpg'  # 图片地址
    im = img.open(IMG)  # 用PIL打开一个图片
    box1 = (20, 5, 45, 30)  # box代表需要剪切图片的位置格式为:xmin ymin xmax ymax
    box2 = (46, 4, 65, 31)
    box3 = (70, 5, 93, 34)
    box4 = (94, 1, 120, 26)
    boxes = [box1, box2, box3, box4]
    for i in range(len(boxes)):
        im.crop(boxes[i]).save('verify_image_1_crop' + i.__str__() + '.jpg')

