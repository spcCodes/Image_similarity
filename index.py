# USAGE
# python index.py --dataset dataset --index index.csv

# import the necessary packages
from src.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output = open(args["index"], "w")

data = args["dataset"]
# sub directories or class name path
class_path = glob.glob(data + '*')

for f in class_path:

    image_list = glob.glob(f + '/*')

    # use glob to grab the image paths and loop over them
    for imagePath in image_list:
        # name of the file with extension
        base_file_name = os.path.basename(imagePath)

        try:
            # just name of the file
            label_test = base_file_name.split('.jpg')[0]
            image = cv2.imread(imagePath)
            # describe the image
            features = cd.describe(image)
            # write the features to file
            features = [str(f) for f in features]
            output.write("%s,%s\n" % (label_test, ",".join(features)))

        except:
            continue


# close the index file
output.close()
