# Convert and rename images from the raw image folder

from PIL import Image
import os

path = 'C:/ProgramData/Anaconda3/Lib/site-packages/tensorflow/models/workspace/husky_demo/images/raw/'

# get all the image file names
files = os.listdir(path)
print(files)

counter = 1
for i in range(len(files)):
    im = Image.open(path + files[i])
    im.save(path + str(counter) + '.jpg')
    os.remove(path + files[i])
    counter = counter + 1