from PIL import Image, ImageFilter


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(
        ((img_width - crop_width) // 2, (img_height - crop_height) // 2,
         (img_width + crop_width) // 2, (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


im = Image.open('./sample.jpg')
print(im.format, im.size, im.mode)

im_new = crop_max_square(im)
im_new.save('hoge1.jpg')

img_resize_lanczos = im_new.resize((500, 500), Image.LANCZOS)
img_resize_lanczos.save('hoge.jpg')