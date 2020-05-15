# Yolov3 Object Detection on Satellite Images

# Pre-requistes
 - Colab
 - Pytorch >=1.5
 - Clone into repository `https://github.com/ultralytics/yolov3`
 - install `pip install -U -r requirements.txt`
 
 
# Preprocessing
Created train, test and valid folder with correspondence to the training,test and valid`.txt` files.
```
#separate images based on train,val and test and put corresponding files into 
#respective folder having images and labels as subfolders in it
def copy(filepath,dest_dir):
    with open(filepath) as fp:
        for line in fp:
            os.makedirs(dest_dir, exist_ok=True)  # succeeds even if directory exists.
            shutil.copy(line.replace('\n', ''), dest_dir+"images") #image
            shutil.copy(line.replace('.jpg\n', '.txt'), dest_dir+"labels") ##label
    print("Done: "+ filepath)
            
copy('./training.txt','yolo_train/')
copy('./validation.txt','yolo_val/')
copy('./test.txt','yolo_test/')
```

The images and annotations/labels should look like this:
```
Dataset/yolo_test/images/0000.jpg #image
Dataset/yolo_test/label/0000.txt #label
```
Note: Each image's label should be locatable by replacing `/image/*.jpg` with `/label/*.txt`

then created `.txt` for annotations with following code:

```
def copy(filepath,newfile,binder):
    with open(filepath) as fp:
      print(filepath)
      for line in fp:
        in_file = line[2:]
        new = binder+in_file
        with open(newfile, "a") as f:
          f.write(new)

copy('training.txt','Dataset/yolo_train/yolo_train.txt',
     "/content/yolov3/Dataset/yolo_train/")

copy('test.txt','Dataset/yolo_test/yolo_test.txt',
     "/content/yolov3/Dataset/yolo_test/")

copy('validation.txt','Dataset/yolo_val/yolo_val.txt',
     "/content/yolov3/Dataset/yolo_val/")
```

Create `classes.names` file, Here we are using `Dataset/sims_classes.names`
```
car
bus
truck
van
longvehicle
...
```

Create `sims.txt` for passing data for training. It should look like this:
```
classes=15
train=/content/yolov3/Dataset/yolo_train/yolo_train.txt
valid=/content/yolov3/Dataset/yolo_val/yolo_val.txt
names=/content/yolov3/Dataset/sims_classes.names
```
For testing, create `sims_test.txt` and it should look like this:
```
classes=15
valid=/content/yolov3/Dataset/yolo_test/yolo_test.txt
names=/content/yolov3/Dataset/sims_classes.names
```

Update `*.cfg` in all yolov3 layers. Filters in these layers should be `filters=[5 + n] * 3` where n = number of classes




Example dataset provided in `Dataset` folder

# Network Summary
## Yolov3

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
