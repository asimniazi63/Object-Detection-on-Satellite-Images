import shutil
import os
#copy files based on {datasets in txt}

def copy(filepath,dest_dir):
    with open(filepath) as fp:
        for line in fp:
            os.makedirs(dest_dir, exist_ok=True)  # succeeds even if directory exists.
            shutil.copy(line.replace('\n', ''), dest_dir) #image
            shutil.copy(line.replace('.jpg\n', '.xml'), dest_dir) ##label