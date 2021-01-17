import os
from zipfile import ZipFile
from os import path
from os.path import basename
from configure import Config
config = Config()

folders_for_zipping = []

train_path = config.train_orig
folders_for_zipping.append(train_path)

train_masks_path = config.train_orig + "/masks"
folders_for_zipping.append(train_path_masks)

validation_path = config.valid_orig
folders_for_zipping.append(valid_path)

validation__masks_path = config.valid_orig + "/masks"
folders_for_zipping.append(valid_path_masks)




def add_folder_to_zip(zipObj, folderPath):
	zipObj.write(folderPath, basename(folderPath))
	for filename in os.listdir(folderPath):
		filePath = os.path.join(folderPath, filename)
		if path.isfile(filePath):
			print("Adding file to zip: {}".format(filename))
			zipObj.write(filePath, os.path.join(basename(folderPath),basename(filePath)))

with ZipFile ("preprocessed_images.zip", 'w') as zipObj:
	for folder_to_zip in folders_for_zipping:
		add_folder_to_zip(folder_to_zip)





