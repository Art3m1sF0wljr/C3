python3 bmp_gen_file.py

the input file is test_13_LRPT.txt

it generates a bitmap from random input. the input is garbage, use it with te output of test_13_QPSK_my_LRPT.grc

write python code that given input a file containing garbage hex values, read them as bytes and take groups of three. handle the case where there is no valid hex written (ignore it)
given a group , interpret it as a triplet of RGB color channels, for a pixel , valued from 0 to 255

create a bitmap image using the triplets, each triplet for a pixel. populate the bitmap row wise, such that each row has 456 pixels. the number of columns depend on the length of the input file. If the triplets are n < 456 handle by returning a bitmap 1xn
if them are n>456, return the bitmap and the pixels that remain until the 456th column colour them green
