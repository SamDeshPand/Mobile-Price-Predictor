import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Mobile price predictor")
st.divider()
st.header("Battery 🔋")
batt=st.slider(" ",500,2000)
st.divider()
st.header("Blutooth 📶")
blu=st.radio(" ",('Yes','No'))
if blu=='Yes':
    blu=1
else:
    blu=0
st.divider()
st.header("Clock Speed(in GHz) ⏰")
csp=st.slider(" ",0.5,3.0)
st.divider()
st.header("Dual Sim 📶")
dsim=st.radio("  ",('Yes','No'))
if dsim=='Yes':
    dsim=1
else:
    dsim=0
st.divider()
st.header("Front Camera Megapixels 📸")
fc=st.slider(" ",0,19)
st.divider()
st.header("4G 📶")
sim4g=st.radio("   ",('Yes','No'))
if sim4g=='Yes':
    sim4g=1
else:
    sim4g=0
st.divider()
st.header("Internal memory in GB")
intmem=st.slider(" ",2,64)
st.divider()
st.header("Mobile depth in cms")
mobdepth=st.slider(" ",0.1,1.0)
st.divider()
st.header("Weight of mobile phone")
mobwt=st.slider(" ",80,200)
st.divider()
st.header("Number of cores")
ncores=st.slider(" ",1,8)
st.divider()
st.header("Primary Camera mega pixels 📸")
pc=st.slider(" ",0,20)
st.divider()
st.header("Pixel Resolution Height")
px_height=st.slider(" ",0,1960)
st.divider()
st.header("Pixel Resolution Width")
px_width=st.slider(" ",500,1960)
st.divider()
st.header("Random Access Memory in Mega Bytes")
ram=st.slider(" ",256,3998)
st.divider()
st.header("Screen Height of mobile in cm 📱")
sc_h=st.slider(" ",5,19)
st.divider()
st.header("Screen Width of mobile in cm 📱")
sc_w=st.slider(" ",0,18)
st.divider()
st.header("Talk Time")
talk_time=st.slider(" ",2,20)
st.divider()
st.header("3G 📶")
sim3g=st.radio("    ",('Yes','No'))
if sim3g=='Yes':
    sim3g=1
else:
    sim3g=0
st.divider()
st.header("Touch Screen 📱")
touch=st.radio("     ",('Yes','No'))
if touch=='Yes':
    touch=1
else:
    touch=0
st.divider()
st.header("Wifi ᯤ")
wifi=st.radio("      ",('Yes','No'))
if wifi=='Yes':
    wifi=1
else:
    wifi=0
st.divider()


list=[batt,blu,csp,dsim,fc,sim4g,intmem,mobdepth,mobwt,ncores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,sim3g,touch,wifi]

df=pd.read_csv('train (1).csv')
x=df.drop(columns=['price_range'])
y=df['price_range']
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=1)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
model1=knn.fit(xtrain,ytrain)

arr=np.array(list)
newarr=arr.reshape(1,-1)
ans=model1.predict(newarr)

if st.button('PREDICT'):
    if ans==[0]:
        st.header("The price of phone lies between 5000-15000")
    elif ans==[1]:
        st.header("The price of phone lies between 15000-25000")
    elif ans==[2]:
        st.header("The price of phone lies between 25000-35000")
    elif ans==[3]:
        st.header("The price of phone is greater than 35000")
