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
Summary availble here in txt file [link](Summary/Yolov3-keras-style.txt)
## Yolov3 Spatial Pyramid Pooling
Summary availble here in txt file [link](Summary/Yolov3-spp-keras-style.txt)



# Training
Form more details please refer to `Yolov3_baseline.ipynb` or 'Yolov3_SPP_improved.ipynb` availble in current directory. <br />
For training on custom dataset, earlier created `data.txt` will be passed with following command:

```
#start training
!python3 train.py --batch 8 --epochs 60 --img-size 512 --data Dataset/sims.txt --cache-images --rec --cfg yolov3.cfg --name from_yolov3 --weights weights/yolov3.pt
```

# Testing
Run command:

```
python3 test.py --data Dataset/sims_test.txt --cfg yolov3.cfg --batch-size 8 --weights weights/last_from_yolov3.pt --save-json --img-size 512
```

For detections run:
```
python3 detect.py --names Dataset/sims_classes.names --cfg yolov3.cfg --weights weights/best_from_yolov3.pt
```

# Performance Measures
Model | Validation mAP | Test mAP
------------ | ------------- | -------------
Yolov3 | 0.608 | 0.634
Yolov3-SPP | 0.653 | 0.679


# Performance Graphs

## Graphs for baseline (Yolov3)
## Training settings

Image Size = 512

Batch_size = 8

iterations_per_epoch = 1000

LR = 0.01 , final = 0.0005

LR Scheduler = cosine scheduler

config file = `cfg/Yolov3.cfg`

![Yolov3](Graphs/_results_yolov3.png)

## Graphs for improvement with SPP
## Training settings

Image Size = 512

Batch_size = 8

iterations_per_epoch = 1000

LR = 0.01 , final = 0.0005

LR Scheduler = cosine scheduler

config file = `cfg/Yolov3-spp.cfg`

![Yolov3-spp](Graphs/results_yolov3-spp.png)



# Per Class Evaluation results
## Test set - Yolov3
```
 Class    Images   Targets         P         R   mAP@0.5        F1: 100% 94/94 [00:25<00:00,  3.76it/s]
                 all       748  7.98e+03     0.549     0.697     0.634     0.581
                 car       748  3.68e+03     0.768     0.836     0.834     0.801
               truck       748       446     0.497      0.78     0.674     0.607
                 van       748       874     0.499     0.747     0.626     0.598
         longvehicle       748       222     0.395     0.856       0.6     0.541
                 bus       748       366     0.733     0.847     0.823     0.786
            airliner       748       161     0.696     0.981     0.962     0.815
           propeller       748        25     0.254      0.92     0.689     0.398
             trainer       748        49     0.533     0.863     0.782     0.659
           chartered       748       103     0.677     0.854     0.838     0.755
             fighter       748         8      0.53     0.625     0.657     0.574
               other       748        85    0.0956     0.259    0.0944      0.14
          stairtruck       748        83     0.395      0.47     0.328     0.429
       pushbacktruck       748        55     0.255     0.145      0.13     0.185
          helicopter       748         9         1     0.352      0.54      0.52
                boat       748  1.82e+03     0.898     0.918     0.936     0.908
Speed: 19.6/2.7/22.3 ms inference/NMS/total per 512x512 image at batch-size 8
```
## Test set (Yolov3-SPP)
```
  Class    Images   Targets         P         R   mAP@0.5        F1: 100% 94/94 [00:17<00:00,  5.24it/s]
                 all       748  7.98e+03     0.586     0.712     0.679     0.636
                 car       748  3.68e+03     0.785     0.856     0.859     0.819
               truck       748       446      0.57     0.767     0.727     0.654
                 van       748       874     0.643     0.778     0.743     0.704
         longvehicle       748       222     0.488     0.833     0.632     0.615
                 bus       748       366     0.757     0.883     0.864     0.815
            airliner       748       161     0.904     0.969     0.968     0.935
           propeller       748        25     0.658      0.88     0.903     0.753
             trainer       748        49     0.687      0.98     0.941     0.807
           chartered       748       103     0.635     0.963     0.927     0.765
             fighter       748         8      0.75      0.75     0.821      0.75
               other       748        85    0.0909     0.235    0.0898     0.131
          stairtruck       748        83      0.32     0.283      0.22       0.3
       pushbacktruck       748        55      0.17     0.109     0.115     0.133
          helicopter       748         9     0.437     0.432     0.421     0.434
                boat       748  1.82e+03       0.9     0.955     0.952     0.927
Speed: 9.1/2.6/11.8 ms inference/NMS/total per 512x512 image at batch-size 8
```


# Visual Results
## Results for Yolov3
![Yolov3](output/Yolov3/1.jpg)
![Yolov3](output/Yolov3/2.jpg)
![Yolov3](output/Yolov3/3.jpg)
![Yolov3](output/Yolov3/4.jpg)
![Yolov3](output/Yolov3/5.jpg)

## Results for Yolov3-SPP
![Yolov3](output/Yolov3-spp/1.jpg)
![Yolov3](output/Yolov3-spp/2.jpg)
![Yolov3](output/Yolov3-spp/3.jpg)
![Yolov3](output/Yolov3-spp/4.jpg)
![Yolov3](output/Yolov3-spp/5.jpg)
![Yolov3](output/Yolov3-spp/6.jpg)
![Yolov3](output/Yolov3-spp/7.jpg)
![Yolov3](output/Yolov3-spp/8.jpg)
![Yolov3](output/Yolov3-spp/9.jpg)