# Matches xml image numbers to images and moves the matched images to the matched_xml folder

import os
import shutil


path = 'C:/ProgramData/Anaconda3/Lib/site-packages/tensorflow/models/workspace/vessel_detection/annotations/xmls/'

# get all the xml file names
xml_files = os.listdir(path)
xml_names = [os.path.splitext(x)[0] for x in xml_files]

# Copy images with matching names into new folder
img_names = [x + '.jpg' for x in xml_names]

[shutil.copyfile('C:/ProgramData/Anaconda3/Lib/site-packages/tensorflow/models/workspace/vessel_detection/images/raw/' + x, 
  'C:/ProgramData/Anaconda3/Lib/site-packages/tensorflow/models/workspace/vessel_detection/images/matched/' + x) for x in img_names]