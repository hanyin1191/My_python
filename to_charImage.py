'''----------------------------------------------------------'''
'''------------------------------------------------------'''
'''--------------------------------------'''

from PIL import Image, ImageDraw, ImageFont             #导入模块


#把RGB转换成字符--------------------
def get_char(r, g, b, alpha = 256):             

    if(alpha == 0):
        return ''
    #ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. ")
    #ascii_char = list("MNHQ$OC67+>!:-. ")
    ascii_char = list("oahkbdpqwmZO0QLCJUYXzcvunxrjft")
    #ascii_char = list("MNHQ$OC67)oa+>!:+. ")

    length = len(ascii_char)

    gray = int((2126 * r + 7152 * g + 722 * b)/10000)
    #gray = (299 * r + 587 * g + 114 * b)/1000
    unit = (256 +1.0)/length
    x_in_ascii = int(gray / unit)
    return ascii_char[x_in_ascii]


#把图片转换成字符画（txt格式）
def to_CharTxt(file_name, out_file_name, multiple_width = 6, multiple_height = 15):

    text = ""

    with open(file_name, 'rb') as image_file:
        im = Image.open(image_file)

        new_width = int(im.size[0] / multiple_width)
        new_height = int(im.size[1] / multiple_height)

        im = im.resize((new_width,new_height), Image.NEAREST)       #ANTIALIAS

        for j in range(new_height):
            for i in range(new_width):
                pixel = im.getpixel((i,j))
                text += get_char(*pixel)
            text += '\n'

    print(text)

    with open(out_file_name,'w') as f:
        f.write(text)


#把图片转换成彩色字符图片-----------------
def to_ColorCharImage(file_name, out_file_name, multiple_width = 6, multiple_height = 15):

    txt = ''               #保存字符
    colors =[]             #保存颜色

    with open(file_name, 'rb') as image_file:
        im = Image.open(image_file)

        width = int(im.width / multiple_width)
        height = int(im.height / multiple_height)

        im_txt = Image.new("RGB",(im.width,im.height),(255,255,255))        
        im = im.resize((width,height), Image.NEAREST)
       
        for j in range(height):
                for i in range(width):
                        pixel = im.getpixel((i,j))
                        colors.append((pixel[0], pixel[1], pixel[2]))
                        if(len(pixel) == 4):
                                txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
                        else:
                                txt += get_char(pixel[0], pixel[1], pixel[2])
                txt += '\n'
                colors.append((255,255,255))
        
    dr = ImageDraw.Draw(im_txt)                 #设置画笔
    font = ImageFont.load_default().font        #操作字体

    font_w, font_h = font.getsize(txt[1])
    font_h *= 1.37
    
    x = y = 0
    for i in range(len(txt)):
            if(txt[i] == '\n'):
                    x += font_h
                    y = 0
            dr.text([y,x], txt[i], colors[i])       #开始画字符，位置、字符、颜色
            y += font_w

    im_txt.save(out_file_name)
    print("OK")


if __name__ == '__main__':

    to_ColorCharImage(r"C:\Users\hanyh_\Desktop\test.png", r"C:\Users\hanyh_\Desktop\test_ouput.png")
    to_CharTxt(r"C:\Users\hanyh_\Desktop\test.png", r"C:\Users\hanyh_\Desktop\test_ouput.txt")