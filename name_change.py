
import cv2
import glob
import os


data = 'dataset_similarity/shirt/'
# sub directories or class name path
class_path = glob.glob(data + '/*')


output_path = 'dataset_similarity/shirt_modified/'

for imagePath in class_path:
    # name of the file with extension
    base_file_name = os.path.basename(imagePath)

    output_name = output_path+ 'shirt'+ base_file_name

    img = cv2.imread(imagePath)

    #im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.imwrite(output_name , img)
