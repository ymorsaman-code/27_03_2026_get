from PIL import Image
im = Image.open('TestPicture.jpg').convert("RGB")
w,h = im.size


im1 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))
        im1.putpixel((i,j), (r,r,r))

im2 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))
        im2.putpixel((i,j), (g,g,g))

im3 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        im3.putpixel((i,j), (b,b,b))

im4 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        mx = max(r, g, b)
        im4.putpixel((i, j), (mx,mx,mx))

im5 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        mn = min(r, g, b)
        im5.putpixel((i, j), (mn,mn,mn))

im6 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        avg = (r + g + b) // 3
        im6.putpixel((i,j), (avg,avg,avg))

im7 = Image.new('RGB', (w, h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        c = (r+g+b)//3
        if (c > 127):im7.putpixel((i,j), (255,255,255))
        else :im7.putpixel((i,j), (0,0,0))

im8 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        sr = int(r * .393 + g * .769 + b * .189)
        sg = int(r * .349 + g * .686 + b * .168)
        sb = int(r * .272 + g * .534 + b * .131)
        im8.putpixel((i,j), (sr,sg,sb))

im9 = Image.new('RGB', (w,h))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i,j))
        im9.putpixel((i,j), (0,int(g * 0.5),b))

W22 = Image.new('RGB', (w * 3, h*3))
im1 = im1.crop(0,0,w//3,h//3)
im1.show()
W22.paste(im1, (0,0))
W22.paste(im2, (w,0))
W22.paste(im3, (w*2,0))
W22.paste(im4, (0,h))
W22.paste(im5, (w,h))
W22.paste(im6, (w*2,h))
W22.paste(im7, (0,h*2))
W22.paste(im8, (w,h*2))
W22.paste(im9, (w*2,h*2))

W22.save('WatWaAram22.jpg')
