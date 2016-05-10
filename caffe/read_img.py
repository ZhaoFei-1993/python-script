import glob
import os
import skimage.io as skio

IMG_DIR = 'D:\\Project\\caffe-windows-master-zhangjunhui\\data\\pure\\blur\\'
back_end = '*.bmp'

def read_img(image_dir):
    name_list = glob.glob(image_dir + os.sep + back_end)
    for i in range(len(name_list)):
        image = skio.imread(name_list[i])
        sp = name_list[i].split('.bmp')
        skio.imsave(sp[0] + '.jpg', image)
        print "processing " + str(i) + ": " + sp[0] + '.jpg'

if __name__ == '__main__':
    read_img(IMG_DIR)