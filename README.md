# Image_similarity
The objective of the project is that given a query image, it will find 3 most similar image from the given image directory. The images may be the duplicate images or the most simlar ones.

## Table of contents
* [General info](#general-info)
* [Project Structure](#project_str)
* [Dataset](#data)
* [Project Execution Steps](#project)
* [Result Similar Images](#similar)
* [Conclusion](#conclusion)
* [Future Work](#future)

<a name="general-info"></a>
## General info

The objective of this project is to find out the similar images from the images directory given a query image. The dataset for this project is available in data directory. However beacuse github has its own storage constraints all the data, all the data is not reflecting in the **data** folder . 

The data can be downloaded from **[dataset](https://drive.google.com/open?id=1_Qww0NbYJOH17IiTr7bgXWQTQTFD-V9R)**. If you face downloading the dataset , do drop me a mail to gain the access credentials.

Any Content-Based Image Retrieval System we are building, they all can be boiled down into 4 distinct steps:

* **Defining your image descriptor**: At this phase we need to decide what aspect of the image we want to describe. Are we interested in the color of the image or in the shape of an object in the image or we want to characterize texture?
* **Indexing your dataset**: Now that we have our image descriptor defined, our job is to apply this image descriptor to each image in our dataset, extract features from these images, and write the features to storage (ex. CSV file) so that they can be later compared for similarity.
* **Defining our similarity metric**: We have a bunch of feature vectors. But how do we compare them? Popular choices include the Euclidean distance, Cosine distance, and chi-squared distance, but the actual choice is highly dependent on (1) our dataset and (2) the types of features we extracted.
* **Searching**: The final step is to perform an actual search. A user will submit a query image to our system (from an upload form or via a mobile app, for instance) and our job will be to 

(1) extract features from this query image and then 

(2) apply our similarity function to compare the query features to the features already indexed. From there, we simply return the most relevant results according to our similarity function.

Steps 1 and 2 involves the following:

<div style="text-align: center"><img src="images/preprocessing_and_indexing.jpg" width="700"/></div>

We can then move on to performing a search (Steps 3 and 4):

<div style="text-align: center"><img src="images/searching.jpg" width="700"/></div>

<a name="project_str"></a>
## Project Structure

The entire project structure is as follows:
```
├── data
|__ images1.jpg
|__ images2.jpg
|__ .....
├── images
│   ├── preprocessing_and_indexing.jpg
│   └── searching.jpg
├── queries
│   ├── Classic_Mid-Rise_Skinny_Jeansimg_00000050.jpg
│   └── Cropped_Trench_Coatimg_00000004.jpg
├── src
│   ├── colordescriptor.py
│   └── searcher.py
├── README.md
├── index.py
├── index1.csv
├── name_change.py
└── search.py
```

As we see from the project structure :

a) all the class related to Histogram descriptor and Searcher are kept in **src** folder. 

b)The test images are kept in **queries** folder. 

c) All the csv file which contains the features are found in **index1.csv**

d) The features extraction script is in **index.py** file

<a name="data"></a>
## Dataset

The dataset for this challenge was given to us which can be downloaded from the  **[dataset](https://drive.google.com/open?id=1_Qww0NbYJOH17IiTr7bgXWQTQTFD-V9R)** and kept in **data_similarity** file

The dataset contains 3050 images in total.Since it doesnot require any deep learning based module training , thus there was no need to divide the dataset into training and testing sets.

<a name="project"></a>
## Project Execution Steps 

**Step 1. Clone the entire project**

* The entire project needs to be cloned into your machine. Once it is cloned we go to that project structure and type in terminal as:

```
export PYTHONPATH=.
```
* We need to install the dependencies required for this project. The dependencies are given in **requirements.txt** file 


**Step 2: Defining our Image Descriptor**

We need to define our image descriptor which will find out the image features and save it in corresponding csv file for all the images in the **data_similarity** directory

Our image descriptor will be a 3D color histogram in the HSV color space (Hue, Saturation, Value).

For our apparel photo image search engine, we’ll be utilizing a 3D color histogram in the HSV color space with 8 bins for the Hue channel, 12 bins for the saturation channel, and 3 bins for the value channel, yielding a total feature vector of dimension 8 x 12 x 3 = 288.

This means that for every image in our dataset, no matter if the image is 36 x 36 pixels or 2000 x 1800 pixels, all images will be abstractly represented and quantified using only a list of 288 floating point numbers.

Our color histogram is normalized on Line 61 or 65 (depending on OpenCV version) to obtain scale invariance. This means that if we computed a color histogram for two identical images, except that one was 50% larger than the other, our color histograms would be (nearly) identical.

**Step 3: Extracting Features from Our Dataset**

Now that we have our image descriptor defined, we can move on to Step 2, and extract  features (i.e. color histograms) from each image in our dataset. 

The script to extract the features from our image  dataset is as follows:

```
python index.py --dataset dataset --index index1.csv
```

This will save a index1.csv file containing all the image histogram features of all the images.

**Step 4: Performing a Search**

 Now that we’ve extracted features from our dataset, we need a method to compare these features for similarity. That’s where we have create a class that will define the actual similarity metric between two images. This is the **searcher.py** file which contains the class of searching method which uses chi-square similarity.
 
 Finally we have created a **search.py** file which will search all the related similar images from **data_similarity** folder and returns out with the 3 most similar products.
 
 The scripts to run the search is as follows:
 
 ```
 python search.py --index index1.csv --query queries/Classic_Mid-Rise_Skinny_Jeansimg_00000050.jpg --result-path data_similarity

 ```
 

* As we can see the images for testing are kept in queries folder. To test it for varying images , you can change the image name accordingly in the terminal. In case you want to test it for your test image, copy the image inside examples folder and then run the scipt changing the image name 

<a name="similar"></a>
## Result Similar Images

Some of the results after running the script is as follows:

Output 1 
========
```
python search.py --index index1.csv --query queries/Classic_Mid-Rise_Skinny_Jeansimg_00000050.jpg --result-path data_similarity
```

The output is as follows:

<div style="text-align: center"><img src="images/Similar_images2.jpg" width="700"/></div>

* As we can see the first image is the query image , while the rest 3 images are the most similar ones that could be found in the **data_similarity** folder.

Output 2
========

```
python search.py --index index1.csv --query queries/Cropped_Trench_Coatimg_00000004.jpg --result-path data_similarity
```
The output is as follows:


<div style="text-align: center"><img src="images/Similar_images1.jpg" width="700"/></div>

* As we can see the first image is the query image , while the rest 3 images are the most similar ones that could be found in the **data_similarity** folder.



<a name="conclusion"></a>
## Conclusion

We have succesfully implemented a project that could find the most similar images from the given dataset. One of the major merits in trying out this project was it was able to find similar images without using any deep learning models which is usually data hungry and large. However the search time is moderate right now which will tend to increase once the dataset size increases. Thus we also have to look into alternate image searching techniques probably a deep learning module might come in handy.

<a name="future"></a>
## Future Work

-  Have to create a REST apI so that it could be deployed over the web
-  Create GUI for web based aplication.
-  Try out any deep learning based similarity approach as the current one is taking moderate time
-  Get more dataset for training and remove the duplicate images.
-  Dockerize so that it can be productionised

