# Tutorials using keras for Machine learning
Here I will add notebooks about how to use keras for training private datasets. This means, wild data that you own or are not a built-in function of other python library.

For the moment I have the following tutorials:  
## <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/Keras%20-%20StarCraft%20unit%20prediction%20from%20disk%20-%20FC.ipynb" target="_blank">keras - StarCraft unit prediction from disk - FC.ipynb. </a>
### Added on 20180418.
Here you can see:
* How to train a keras model using Fully Connected (FC) Layers. FC are also called multilayer perpectrons.
* How to train images from disk (HDD) by batch. In order words, only load them into memory when training in a given batch.
* How to train using manual features, in this case a histogram of all the channels of an image.

## <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/Keras%20-%20StarCraft%20Unit%20Classification%20from%20disk.ipynb" target="_blank"> Keras - StarCraft Unit Classification from disk.ipynb. </a>
### Added on 20180419.
Here you can see:  
* how to train an image classification model using Convolutional Neural Networks (CNN).  
* how to train using images inside a zip file, by batch. In order words, only load them into memory when training in a given batch, without unziping all the content of the zip file.
* how to save and restore a keras model.  

## <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/VGG_Data_extraction.ipynb" target="_blank" > VGG annotator: Extract data from json export for image localization </a>
### Added on 20180428.  
Here you can see:  
* How to annotate the position of an object in a group of images for a further object localization process.
* How to use the VGG annotator tool for this purpose.
* How to export the metadata that holds the position of the objects as a JSON file.
* How to extract the data from the JSON file into a usable format, a pandas DataFrame.  
You can see the process here: https://youtu.be/MRkdgOoUqFk 

## <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/tfjs.html" target="_blank"> Use your keras model in javascript for image classification</a>  
### Added on 20180428
This is an example of a html file alone that shows how to use a keras model, transformed using the tensorflow.js tool, for prediction of a Star craft 2 unit. Here you can see:
* How to load the tensorflow.js
* How to load your model (model.js)
* How to upload an image and change its format so you can feed it into the keras trained model.  
  
**Important**: In order to make it work you need to place the model into a web server, just your browser is not enough.  


## <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/get_yolo_darknet_model.ipynb" target="_blank"> See the output of a Convolutional Neural Network layer with Keras</a>  
### Added on 20190314
In this notebook you will see how to get the output of a CNN keras model. As an example I picked up the Yolov3 model architecture and showed the last layers output as an image.

# <a href="https://github.com/bsaldivaremc2/keras_tutorials/blob/master/python_base64_encode_decode.ipynb" target="_blank"> **base64 encoding and decoding**</a>  
### Added on 20190815  
This small tutorial shows how to use base64 to store an image as a string inside a json string and then recover it for saving or processing with numpy.  
  
