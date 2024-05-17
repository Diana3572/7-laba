import ImageFilter
from PIL import Image
def nn1():
    image = Image.open('photo.jpg')
    print(f"Формат: {image.format}")
    print(f"Размер: {image.size}")
    print(f"Цветовая модель: {image.mode}")
    image.show()

print(nn1())


def nn2():
    image = Image.open('photo.jpg')
    res_img2 = image.reduce(3)
    res_img2.save('photo_ув.jpg')
    res_img3 = image.transpose(Image.ROTATE_180)
    res_img4 = image.transpose(Image.ROTATE_90)
    res_img3.save('photo_180.jpg')
    res_img4.save('photo_90.jpg')
    image.show()
    res_img3.show()
    res_img4.show()

print(nn2())

def nn3():
    x = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for name in x:
        image = Image.open(name)
        toned_image = Image.eval(image, lambda x: x * 0.5)
        n = name.replace(".", "new.")
        toned_image.save(n)
        toned_image.show()

print(nn3())







