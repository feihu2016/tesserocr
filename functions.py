#encoding=utf-8


def bina(img, threshold):
     img = img.convert("L")
     pixdata  = img.load()
     w, h = img.size
     for y in range(h):
         for x in range(w):
             if pixdata[x, y] < threshold:
                 pixdata[x, y] = 0
             else:
                 pixdata[x, y] = 255
     return img



def depoint(img):
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:#上
                count = count + 1
            if pixdata[x,y+1] > 245:#下
                count = count + 1
            if pixdata[x-1,y] > 245:#左
                count = count + 1
            if pixdata[x+1,y] > 245:#右
                count = count + 1
            if pixdata[x-1,y-1] > 245:#左上
                count = count + 1
            if pixdata[x-1,y+1] > 245:#左下
                count = count + 1
            if pixdata[x+1,y-1] > 245:#右上
                count = count + 1
            if pixdata[x+1,y+1] > 245:#右下
                count = count + 1
            if count > 4:
                pixdata[x,y] = 255
    return img
