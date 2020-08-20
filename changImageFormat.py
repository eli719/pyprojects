from PIL import Image

image = Image.open('3.jpg')  # type:Image.Image
print(image)
image = image.convert('RGB')  # P->RGB
image = image.save('p_3.jpg')
image = Image.open('p_3.jpg')
print(image)


def changFormat(type):
    print(image.getpixel((0, 0)))
    im = image.convert(type)
    im.save('lena_' + type + '_1.jpg')
    print(im)
    print(im.getpixel((0, 0)))
    # im.show()

'''
模式“1”为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白。下面我们将lena图像转换为“1”图像
'''
changFormat('1')

'''
模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的：
L = R * 299/1000 + G * 587/1000+ B * 114/1000
'''
# changFormat('L')

'''
模式“P”为8位彩色图像，它的每个像素用8个bit表示，其对应的彩色值是按照调色板查询出来的。
'''
# print(image.getpixel((0, 0)))
# image = image.convert('P')
# # image.save('lena_' + 'P' + '.png')
# print(image)
# print(image.getpixel((0, 0)))
# image.show()
# changFormat('P')
