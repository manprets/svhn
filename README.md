## svhn
-   google street view house number

##Machine Learning Capstone Project: 
-   Deep Learning: Detect Housing Numbers from google street view image dataset

##Files in the project:
-   explore_data.ipynb: explore, preprocess dataset and create pickle files to train and test the deep learning model
-   build_my_model_color.ipynb: build architecture for training the convolutional network

##Install
Following installations are required for this project:
-   Python 2.7
-   Jupyter Notebook

This project requires following Python libraries:
-   numpy
-   pandas
-   matplotlib
-   scikit-learn
-   scipy
-   tensorflow
-   six

##Data
This project uses data avaibale at http://ufldl.stanford.edu/housenumbers/

SVHN dataset consists of over 600k labeled digit images of house numbers taken from Google Street View imaging dataset. The sequence of numbers in the images are of bounded length.

##Run
-   Step.1) Download 3 datasets from http://ufldl.stanford.edu/housenumbers/ related to SVHN dataset
-   Step.2) Download project files from https://github.com/prijip/Py-Gsvhn-DigitStruct-Reader
-   Step.3) Run ```jupyter notebook explore_data.ipynb``` command to create 3 pickle files containing test, train and extra datasets and labels
-   Step.4) Run ```jupyter notebook build_my_model_color.ipynb``` command to train and report accuracy of the convolutional netowrk

##Links:
http://ufldl.stanford.edu/housenumbers/


