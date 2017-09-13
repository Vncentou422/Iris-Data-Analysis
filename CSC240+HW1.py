
# coding: utf-8

# In[77]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

data = pd.read_csv("iris.data", names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])


# In[78]:

plt.figure()


# In[79]:

df = pd.DataFrame(data)


# In[80]:

df.head()


# In[95]:

ax = df[['Sepal Length','Sepal Width','Petal Length','Petal Width']].plot(kind='box', title ="Boxplot of Sepal and Petal Dimensions", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Name", fontsize=12)
ax.set_ylabel("Dimension", fontsize=12)


# In[96]:

plt.show()


# In[97]:

for name, df_name in df.groupby('Name'):
    print(df_name)


# In[98]:

region_list=df['Name'].unique().tolist()


# In[112]:

s = df['Name'].ne(df['Name'].shift()).cumsum()
print(s)


# In[113]:

dfs = [g for i,g in df.groupby(df['Name'].ne(df['Name'].shift()).cumsum())]


# In[114]:

dfs0 = dfs[0]


# In[115]:

dfs1 = dfs[1]


# In[116]:

dfs2 = dfs[2]


# In[117]:

ax = dfs0[['Sepal Length','Sepal Width','Petal Length','Petal Width']].plot(kind='box', title ="Boxplot of Sepal and Petal Dimensions for Iris-setosa", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Name", fontsize=12)
ax.set_ylabel("Dimension", fontsize=12)
plt.show()


# In[118]:

ax = dfs1[['Sepal Length','Sepal Width','Petal Length','Petal Width']].plot(kind='box', title ="Boxplot of Sepal and Petal Dimensions for Iris-versicolor", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Name", fontsize=12)
ax.set_ylabel("Dimension", fontsize=12)
plt.show()


# In[119]:

ax = dfs2[['Sepal Length','Sepal Width','Petal Length','Petal Width']].plot(kind='box', title ="Boxplot of Sepal and Petal Dimensions of Iris-virginica", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Name", fontsize=12)
ax.set_ylabel("Dimension", fontsize=12)
plt.show()


# In[123]:

pd.concat([dfs0['Sepal Length'], dfs1['Sepal Length'], dfs2['Sepal Length']], axis=1).boxplot()
plt.show()


# In[124]:

pd.concat([dfs0['Sepal Width'], dfs1['Sepal Width'], dfs2['Sepal Width']], axis=1).boxplot()
plt.show()


# In[125]:

pd.concat([dfs0['Petal Length'], dfs1['Petal Length'], dfs2['Petal Length']], axis=1).boxplot()
plt.show()


# In[126]:

pd.concat([dfs0['Petal Width'], dfs1['Petal Width'], dfs2['Petal Width']], axis=1).boxplot()
plt.show()


# In[132]:

df.plot.scatter(x="Sepal Length", y="Petal Length")
plt.show()


# In[133]:

df.plot.scatter(x="Sepal Width", y="Petal Width")
plt.show()


# In[149]:

df["Sepal Length"].mean()


# In[150]:

df["Sepal Length"].median()


# In[151]:

df["Sepal Width"].mean()


# In[152]:

df["Sepal Width"].median()


# In[153]:

df["Petal Length"].mean()


# In[154]:

df["Petal Length"].median()


# In[155]:

df["Petal Width"].mean()


# In[156]:

df["Petal Width"].median()


# In[ ]:



