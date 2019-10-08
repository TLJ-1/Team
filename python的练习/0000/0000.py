#给图片加上右上标数字
import cv2
from PIL import Image,ImageFont,ImageDraw  #导入相关图片的模块
import numpy as np

bk_image=cv2.imread("0000.jpg")

#设置字体、字号等
fontpath='C:/WINDOWS/FONTS/SIMKAI.ttf'
font=ImageFont.truetype(fontpath,44)
img_pil = Image.fromarray(bk_image)  ##
draw = ImageDraw.Draw(img_pil)

draw.text((10,10),"臭猪猪",font=font,fill=(10,110,170))
#draw.text((40,40),"是猪",fill=(0,0,0),font=font)
bk_image = np.array(img_pil)

cv2.imshow("add_text",bk_image)
cv2.waitKey()
cv2.imwrite("add_text.jpg",bk_image)


"""#准备工作
#指定要用的字体和大小颜色
font=ImageFont.truetype('C:/WINDOWS/FONTS/SIMKAI.ttf',44,index=0)
#image:图片，text:要加上去的字 font:字体
def add_text_to_image(image,text,font=font):
    rgba_image=image.convert('RGBA')  #
    text_overlay=image.new('RGBA',rgba_image.size,(255,255,255,0))
    image_draw=ImageDraw.Draw(text_overlay)
    text_size_x,text_size_y=image_draw.textsize(text,font=font)

    #设置文本位置
    print(rgba_image)
    text_xy=((rgba_image.size[0]-text_size_x)/2,(rgba_image.size9[0]-text_size_y)/2)

    #设置文本颜色和透明度
    image_dram.text(text_xy,text,font=font,fill=(255,255,255,255))
    image_with_text=image.alpha_composite(rgba_image,text_overlay)
    return image_with_text

image_before=Image.open("0000.jpg")

image_after=add_text_to_image(image_before,'你好')
image_after.show()
"""