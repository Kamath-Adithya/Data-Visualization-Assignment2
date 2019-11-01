#!/usr/bin/env python
# coding: utf-8

# In[461]:


import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings('ignore')


# ### Getting the list of all the file names

# In[401]:


entries = os.listdir('Downloads/DV')
basepath = 'C:/Users/018755332SA/Downloads/DV'
count=1
Files_List =[]
temp=[]
while count<=36:
    if count !=8 and count!= 9 and count !=22 and count !=26 and count !=29:
        path=basepath+'/p'+str(count)
        for entry in os.listdir(path):
            if os.path.isfile(os.path.join(path, entry)):
                Files_List.append(entry)
    else:
        pass
    count=count+1


# ### Processing all participants Event Data and putting it together in a Data Frame

# In[468]:


folder_name =""
file_name=""
flattened_List=[]
Final_EVD=[]
#df_Event_Data = pd.DataFrame(columns=['A','B','C','D','E','F','G','H'])
Final_Combined_EVD=[]
for value in Files_List:
    if value.endswith("EVD.txt")==True:
        folder_name =value.split(".",2)[0]
        file_name= value
        df=pd.read_csv(basepath+"/"+folder_name+"/"+file_name, sep = "\t", header=None,error_bad_lines=False)
        df['Participant']=folder_name
        df['Graph/Tree']=value.split(".",2)[1]
        Final_EVD.append([df.values.tolist()])
for values in Final_EVD:
    for n in values:
        for x in n:
            flattened_List.append(x)
df_Event_Data = pd.DataFrame(flattened_List[1:],columns=['A','B','C','D','E','F','G','H'])


# In[403]:


df_Event_Data.rename(columns = {'A':'time', 
                     'B': 'event', 
                     'C': 'event_key', 
                     'D': 'data1', 
                     'E': 'data2',
                     'F':'description',
                       'G':'Participant',
                     'H':'Graph/Tree'}, inplace = True)


# In[404]:


df_Event_Data.head(5)


# ### Processing all participants Fixation Data and putting it together in a Data Frame

# In[405]:


Final_FXD=[]
Fxd_Flattened_List=[]
for value in Files_List:
    if value.endswith("FXD.txt")==True:
        folder_name =value.split(".",2)[0]
        file_name= value
        df=pd.read_csv(basepath+"/"+folder_name+"/"+file_name, sep = "\t", header=None,error_bad_lines=False)
        df['Participant']=folder_name
        df['Graph/Tree']=value.split(".",2)[1]
        Final_FXD.append([df.values.tolist()])
for values in Final_FXD:
    for n in values:
        for x in n:
            Fxd_Flattened_List.append(x)
df_Fixation_Data = pd.DataFrame(Fxd_Flattened_List[1:],columns=['A','B','C','D','E','F','G'])


# In[406]:


df_Fixation_Data.rename(columns = {'A':'number', 
                     'B': 'time', 
                     'C': 'duration', 
                     'D': 'screen_x', 
                     'E': 'screen_y',
                    'F':'Participant',
                     'Participant':'Graph/Tree'}, inplace = True)


# In[407]:


df_Fixation_Data.head(10)


# ### Processing all participants Gaze Data and putting it together in a Data Frame
#     

# In[444]:


Final_GZD=[]
Gzd_Flattened_List=[]
#print(len(folder_name))
for value in Files_List:
    if value.endswith("GZD.txt")==True and len(value)>10:
        folder_name =value.split(".",2)[0]
        file_name= value
        df=pd.read_csv(basepath+"/"+folder_name+"/"+file_name, sep = "\t", header=None,error_bad_lines=False)
        df['Participant']=folder_name
        df['Graph/Tree']=value.split(".",2)[1]
        Final_GZD.append([df.values.tolist()])
for values in Final_GZD:
    for n in values:
        for x in n:
            Gzd_Flattened_List.append(x)
