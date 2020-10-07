import ctypes
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from termcolor import colored

def read_convert_imgs(imgs):
    imgs = [cv.imread(str(imgs[i])) for i in range(len(imgs))]
    imgs = [cv.cvtColor(img, cv.COLOR_BGR2RGB) for img in imgs]
    return imgs


def resize_all(imgs):
    for i,im in enumerate(imgs):
        imgs[i] = cv.resize(im, (250,250), interpolation=cv.INTER_AREA)

    return imgs


def calculate_grid_size(num_imgs):
    rows = int(np.ceil(np.sqrt(num_imgs)))
    cols = rows

    return rows,cols


def show_multiple_images(imgs,rows,cols,figsize=(20,20)):
    fig=plt.figure(figsize=figsize)
    for i in range(1, cols*rows +1):
        try:
            img = imgs[i]
        except:
            img = np.random.randint(10, size=img.shape)
        fig.add_subplot(rows, cols, i)
        plt.title("Image index: {}".format(i), fontsize=15)
        plt.subplots_adjust(wspace=0.2, hspace=0.4)
        plt.imshow(img)

    plt.show()


def get_screensize(multiplier):
    user32 = ctypes.windll.user32
    screensize = "{}x{}".format(user32.GetSystemMetrics(78)*multiplier,user32.GetSystemMetrics(79)*multiplier)
    print(user32.GetSystemMetrics(78),user32.GetSystemMetrics(79))


if __name__ == "__main__":
    get_screensize(1)
    backgroundImages = list(pathlib.Path(r"C:\Users\lucas\Pictures\background_images").iterdir())
    imgs = read_convert_imgs(backgroundImages)
    imgs = resize_all(imgs)
    #imgs.insert(0, np.zeros(shape=imgs[0].shape)) # inserting a placeholder image to match rows and columns
    #backgroundImages.insert(0,"placeholder.png") # matching the index with images
    rows,cols = calculate_grid_size(len(imgs))
    show_multiple_images(imgs,rows,cols,figsize=(20,20))
    choose_img_index = int(input("What is the image you want to set as background?(index: 1,2,3,4....)")    )
    choosen_image = backgroundImages[choose_img_index]
    print(colored("You chose this image:"))
    print(colored(str(choosen_image)))
    plt.imshow(imgs[choose_img_index])
    plt.show()
    ctypes.windll.user32.SystemParametersInfoW(20,0,str(choosen_image),0)      
    


        
    





