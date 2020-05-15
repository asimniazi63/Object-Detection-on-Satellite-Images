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
Faster-RCNN | 0.515 | 0.508

# Performance Graphs
## Training settings


Image Size = 512

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


# Visual Results
![RetinaNet](images/1.png)
![RetinaNet](images/2.png)
![RetinaNet](images/3.png)
![RetinaNet](images/4.png)
![RetinaNet](images/5.png)
![RetinaNet](images/6.png)
