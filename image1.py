from PIL import Image
import requests as rq
from PIL import ImageFilter

# 访问验证码链接并保存到本地
for i in range(50):
    rp = rq.get('http://zgcx.nhc.gov.cn:9090/CaptchaGenerate/Generate/')
    with open('D://picture/source/'+str(i)+'.jpg','wb') as f:
      f.write(rp.content)
# dir = r'D:/picture'
#
# file_name = dir+"/"+"1.jpg"
# # 读取验证码图片
# image = Image.open(file_name) #type:Image.Image
#
# # 二值化
# # image.format 这个属性标识了图像来源，如果图像不是从文件读取它的值就是None。
# print(image.format, image.size, image.mode)
# image = image.convert('RGB')
# two_file = dir+"/two"+'/1.jpg'
# image.save(two_file)
# image = Image.open(dir+"/two"+"/1.jpg")
# f = open("o.txt", 'w+')
# print(image.format, image.size,image.mode)
#
# img_array=image.load()
# print(img_array)
# for i in range(135):
# 	for j in range(40):
# 		r, g, b = image.getpixel((i, j))
# 		print(r, g, b,file=f)



# r,g,v=image.split()
# # r.show()
# g.show()
# v.show()
# bluF = image.filter(ImageFilter.BLUR)##均值滤波
# conF = image.filter(ImageFilter.CONTOUR)##找轮廓
# edgeF = image.filter(ImageFilter.FIND_EDGES)##边缘检测
# image.show()
# bluF.show()
# conF.show()
# edgeF.show()

# image.show()


