import os
from simplejpeg import decode_jpeg
import numpy as np
from natsort import natsorted,ns
import cv2
import shutil
import random

'''
ext1 = "Train"
ext2 = "train"

img_dir = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch64\\"+ext2+"\\"
mask_dir = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch64\\"+ext2+"_masks\\"
dst_mask = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch64_strat\\"+ext2+"_vmasks\\"
dst_img = r"T:\\Dataset_vascular\\"+ext1+r"_images_full_sampled_patch64_strat\\"+ext2+"v\\"
'''

def execute(ext1, ext2):
	path = "/content/projektR/notebooks/UNet/" + ext1 + "_images"
	img_dir = path + "/resampled_" + ext2 + "/"
	mask_dir = path + "/resampled_" + ext2 + "_masks/"
	dst_img = path + "/" + ext2 + "/"
	dst_mask = path + "/" + ext2 + "_masks/"

	img_list = natsorted(os.listdir(img_dir), alg=ns.IGNORECASE)
	mask_list = natsorted(os.listdir(mask_dir), alg=ns.IGNORECASE)
	cnt_vessel = 0
	cnt_background = 0
	idx = []
	idxv = []

	if not os.path.exists(dst_img):
		os.makedirs(dst_img)
	if not os.path.exists(dst_mask):
		os.makedirs(dst_mask)

	print("Labelling data...")
	for i in range(0,len(mask_list)):
		with open(os.path.join(mask_dir, mask_list[i]), 'rb') as f1:
			image = decode_jpeg(f1.read())[:, :, 1]/255
	#ako je suma piksela veca od 10, zabiljezi indeks slike kao sliku pozadine
		if image.sum()<=10:
			cnt_background = cnt_background + 1
			idx.append(i)
	#inace zabiljezi indeks slike kao sliku krvne zile
		else:
			cnt_vessel = cnt_vessel + 1
			idxv.append(i)
	print("Labelling complete.")

	print("Vessel masks: ", str(cnt_vessel))
	print("Background masks: ", str(cnt_background))


	print("Copying preprocessed files to destination...")
	
	
	#kopiraj slike na kojima nema krvnih zila -> uzima random sliku na kojoj nema krvne zile, ukupan broj mora biti jednak kao broj slika na kojima ima krvnih zila
	#radi li ovo?
	'''
	idxr = random.sample(idx, len(idxv))
	for i in idxr:
		shutil.copy(mask_dir + mask_list[i], dst_mask + mask_list[i])
		shutil.copy(img_dir + img_list[i], dst_img + img_list[i])
	'''

	#kopiraj slike na kojima ima zila
	for i in idxv:
		shutil.copy(mask_dir + mask_list[i], dst_mask + mask_list[i])
		shutil.copy(img_dir + img_list[i], dst_img + img_list[i])

	#print("Folder {} contains {} images".format(dst_img, len(idxv) + len(idxr) ))
	print("Folder {} contains {} images".format(dst_img, len(idxv)))
	print("Copying complete.")