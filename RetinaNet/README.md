# RetinaNet Object Detection on Satellite Images

# Pre-requistes
 - Colab
 - Keras and Tensorflow
 - Clone into https://github.com/fizyr/keras-retinanet.git
 - Install requirements by `pip install .` and Build cython code `python setup.py build_ext --inplace`
 
# Preprocessing
In first step, separate images into train,valid and test directories. The dataset was provided in <b>Pascal voc </b> but was converted to custom format
of `filepath,x1,y1,x2,y2,class_name`. Training requires annotation files in `.csv` format. For step by step preprocessing please refer to 
`Preprocessing/RetinaNet_preprocessing.ipynb` <br />

Example dataset provided in `Dataset` folder

# Network Summary
## RetinaNet (ResNet50 backnone)
![Faster RCNN](Summary/model_plot_retinaNet_resnet50.png)
## RetinaNet (EfficientNetB7 backnone)
![Faster RCNN](Summary/RetinaNet_model_plot_effNetB7_backbone.png)

# Training


# Testing
Refer to `frcnn_test_vgg.ipynb`. <br />
Note: training config is used for testing the Model.

# Performance Measures
Model | Validation mAP | Test mAP
------------ | ------------- | -------------
RetinaNet (ResNet50) | 0.8442 | 0.6231
RetinaNet (EfficientNetB7) | 0.6126 | [evaluation script error-see this issue](https://github.com/fizyr/keras-retinanet/issues/647)

# Performance Graphs
## Training settings


Image Size = 1024x768

Batch_size = 4

iterations_per_epoch = 1000


## Graphs for baseline (ResNet50)
![RetinaNet](Graphs/baseline/1.PNG)
![RetinaNet](Graphs/baseline/2.PNG)
![RetinaNet](Graphs/baseline/3.PNG)
![RetinaNet](Graphs/baseline/4.PNG)

## Graphs for improvement with EfficientNetB7 as Backbone
![RetinaNet](Graphs/EfficientNet(backbone)/1.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/2.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/3.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/4.PNG)


# Per Class Evualtion results on test dataset
```
3678 instances of class car with average precision: 0.8669
446 instances of class truck with average precision: 0.6585
874 instances of class van with average precision: 0.7033
222 instances of class longvehicle with average precision: 0.5817
366 instances of class bus with average precision: 0.7277
161 instances of class airliner with average precision: 0.9638
25 instances of class propeller with average precision: 0.6700
49 instances of class trainer with average precision: 0.8611
103 instances of class chartered with average precision: 0.8428
8 instances of class fighter with average precision: 0.8409
85 instances of class other with average precision: 0.1591
83 instances of class stairtruck with average precision: 0.2610
55 instances of class pushbacktruck with average precision: 0.1585
9 instances of class helicopter with average precision: 0.1115
1820 instances of class boat with average precision: 0.9398
Inference time for 747 images: 0.0855
mAP using the weighted average of precisions among classes: 0.8211
mAP: 0.6231
```


# Visual Results
![RetinaNet](images/1.png)
![RetinaNet](images/2.png)
![RetinaNet](images/3.png)
![RetinaNet](images/4.png)
![RetinaNet](images/5.png)
![RetinaNet](images/6.png)
