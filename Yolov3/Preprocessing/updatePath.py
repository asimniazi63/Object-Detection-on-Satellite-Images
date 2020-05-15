#update paths of train,test,val

### replace ./images/0000.jpg to "/content/yolov3/Dataset/yolo_train/images/0000.jpg" 

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