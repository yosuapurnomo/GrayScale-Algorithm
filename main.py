import sys
import cv2
import numpy as np
import keyboard as keyboard

def GrayScale_i(img):
    # Algoritma i = (R+G+B)/3
    shape = np.array(img)
    for x in range(shape.shape[0]):
        for y in range(shape.shape[1]):
            img[[x], [y]] = int(np.sum(img[[x], [y]])/3)
    # print(f"Total Akhir : \n{img}")
    return img

def GrayScale_I(img):
    # Algoritma I = 0,2989 x R + 0,5870 x G + 0,1141 x B
    shape = np.array(img)
    for x in range(shape.shape[0]):
        for y in range(shape.shape[1]):
            img[[x], [y]] = int((0.2989 * img[[x], [y], [2]]) + (0.5870 * img[[x], [y], [1]]) + (0.1141 * img[[x], [y], [0]]))
    # print(f"Total Akhir : \n{img}")
    return img

Image_Crop = False
ix, iy, ix_end, iy_end = 0,0,0,0

# Mengambil Gambar
img = cv2.imread('raja-ampat.jpg')

def mouse_crop(event, x, y, flags, param):
    # Set Global Variable
    global ix, iy, ix_end, iy_end, Image_Crop

    # jika mouse klik kiri maka akan direkam titik x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy, ix_end, iy_end = x, y, x, y
        Image_Crop = True

    # Merekam Pergerakan Mouse
    elif event == cv2.EVENT_MOUSEMOVE:
        if Image_Crop == True:
            ix_end, iy_end = x, y

    # Jika Mouse klik dilepas maka akan Mengambil titik x, y dan disimpan pada variable x_end, y_end
    elif event == cv2.EVENT_LBUTTONUP:
        # Record Titik Koordinat akhir
        ix_end, iy_end = x, y
        Image_Crop = False  # Crooping Selasai

        titik = [(ix, iy), (ix_end, iy_end)]

        if len(titik) == 2:  # ketika kedua titik point ditemukan

            # Algoritma i
            HasilGray_i = GrayScale_i(img[titik[0][1]:titik[1][1], titik[0][0]:titik[1][0]].copy())
            cv2.imshow("Hasil GrayScale i", HasilGray_i) # Image Output Bagihan Atas

            HasilGray_I = GrayScale_I(img[titik[0][1]:titik[1][1], titik[0][0]:titik[1][0]].copy())
            cv2.imshow("Hasil GrayScale I", HasilGray_I) # Image Output Bagihan Bawah
            cv2.moveWindow("Hasil GrayScale I", 120, 250)

# Title Frame harus sama dengan Origin Images
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

while True:
    image_copy = img.copy()

    if not Image_Crop:
        cv2.imshow('image', img)

    elif Image_Crop:
        cv2.rectangle(image_copy, (ix, iy), (ix_end, iy_end), (255, 0, 0), 2)
        cv2.imshow("image", image_copy)

    # Untuk Mengakhiri Press Ecs
    if keyboard.is_pressed('Esc'):
        sys.exit(0)
    cv2.waitKey(1)

cv2.destroyAllWindows()


