from PIL import Image  # 用于打开图片和对图片处理
import pytesseract


def processing_image(self):
    # image_obj = self.get_pictures()  # 获取验证码
    img = self.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    threshold = 80
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


def delete_spot(self):
    # images = self.processing_image()
    data = self.getdata()
    w, h = self.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    self.putpixel((x, y), 255)
                black_point = 0
    self.show()
    return self


image = Image.open('p_3.jpg')#type:Image.Image
image=processing_image(image)
delete_spot(image)
image.save('verify3.jpg')
code = pytesseract.image_to_string(image)
print(code)