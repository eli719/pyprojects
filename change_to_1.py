from PIL import Image


def changFormat(kind):
    image = Image.open('verify_image.jpg')  # type:Image.Image
    # print(image)
    image = image.convert('RGB')  # P->RGB
    image = image.save('verify_image.jpg')
    image = Image.open('verify_image.jpg')
    # print(image)
    print(image.getpixel((0, 0)))
    im = image.convert(kind)
    im.save('verify_' + kind + '_1.jpg')
    print(im)
    print(im.getpixel((0, 0)))
    # im.show()

