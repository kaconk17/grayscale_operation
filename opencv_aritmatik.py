import cv2 as cv
import numpy as np
print("Operasi Aritmatika pada gambar Pilih salah satu opsi :")
print("1. Menambah nilai image grayscale")
print("2. Mengurangi nilai image grayscale")
print("3. Mendapatkan gambar MAX dari 2 gambar")
print("4. Mendapatkan gambar MIN dari 2 gambar")
print("5. Melakukan Inverse pada gambar")
pilih = input("Opsi :")

def add_nilai(gb, val):
    plus = cv.add(gb, val)
    print('Hasil penambahan dengan nilai : '+str(val))
    print(plus)
    screen = np.hstack((gb,plus))
    cv.imshow('Gambar Original VS Penambahan '+ str(val), screen)
    cv.waitKey(0)

def sub_nilai(gb, val):
    kurang = cv.subtract(gb, val)
    print('Hasil pengurangan dengan nilai : '+str(val))
    print(kurang)
    screen = np.hstack((gb,kurang))
    cv.imshow('Gambar Original VS Pengurangan '+str(val), screen)
    cv.waitKey(0)

def max_img(gb1, gb2):
    img1 = cv.resize(gb1,(400,400))
    img2 = cv.resize(gb2,(400,400))
    gb_max = cv.max(img1,img2)
    print('hasil operasi MAX')
    print(gb_max)
    gb_stack = np.hstack((img1, img2))
    screen = np.hstack((gb_stack, gb_max))
    cv.imshow('Hasil operasi MAX', screen)
    cv.waitKey(0)

def min_img(gb1, gb2):
    img1 = cv.resize(gb1,(400,400))
    img2 = cv.resize(gb2,(400,400))
    gb_min = cv.min(img1,img2)
    print('hasil operasi MIN')
    print(gb_min)
    gb_stack = np.hstack((img1, img2))
    screen = np.hstack((gb_stack, gb_min))
    cv.imshow('Hasil operasi MIN', screen)
    cv.waitKey(0)
def inv_img(gb):
    gb_inv = (255-gb)
    print(gb)
    print('Hasil inverse')
    print(gb_inv)
    screen = np.hstack((gb,gb_inv))
    cv.imshow('Gambar Original VS inverse',screen)
    cv.waitKey(0)

if pilih == "1" :
    src = input("Drag gambar kesini !")
    nilai = input("Masukkan nilai !")
    img = cv.imread(src,0)
    print(img)
    add_nilai(img,int(nilai))
elif pilih == "2":
    src = input("Drag gambar kesini !")
    nilai = input("Masukkan nilai !")
    img = cv.imread(src,0)
    print(img)
    sub_nilai(img,int(nilai))
elif pilih == "3":
    src1 = input("Drag gambar 1 !")
    src2 = input("Drag gambar 2 !")
    img1 = cv.imread(src1,0)
    img2 = cv.imread(src2,0)
    max_img(img1, img2)
elif pilih == "4":
    src1 = input("Drag gambar 1 !")
    src2 = input("Drag gambar 2 !")
    img1 = cv.imread(src1,0)
    img2 = cv.imread(src2,0)
    min_img(img1, img2)
elif pilih == "5":
    src1 = input("Drag gambar !")
    img1 = cv.imread(src1,0)
    inv_img(img1)
else :
    print('Opsi tidak ditemukan !')