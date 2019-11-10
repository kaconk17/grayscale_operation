import cv2 as cv
import numpy as np
print("Operasi Logika pada gambar Pilih salah satu opsi :")
print("1. Operasi NOT image grayscale")
print("2. Operasi AND pada 2 image grayscale")
print("3. Operasi OR pada 2 image grayscale")
print("4. Operasi XOR pada 2 image grayscale")
pilih = input("Opsi :")

def op_not(gb):
    gb_not = cv.bitwise_not(gb)
    print('Hasil operasi NOT')
    print(gb_not)
    screen = np.hstack((gb,gb_not))
    cv.imshow('Gambar Original VS Operasi NOT ', screen)
    cv.waitKey(0)

def op_and(gb1, gb2):
    img1 = cv.resize(gb1,(400,400))
    img2 = cv.resize(gb2,(400,400))
    gb_and = cv.bitwise_and(img1,img2)
    print('Hasil operasi AND')
    print(gb_and)
    gb_stack = np.hstack((img1,img2))
    screen = np.hstack((gb_stack,gb_and))
    cv.imshow('Hasil operasi AND', screen)
    cv.waitKey(0)

def op_or(gb1, gb2):
    img1 = cv.resize(gb1,(400,400))
    img2 = cv.resize(gb2,(400,400))
    gb_or = cv.bitwise_or(img1,img2)
    print('hasil operasi OR')
    print(gb_or)
    gb_stack = np.hstack((img1,img2))
    screen = np.hstack((gb_stack,gb_or))
    cv.imshow('Hasil operasi OR', screen)
    cv.waitKey(0)

def op_xor(gb1, gb2):
    img1 = cv.resize(gb1,(400,400))
    img2 = cv.resize(gb2,(400,400))
    gb_xor = cv.bitwise_xor(img1,img2)
    print('Hasil operasi XOR')
    print(gb_xor)
    gb_stack = np.hstack((img1,img2))
    screen = np.hstack((gb_stack,gb_xor))
    cv.imshow('Hasil operasi XOR', screen)
    cv.waitKey(0)

if pilih == "1" :
    src = input("Drag gambar kesini !")
    img = cv.imread(src,0)
    print(img)
    op_not(img)
elif pilih == "2":
    src1 = input("Drag gambar 1 kesini !")
    src2 = input("Drag gambar 2 kesini !")
    
    img1 = cv.imread(src1,0)
    img2 = cv.imread(src2,0)
    print(img1)
    print(img2)
    op_and(img1,img2)
elif pilih == "3":
    src1 = input("Drag gambar 1 !")
    src2 = input("Drag gambar 2 !")
    img1 = cv.imread(src1,0)
    img2 = cv.imread(src2,0)
    op_or(img1, img2)
elif pilih == "4":
    src1 = input("Drag gambar 1 !")
    src2 = input("Drag gambar 2 !")
    img1 = cv.imread(src1,0)
    img2 = cv.imread(src2,0)
    op_xor(img1, img2)
else :
    print('Opsi tidak ditemukan !')
