from PIL import Image


def is_pixel_equal( image1, image2, x, y):
    """
    判断两个像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param x: 位置x
    :param y: 位置y
    :return: 像素是否相同
    """
    # 取两个图片的像素点
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:

        return True
    else:
        print(pixel1, pixel2)
        return False

def get_gap( image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 0
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left


img1 = Image.open('verify_image1.jpg') #type:Image.Image
img2 = Image.open('verify_image2.jpg')
point = get_gap(img1,img2)
print(point)


