# Yolov3 Object Detection on Satellite Images

# Pre-requistes
 - Colab
 - Keras and Tensorflow
 - Clone into https://github.com/fizyr/keras-Yolov3.git
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
## Yolov3 (ResNet50 backnone)
![Faster RCNN](Summary/model_plot_retinaNet_resnet50.png)
## Yolov3 (EfficientNetB7 backnone)
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
Yolov3 (ResNet50) | 0.8442 | 0.6231
Yolov3 (EfficientNetB7) | 0.6126 | [evaluation script error-see this issue](https://github.com/fizyr/keras-Yolov3/issues/647)

# Performance Graphs

## Graphs for baseline (ResNet50)
## Training settings

Image Size = 1024x768

Batch_size = 4

iterations_per_epoch = 1000

LR = 1e-5

![Yolov3](Graphs/baseline/1.PNG)
![Yolov3](Graphs/baseline/2.PNG)
![Yolov3](Graphs/baseline/3.PNG)
![Yolov3](Graphs/baseline/4.PNG)

## Graphs for improvement with EfficientNetB7 as Backbone
## Training settings

Image Size = 512

Batch_size = 1

iterations_per_epoch = 3000

LR = 1e-5

![Yolov3](Graphs/EfficientNet(backbone)/1.PNG)
![Yolov3](Graphs/EfficientNet(backbone)/2.PNG)
![Yolov3](Graphs/EfficientNet(backbone)/3.PNG)
![Yolov3](Graphs/EfficientNet(backbone)/4.PNG)



# Per Class Evaluation results
## Validation set (ResNet50)
```

```
## Test set (ResNet50)
```

```


# Visual Results
![Yolov3](images/1.png)
![Yolov3](images/2.png)
![Yolov3](images/3.png)
![Yolov3](images/4.png)
![Yolov3](images/5.png)
![Yolov3](images/6.png)
