import os
from simplejpeg import decode_jpeg
import numpy as np
from natsort import natsorted,ns
import cv2
from configure import Config
config = Config()

#256-5, 192-7, 128-11, 96-13, 64-19 -> namjesteni su patch_size i no_patches tako da bude patch_size*no_patches minimalno veci od velicine slike
# no mozda bi bilo bolje staviti vise no_patches, npr. size=64, no_patches=23, tako da se dobije vise preklapajucih patcheva, a s time i vise
# slika s "centriranim" krvnim zilama

patch_size = config.patch_size
no_patches = config.no_of_patches #in one direction, equal in all directions

ext1 = "Train"
ext2 = "train"

#img_dir = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled\\" + ext2 + "\\"
#mask_dir = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled\\" + ext2 + "_masks\\"
#img_dst = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch"+str(patch_size)+"\\"+ext2+"\\"
#mask_dst = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch"+str(patch_size)+"\\"+ext2+"_masks\\"

#LAD7
#path = r"C:\Users\Jakov\Documents\Misc\FER - jakov\5. semestar\Projekt R\Materijali - segm. srca\Git-Projekt R\notebooks\UNet\Train_images"
path = "/content/projektR/notebooks/UNet/Train_images"
img_dir = path + "/orig_train/"
mask_dir = path + "/orig_train_masks/"
img_dst = path + "/extracted_train/"
mask_dst = path + "/extracted_train_masks/"

if not os.path.exists(img_dst):
    os.makedirs(img_dst)
if not os.path.exists(mask_dst):
    os.makedirs(mask_dst)

img_list = natsorted(os.listdir(img_dir), alg=ns.IGNORECASE)
mask_list = natsorted(os.listdir(mask_dir), alg=ns.IGNORECASE)

'''//
print(mask_dst)
print(img_dst)

os.makedirs(mask_dst + "bla")
'''



#for i in range(0,len(img_list)):
for i in range(0,4):				##PROMIJENITI, OVO JE PROBNO
    with open(os.path.join(img_dir, img_list[i]), 'rb') as f1:
        image = decode_jpeg(f1.read())[:, :, 1]
    with open(os.path.join(mask_dir, mask_list[i]), 'rb') as f2:
        mask = decode_jpeg(f2.read())[:, :, 1]

    print("Extracting from original image: ", i, "/",len(img_list))
    w0, h0 = image.shape
    overlap_w = int((no_patches*patch_size - w0) / (no_patches-1))
    overlap_h = int((no_patches * patch_size - h0) / (no_patches - 1))
    idx_w = patch_size - overlap_w-1
    idx_h = patch_size - overlap_h - 1
    for j in range(0,no_patches,1):
        for k in range(0,no_patches,1):
            cv2.imwrite(img_dst + img_list[i].rsplit('.')[0] + '_' + str(j*no_patches+k+1) + '.jpeg', image[idx_w*j:idx_w*j+patch_size, idx_h*k:idx_h*k+patch_size])
            cv2.imwrite(mask_dst + mask_list[i].rsplit('.')[0] + '_' + str(j * no_patches + k + 1) + '.jpeg', mask[idx_w * j:idx_w * j + patch_size, idx_h * k:idx_h * k + patch_size])
