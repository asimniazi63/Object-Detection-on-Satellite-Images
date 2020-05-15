# Faster RCNN for Object Detection on Satellite Images

# Pre-requistes
 - Colab
 - Keras
 - Tensorflow
 - Pandas
 
# Preprocessing
In first step, separate images into train,valid and test directories. The dataset was provided in <b>Pascal voc </b> but was converted to custom format
of `filepath,x1,y1,x2,y2,class_name`. Training requires annotation files in `.txt` format. For step by step preprocessing please refer to 
`Preprocessing/FRCNN_preprocessing.ipynb` <br />

Example dataset provided in `Dataset` folder

# Network Summary
## Faster RCNN
![Faster RCNN](Summary/model_frcnn_vgg.png)

# Training
Refer to `frcnn_train_vgg.ipynb`

# Testing
Refer to `frcnn_test_vgg.ipynb`. <br />
Note: training config is used for test the Model.

# Performance Measures
Model | Validation mAP | Test mAP
------------ | ------------- | -------------
Faster-RCNN | 0.515 | 0.508

# Performance Graphs
![Faster-RCNN](Graphs/1.png)
![Faster-RCNN](Graphs/2.png)
![Faster-RCNN](Graphs/3.png)

# Visual Results
![Faster-RCNN](Outputs/1.png)
![Faster-RCNN](Outputs/2.png)
![Faster-RCNN](Outputs/3.png)
