import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt


#Отдельная функция под ошибки, чтобы не дублировать код
def error_msg():
    print("You've entered wrong or negative number\n")
    if_func()


# Функция для вывода изображения
def print_new_image(imagine):
    print(imagine.shape)
    plt.imshow(imagine, vmin=0, vmax=255)
    plt.show()


# Функция делает картинку черно белой. Берем любой слой и в RGB ставим одинаковые значени
def make_gray(imagine):
    gray_v = int(input("Enter from 1 to 255\n"))
    if gray_v > 255:
        error_msg()
    elif gray_v < 1:
        error_msg()
    else:
        red = imagine[:, :, 0]
        mod_red = np.where(red > gray_v, red, 0)
        imagine[:, :, 0] = mod_red
        plt.gray()
        print_new_image(mod_red)


# Функция изменения картинки на y% коорд. При reshape=False не будет меняться расширение картинки,
# но при повороте не будет углов, работает при отрицательных значениях.
def rotate_y(imagine):
    y_rot = int(input("Enter y%:\n"))
    imagine = ndimage.rotate(imagine, y_rot, reshape=True)
    print_new_image(imagine)


# Функция изменения высоты, при отрицательных значениях выкидывает ошибку
def change_height(imagine):
    new_height = int(input("Enter new height:\n"))
    if new_height < 0:
        error_msg()
    imagine = ndimage.zoom(imagine, (new_height / 768, 1.0, 1.0))
    print_new_image(imagine)


# Функция изменения ширины, при отрицательных значениях выкидывает ошибку
def change_weight(imagine):
    new_weight = int(input("Enter new weight:\n"))
    if new_weight < 0:
        error_msg()
    imagine = ndimage.zoom(imagine, (1.0, new_weight / 1024, 1.0))
    print_new_image(imagine)


# Вызов одной из функций выше, изначально хотел сделать что-то вроде switch_case,
# но его в питоне нет, нашел пару альтернатив, но тут они не применимы
def if_func():
    copy_image = image.copy()
    help_num = int(input("Enter:\n1. Rotate y%\n2. Change height\n3. Change weight\n4. Make picture gray\n"))
    if help_num == 1:
        rotate_y(copy_image)
    elif help_num == 2:
        change_height(copy_image)
    elif help_num == 3:
        change_weight(copy_image)
    elif help_num == 4:
        make_gray(copy_image)
    else:
        error_msg()


image = misc.face()
if_func()
