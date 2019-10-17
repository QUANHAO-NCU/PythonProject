from PIL import Image, ImageFilter

im = Image.open('plmm.jpg')
im3 = im
im2 = im
w, h = im.size
print('The size of this image is w:{},h:{}'.format(w, h))
im3.thumbnail((w // 2, h // 2))

im3.save('thumbnail.jpg', 'jpeg')

for i in range(10):
    im2 = im2.filter(ImageFilter.BLUR)
im2.save('blur.jpeg', 'jpeg')
