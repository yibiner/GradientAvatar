from PIL import Image

# 读取图片，并将五星红旗图片尺寸重置为头像图片的尺寸
s_avatar = Image.open('头像.jpg').convert("RGBA")
s_banner = Image.open('国旗.png').convert("RGBA").resize(s_avatar.size)

# 将五星红旗图片设置透明渐变
w, h = s_banner.size
for i in range(w):
    for j in range(h):
        alpha = int(255-(i*(255/int(w*0.8)))) if int(255-(i*(255/int(w*0.8)))) > 0 else 0
        s_banner.putpixel((i, j), s_banner.getpixel((i, j))[:-1] + (alpha, ))

# 将五星红旗图片粘贴到头像图片并保存 
s_avatar.paste(s_banner, (0,0), s_banner)
s_avatar.save('国庆半透明渐变头像.png')