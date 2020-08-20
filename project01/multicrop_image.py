import PIL.Image as img


def crop_img():
    image_dir = 'D:/picture/'
    for i in range(50):
        format_1 = image_dir + 'format_1/' + str(i) + '.jpg'
        im = img.open(format_1)  # 用PIL打开一个图片
        box1 = (20, 5, 45, 30)  # box代表需要剪切图片的位置格式为:xmin ymin xmax ymax
        box2 = (43, 5, 65, 30)
        box3 = (70, 5, 93, 33)
        box4 = (95, 3, 120, 25)
        boxes = [box1, box2, box3, box4]

        for j in range(len(boxes)):
            crop_img = image_dir + 'crop/' + str(i) + '_' + str(j) + '.jpg'
            im.crop(boxes[j]).save(crop_img)


# crop_img()