df_Gaze_Data = pd.DataFrame(Gzd_Flattened_List[1:],columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


# In[445]:


df_Gaze_Data.head(10)


# In[447]:


df_Gaze_Data.rename(columns ={1:'time', 
                     2: 'number', 
                     3: 'screen_x_left_eye', 
                     4: 'screen_y_left_eye', 
                     5: 'cam_x_left_eye',
                     6:'cam_y_left_eye',
                     7:'distance_left_eye',
                     8:'pupil_left_eye',
                     9:'code_left_eye', 
                    10:'screen_x_right_eye', 
                    11:'screen_y_right_eye',
                    12:'cam_x_rigth_eye',
                    13:'cam_y_right_eye',
                    14:'distance_right_eye', 
                    15:'pupil_right_eye', 
                    16:'code_right_eye',
                    17:'Participant',
                    18:'Graph/Tree'},inplace = True)


# In[448]:


df_Gaze_Data.head(10)


# ### Processing all baseline data of all the participants and writing it to a DataFrame

# In[440]:


Final_Baseline_GZD=[]
Gzd_BaseLN_Flattened_List=[]
#print(len(folder_name))
for value in Files_List:
    if value.endswith("GZD.txt")==True and len(value)<11:
        temp =value.split(".",2)[0]
        folder_name = temp.rstrip("GZD")
        file_name= value
        df=pd.read_csv(basepath+"/"+folder_name+"/"+file_name, sep = "\t", header=None,error_bad_lines=False)
        df['Participant']=folder_name
        df['Graph/Tree']=folder_name+"_BaseLine_Data"
        Final_Baseline_GZD.append([df.values.tolist()])
for values in Final_Baseline_GZD:
    for n in values:
        for x in n:
            Gzd_BaseLN_Flattened_List.append(x)
df_Gaze_BaseLine_Data = pd.DataFrame(Gzd_BaseLN_Flattened_List[1:],columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


# In[441]:


df_Gaze_BaseLine_Data.head(5)


# In[449]:


df_Gaze_BaseLine_Data.rename(columns ={1:'time', 
                     2: 'number', 
                     3: 'screen_x_left_eye', 
                     4: 'screen_y_left_eye', 
                     5: 'cam_x_left_eye',
                     6:'cam_y_left_eye',
                     7:'distance_left_eye',
                     8:'pupil_left_eye',
                     9:'code_left_eye', 
                    10:'screen_x_right_eye', 
                    11:'screen_y_right_eye',
                    12:'cam_x_rigth_eye',
                    13:'cam_y_right_eye',
                    14:'distance_right_eye', 
                    15:'pupil_right_eye', 
                    16:'code_right_eye',
                    17:'Participant',
                    18:'Graph/Tree'},inplace = True)


# In[450]:


df_Gaze_BaseLine_Data.head(10)


# ### Basic information about the Files

# In[451]:


df_Event_Data.info()


# In[452]:


df_Fixation_Data.info()


# In[453]:


df_Gaze_Data.info()


# In[454]:


df_Gaze_BaseLine_Data.info()


# ### Differentiating Categorical with the Numerical Data

# In[457]:


df_Event_Data.describe(include = [np.number])


# In[458]:


df_Fixation_Data.describe(include = [np.number])


# In[459]:


df_Gaze_Data.describe(include = [np.number])


# In[460]:


df_Gaze_BaseLine_Data.describe(include = [np.number])


# ### Visualizing relationships between variables

# In[462]:


pair_plt = sns.pairplot(df_Event_Data, hue = 'event');
pair_plt.fig.set_figheight(12);
pair_plt.fig.set_figwidth(12);
pair_plt.fig.suptitle("Relationship between different variables");


# In[466]:


df_Event_Data.hist()


# In[465]:


pair_plt = sns.pairplot(df_Fixation_Data);
pair_plt.fig.set_figheight(12);
pair_plt.fig.set_figwidth(12);
pair_plt.fig.suptitle("Relationship between different variables");


# In[467]:


df_Fixation_Data.hist()

