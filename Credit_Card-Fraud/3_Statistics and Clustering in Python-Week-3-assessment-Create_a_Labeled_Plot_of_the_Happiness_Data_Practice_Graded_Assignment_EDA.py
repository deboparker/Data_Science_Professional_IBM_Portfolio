
# coding: utf-8

# In[2]:


#Load the given Banknote authentication dataset.  

import pandas as pd 

data = pd.read_csv ('banknote_authentication_dataset.csv')
print(data)



# In[3]:


#Step 2: Calculate statistical measures, e.g. mean and standard deviation. 
data.describe()


# In[4]:


#Step 3: Visualise your data as you consider fit. 
import matplotlib.pyplot as plt


plt.scatter(data['V1'], data['V2'], alpha= 0.25)
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()


# In[7]:


# adding color to the graph to visually compar the two dimensions
plt.scatter(data.index, data['V1'], color= 'blue', alpha= 0.50, label='V1')
plt.scatter(data.index, data['V2'], color= 'green', alpha=0.5, label= 'V2')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.legend()
v1_max_idx = data['V1'].idxmax()
v1_min_idx = data['V1'].idxmin()
v2_max_idx = data['V2'].idxmax()
v2_min_idx = data['V2'].idxmin()

# add text labels at those points
plt.annotate(f"V1 max: {data['V1'].max():.2f}", (v1_max_idx, data['V1'].max()))
plt.annotate(f"V1 min: {data['V1'].min():.2f}", (v1_min_idx, data['V1'].min()))
plt.annotate(f"V2 max: {data['V2'].max():.2f}", (v2_max_idx, data['V2'].max()))
plt.annotate(f"V2 min: {data['V2'].min():.2f}", (v2_min_idx, data['V2'].min()))

plt.show()


# In[5]:


#not not transparent
plt.scatter(data.index, data['V1'], color= 'blue', label='V1')
plt.scatter(data.index, data['V2'], color= 'green', label= 'V2')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.legend()
v1_max_idx = data['V1'].idxmax()
v1_min_idx = data['V1'].idxmin()
v2_max_idx = data['V2'].idxmax()
v2_min_idx = data['V2'].idxmin()

# add text labels at those points
plt.annotate(f"V1 max: {data['V1'].max():.2f}", (v1_max_idx, data['V1'].max()))
plt.annotate(f"V1 min: {data['V1'].min():.2f}", (v1_min_idx, data['V1'].min()))
plt.annotate(f"V2 max: {data['V2'].max():.2f}", (v2_max_idx, data['V2'].max()))
plt.annotate(f"V2 min: {data['V2'].min():.2f}", (v2_min_idx, data['V2'].min()))

plt.show()


# In[6]:


#Step 4: Evaluate if the given dataset is suitable for the K-Means clustering task.
#Step 1 showed us that std 1 for V2 is double of std of V1, so now we have to scale the data 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_scaled =scaler.fit_transform(data[['V1', 'V2']])
print (data_scaled)


# In[18]:


# now lets see it visually scaled
plt.scatter(data.index, data_scaled[:, 0], color='blue', alpha=0.5, label='V1 (scaled)')
plt.scatter(data.index, data_scaled[:, 1], color='green', alpha=0.5, label='V2 (scaled)')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[7]:


#find the outliers
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = (data < lower_bound) | (data > upper_bound)
print(outliers.sum())


# In[8]:


# calculating the outliers NOT eyeballing it
from sklearn.cluster import KMeans

inertia = []
for k in range(1, 6):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(data_scaled)
    inertia.append(km.inertia_)

plt.plot(range(1, 6), inertia, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.show()


# In[ ]:


#Step 5: Write a short description of the dataset and your evaluation of its suitability for the K-Means clustering task.   

""""

Population: the entire collection of objects of interest.
Sample: a subset of the population observed.
Population parameter: a numerical characteristic of the population, usually unknown.
Sample statistic: a numerical characteristic of the sample used to estimate the population parameter."""

