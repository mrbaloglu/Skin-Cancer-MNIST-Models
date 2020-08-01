# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:43:12 2020

@author: mrbaloglu
"""

import numpy as np
import pandas as pd
import matplotlib.image as img
import matplotlib.pyplot as plt
from PIL import Image
import os

num_ptx = 64
root_path = "D:\\Belgeler\\MATH 465 Mathematical Foundations of Data Science\\Proje\\HAM10000_images_part_1"
output_path = "D:\\Belgeler\\MATH 465 Mathematical Foundations of Data Science\\Proje\\cleaned_data\\" + str(num_ptx) + "ptx\\"

import glob
#take all file names in the directory intoa list for each class
image_file_list = glob.glob(root_path + "\\*")

images_np = []
image_names= []

#putting pictures in the HAM10000_images_part_1 into pd.dataframe
for img_file in image_file_list:
    try:
      image_names.append(img_file.split("\\")[5].split(".")[0])   
      im = Image.open(img_file)
      im = np.asarray(im.resize((num_ptx,num_ptx), Image.ANTIALIAS)) #resize all images to 64*64 as (64,64,3) numpy arrays
      #print(img_file.split("\\")[5])
      #df.append(pd.DataFrame(arr).T)
      #data = {"pixels": im.reshape(im.shape[0], -1), "image_id": img_file.split("\\")[5].split(".")[0]}
      #images_pd = images_pd.append(data, ignore_index = True)
      images_np.append(im)
    except:
        IOError

root_path = "D:\\Belgeler\\MATH 465 Mathematical Foundations of Data Science\\Proje\\HAM10000_images_part_2"
image_file_list2 = glob.glob(root_path + "\\*")
#putting pictures in the HAM10000_images_part_2 into pd.dataframe
for img_file in image_file_list2:
    try:
      image_names.append(img_file.split("\\")[5].split(".")[0])  
      im = Image.open(img_file)
      im = np.asarray(im.resize((num_ptx,num_ptx), Image.ANTIALIAS)) #resize all images to 64*64 as (64,64,3) numpy arrays
      #print(img_file.split("\\")[5])
      #data = {"pixels": im.reshape(im.shape[0], -1), "id": img_file.split("\\")[5].split(".")[0]}
      #images_pd = images_pd.append(data, ignore_index = True)
      images_np.append(im)
    except:
        IOError
        
images_np_2 = np.asarray(images_np)  
image_pd = pd.DataFrame(images_np_2.reshape(images_np_2.shape[0], -1))
image_names = np.asarray(image_names)

image_pd["image_id"] = image_names

metadata = pd.read_csv("HAM10000_metadata.csv")

data_labeled = image_pd.merge(metadata, how = "left")
data_labeled.to_csv(output_path + str(num_ptx) + "ptx_data_n")



