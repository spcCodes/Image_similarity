# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from src.colordescriptor import ColorDescriptor
from src.searcher import Searcher
import argparse
import cv2
import numpy as np
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
print(results)

# display the query
cv2.imshow("Query", query)
query = cv2.resize(query,(400,400))

results_arr =[]
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	result = cv2.resize(result, (400, 400))
	results_arr.append(result)
	#im = cv2.resize(result, (1000, 800))
	#imstack = np.hstack(imstack, im)


numpy_horizontal_concat = np.concatenate((query, results_arr[0],results_arr[1],results_arr[2]), axis=1)
cv2.imshow('stack',numpy_horizontal_concat)
#cv2.imshow("Result", result)
cv2.waitKey(0)