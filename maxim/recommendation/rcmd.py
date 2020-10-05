# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


# In[ ]:


def filtering(level): # filter class data based on level which students response
    db=pd.read_csv('/Users/surin/Documents/201720723/3-1/도메인분석및SW설계/Final/rcmd/finalAcademy.csv', engine='python') # load database
    filtered=db[db.level==level] # filter class data
    data=filtered.values.tolist() # change dataframe to list
    return data


# In[ ]:


def getRecommendation(data, preference):
    
    pref=[preference] # pref is the list based on students preference
    std=pd.DataFrame(pref,columns=['class_size','tuition','careerOfTeacher','ageDistribution']) # make a dataframe of pref
    data=pd.DataFrame(filtering(1),columns=['NO.','Academy','class_name','class_ID','subject','level','class_hour_day','class_hour_time','like','student_list','syllabus_ID','class_size','tuition','careerOfTeacher','ageDistribution'])
    # make a dataframe which was filtered by student's response(level) from original database
    df=data[["class_ID","class_size","tuition","careerOfTeacher","ageDistribution"]]
    DF=df[["class_size","tuition","careerOfTeacher","ageDistribution"]]
    clsID=df[["class_ID"]]
    Merge_Data=DF.append(std)
    
    data_points = Merge_Data.values
    kmeans=KMeans(n_clusters=4) # make 4 clusters
    scaler = MinMaxScaler() 
    X_scaled = scaler.fit_transform(data_points) #scale all columns data
    kmeans.fit(X_scaled) # fit with kmeans clustering algorithm
    Merge_Data['cluster_id'] = kmeans.labels_ # add a column which means cluster_id
    std_clusterid=Merge_Data[Merge_Data.shape[0]-1:Merge_Data.shape[0]].cluster_id.values # cluster_id of student's data
    RC=Merge_Data.iloc[0:Merge_Data.shape[0]-1]
    FINAL=pd.concat([RC,clsID],axis=1)
    Filter_cluster=FINAL[FINAL.cluster_id==std_clusterid[0]] # choose class list whose cluster_id is same as student's
    output=Filter_cluster["class_ID"] # return class_id of chosen
    class_list=output.tolist() # return class id to list
    return class_list