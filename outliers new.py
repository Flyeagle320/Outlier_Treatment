# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 10:43:16 2022

@author: Rakesh
"""
#importing pandas package for data manipulation#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #visualization#
import seaborn as sns #advanced visualization#
#lets import data ##
boston= pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/boston_data.csv')
print(boston)

#let see for any NA or null value ##
boston.info() ##no null or na value##

#to mean , min , max , IQR 
boston.describe()
##EDA / Descriptive analysis##

EDA =pd.DataFrame({"coloumn name":[boston.columns],
                   "means":[boston.mean()],
                   "median":[boston.median()],
                   "mode":[boston.mode()],
                   "standard deviation":[boston.std()],
                   "variance":[boston.var()],
                   "skewness":[boston.skew()],
                   "kurtosis":[boston.kurt()]})
EDA
##Scatter plot btw variable using histogram##
sns.pairplot(boston.iloc[:, :])

#finding outliers in data using boxplot##

for column in boston:
    plt.figure()
    boston.boxplot([column])
    
boxplot =boston.boxplot(column=['crim','zn','indus','chas','nox', 'rm','age','dis','rad','tax','ptratio',
                                 'black','lstat','medv'])
#outlier are there in crim,zn ,rm,black , dis,lstat, medv##

## for columns crim##
# Detection of outliers (find limits for crim based on IQR)##
crim_IQR = boston['crim'].quantile(0.75)-boston['crim'].quantile(0.25)
crim_upper_limit= boston['crim'].quantile(0.75)+(crim_IQR*1.5)
####################Let us Replace by maximum and minimum limit######
boston['crim_replaced']=pd.DataFrame(np.where(boston['crim']>crim_upper_limit,crim_upper_limit,boston['crim']))
                                       
sns.boxplot(boston.crim_replaced);plt.title('Boxplot'),plt.show()

## for columns zn ##        
zn_IQR = boston['zn'].quantile(0.75)-boston['zn'].quantile(0.25)
zn_upper_limit = boston['zn'].quantile(0.75)+(zn_IQR*1.5)
##################Replace by using same method as crim##
boston['zn_replaced']=pd.DataFrame(np.where(boston['zn']>zn_upper_limit,zn_upper_limit,boston['zn']))
sns.boxplot(boston.zn_replaced);plt.title('Boxplot'),plt.show()
## for columns rm ## 
rm_IQR = boston['rm'].quantile(0.75)-boston['rm'].quantile(0.25)
rm_upper_limit= boston['rm'].quantile(0.75)+(rm_IQR*1.5)
rm_lower_limit = boston['rm'].quantile(0.25)-(rm_IQR*1.5)

###Replace using Min and max limit##
boston['rm_replaced']= pd.DataFrame(np.where(boston['rm']>rm_upper_limit,rm_upper_limit,
                                             np.where(boston['rm']<rm_lower_limit,rm_lower_limit,boston['rm'])))
sns.boxplot(boston.rm_replaced);plt.title('Boxplot'),plt.show()

## for Columns dis ###
dis_IQR = boston['dis'].quantile(0.75)-boston['dis'].quantile(0.25)
dis_upper_limit = boston['dis'].quantile(0.75)+(dis_IQR*1.5)
###Replace using Min and max limit##
boston['dis_replaced']= pd.DataFrame(np.where(boston['dis']>dis_upper_limit,dis_upper_limit,boston['dis']))
sns.boxplot(boston.dis_replaced);plt.title('Boxplot'),plt.show()

##for columns black ###
black_IQR = boston['black'].quantile(0.75)-boston['black'].quantile(0.25)
black_lower_limit = boston['black'].quantile(0.25)-(black_IQR*1.5)
###Replace using Min and max limit ##
boston['black_replaced']= pd.DataFrame(np.where(boston['black']<black_lower_limit,black_lower_limit,boston['black']))
sns.boxplot(boston.black_replaced);plt.title('Boxplot'),plt.show()

#####for columns lstat#####
lstat_IQR = boston['lstat'].quantile(0.75)-boston['lstat'].quantile(0.25)
lstat_upper_limit = boston['lstat'].quantile(0.75)+(lstat_IQR*1.5)
###Replaced using max & min limit##
boston['lstat_replaced']=pd.DataFrame(np.where(boston['lstat']>lstat_upper_limit,lstat_upper_limit,boston['lstat']))
sns.boxplot(boston.lstat_replaced);plt.title('Boxplot'),plt.show()

#######for columns medv #########
medv_IQR= boston['medv'].quantile(0.75)-boston['medv'].quantile(0.25)
medv_upper_limit=boston['medv'].quantile(0.75)+(medv_IQR*1.5)
medv_lower_limit=boston['medv'].quantile(0.25)-(medv_IQR*1.5)
####Replaced using max & min limit###
boston['medv_replaced']=pd.DataFrame(np.where(boston['medv']>medv_upper_limit,medv_upper_limit,
                                              np.where(boston['medv']<medv_lower_limit,medv_lower_limit,boston['medv'])))
sns.boxplot(boston.medv_replaced);plt.title('Boxplot');plt.show()
###for columns ptratio###
ptratio_IQR = boston['ptratio'].quantile(0.75)-boston['ptratio'].quantile(0.25)
ptratio_lower_limit = boston['ptratio'].quantile(0.25)-(ptratio_IQR*1.5)

####Replaced using max & min limit###
boston['ptratio_replaced']=pd.DataFrame(np.where(boston['ptratio']<ptratio_lower_limit,ptratio_lower_limit,boston['ptratio']))
sns.boxplot(boston.ptratio_replaced);plt.title('Boxplot');plt.show()






    
