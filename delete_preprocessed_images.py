import os, shutil
from os import path
from os.path import basename
from configure import Config
config = Config()

folders = []

#
folders.append("/content/projektR/notebooks/UNet/Train_images/train")
folders.append("/content/projektR/notebooks/UNet/Train_images/train_masks")
folders.append("/content/projektR/notebooks/UNet/Train_images/resampled_train")
folders.append("/content/projektR/notebooks/UNet/Train_images/resampled_train_masks")
folders.append("/content/projektR/notebooks/UNet/Train_images/extracted_train")
folders.append("/content/projektR/notebooks/UNet/Train_images/extracted_train_masks")

folders.append("/content/projektR/notebooks/UNet/Validation_images/validation")
folders.append("/content/projektR/notebooks/UNet/Validation_images/validation")
folders.append("/content/projektR/notebooks/UNet/Validation_images/resampled_validation")
folders.append("/content/projektR/notebooks/UNet/Validation_images/resampled_validation_masks")
folders.append("/content/projektR/notebooks/UNet/Validation_images/extracted_validation")
folders.append("/content/projektR/notebooks/UNet/Validation_images/extracted_validation_masks")

for folder in folders:
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))