# RetinaNet Object Detection on Satellite Images

# Pre-requistes
 - Colab
 - Keras and Tensorflow
 - Clone into https://github.com/fizyr/keras-retinanet.git
 - Install requirements by `pip install .` and Build cython code `python setup.py build_ext --inplace`
 
# Preprocessing
In first step, separate images into train,valid and test directories. The dataset was provided in <b>Pascal voc </b> but was converted to custom format
of `filepath,x1,y1,x2,y2,class_name`. Training requires annotation files in `.CSV` format. For step by step preprocessing please refer to 
`Preprocessing/RetinaNet_preprocessing.ipynb` <br />

Example dataset provided in `Dataset` folder

Create `classes.csv` in format:
```
class_name,id
car,0
bus,1
...
```

# Network Summary
## RetinaNet (ResNet50 backnone)
![Faster RCNN](Summary/model_plot_retinaNet_resnet50.png)
## RetinaNet (EfficientNetB7 backnone)
![Faster RCNN](Summary/RetinaNet_model_plot_effNetB7_backbone.png)

# Debug Annotations
Check validity of annotations by running following commands:

```
!python3 keras_retinanet/bin/debug.py csv labels_train.csv sims_classes.csv  

```

# Training
Form more details please refer to '*.ipynb` availble in current directory. <br />
For training on custom dataset, a CSV file can be used to pass data. To train using CSV run:
```
!python3 keras_retinanet/bin/train.py --batch-size 4 --epochs 50 --steps 1000 --tensorboard-dir '/content/drive/My Drive/SIMS_Dataset/baseline/runs/' 
--snapshot-path '/content/drive/My Drive/SIMS_Dataset/baseline/snapshot' --no-resize --weighted-average --compute-val-loss 
csv labels_train.csv sims_classes.csv --val-annotations labels_valid.csv
```

# Testing
Convert Trained model to inference model by this command:
```
!python3 keras_retinanet/bin/convert_model.py '/content/drive/My Drive/SIMS_Dataset/baseline/snapshot/resnet50_csv_20.h5' snapshots-inference/retinaNet_resnet50.h5
```
Form more details please refer to '*.ipynb` availble in current directory. <br />
Run:
```
python3 keras_retinanet/bin/evaluate.py --save-path test_output csv labels_test.csv sims_classes.csv 'snapshots-inference/retinaNet_resnet50.h5'
```

# Performance Measures
Model | Validation mAP | Test mAP
------------ | ------------- | -------------
RetinaNet (ResNet50) | 0.8442 | 0.6231
RetinaNet (EfficientNetB7) | 0.6126 | [evaluation script error-see this issue](https://github.com/fizyr/keras-retinanet/issues/647)

# Performance Graphs

## Graphs for baseline (ResNet50)
## Training settings

Image Size = 1024x768

Batch_size = 4

iterations_per_epoch = 1000

LR = 1e-5

![RetinaNet](Graphs/baseline/1.PNG)
![RetinaNet](Graphs/baseline/2.PNG)
![RetinaNet](Graphs/baseline/3.PNG)
![RetinaNet](Graphs/baseline/4.PNG)

## Graphs for improvement with EfficientNetB7 as Backbone
## Training settings

Image Size = 512

Batch_size = 1

iterations_per_epoch = 3000

LR = 1e-5

![RetinaNet](Graphs/EfficientNet(backbone)/1.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/2.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/3.PNG)
![RetinaNet](Graphs/EfficientNet(backbone)/4.PNG)



# Per Class Evaluation results
## Validation set (ResNet50)
```
Running network: 100% (1740 of 1740) |####| Elapsed Time: 0:02:51 Time:  0:02:51
Parsing annotations: 100% (1740 of 1740) || Elapsed Time: 0:00:00 Time:  0:00:00
11462 instances of class car with average precision: 0.8828
864 instances of class truck with average precision: 0.6061
2198 instances of class van with average precision: 0.7179
381 instances of class longvehicle with average precision: 0.5732
631 instances of class bus with average precision: 0.7181
212 instances of class airliner with average precision: 0.9720
41 instances of class propeller with average precision: 0.5170
141 instances of class trainer with average precision: 0.9471
155 instances of class chartered with average precision: 0.8477
8 instances of class fighter with average precision: 0.7901
190 instances of class other with average precision: 0.1471
126 instances of class stairtruck with average precision: 0.2763
68 instances of class pushbacktruck with average precision: 0.1446
16 instances of class helicopter with average precision: 0.1049
4707 instances of class boat with average precision: 0.9416
mAP: 0.8442
```
## Test set (ResNet50)
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
