from PIL import Image

x=135
y=40
im = Image.new("RGB", (x, y))

file = open('o.txt')

def set(r,g,b):
    s=[r,g,b]
    if(r>127):
        s[0]=255
    if(g>127):
        s[1]=255
    if(b>127):
        s[2] = 255
    return s

for i in range(0,x):
    for j in range(0,y):
        rgb = file.readline().strip().split(" ")  # 逗号分割
        print(rgb)
        if(len(rgb)!=1):
            s = set(int(rgb[0]), int(rgb[1]), int(rgb[2]))
            im.putpixel((i, j), (s[0], s[1], s[2]))  # （i,j）为坐标，后面的是像素点


im.save("flag.jpg")


