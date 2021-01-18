import os
from zipfile import ZipFile
from os import path
from os.path import basename
from configure import Config
config = Config()

folders = []

train_path = config.train_orig
folders.append(train_path)

train_masks_path = config.train_orig + "_masks"
folders.append(train_masks_path)

validation_path = config.valid_orig
folders.append(validation_path)

validation_masks_path = config.valid_orig + "_masks"
folders.append(validation_masks_path)

# simple version for working with CWD
#print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
for folder in folders:
	print ("Folder {} contains {} files.".format(folder, len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])))
