import os, sys, shutil, random
import pandas as pd
import numpy as np
import cv2
import PIL.Image as Image
import matplotlib.pyplot as plt

clist = {"name":[], "color":[]}

for i in range(10000):
    
    c = random.choice(["red", "green", "blue", "yellow", "orange", "pink", "black", "white", "gray", "purple"])
    
    clist["name"].append(i)
    clist["color"].append(c)    
    
    Image.new("RGB", (10, 10), color=c).save(f"./data/{i}.png")

pd.DataFrame(clist).to_csv("./ogclass.csv")