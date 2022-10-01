# **Importing the libraries**

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import pylab as py


# **Importing the dataset**

# In[2]:


dataset=pd.read_csv('DATA FOR PROJECT (2).csv')


# In[3]:


dataset.head()


# In[4]:


dataset.tail()


# In[5]:


dataset.shape


# In[6]:


dataset.dtypes


# In[7]:


dataset.count()


# In[8]:


dataset.describe()


# In[9]:


dataset.info()


# In[10]:


dataset.isna()


# **Data Visualization**

# In[13]:


get_ipython().system('pip install missingno')
import missingno as msno
msno.bar(dataset,color='pink')
plt.show()


# Finding the locations of the missing value

# In[14]:


msno.matrix(dataset)
plt.show()


# In[16]:


##calculating the percentage of missing values in each column


# In[17]:


dataset.isna().sum()/dataset.shape[0]


# **Dropping rows and columns corresponding to missing values**

# In[18]:


print(dataset)


# In[22]:


##dropping columns with high percentage of missing values


# In[23]:


df=dataset.drop(columns=['aes','ffmc','dmc','dc','bui','isi','fwi','dsr','wmo'])


# In[24]:


##dropping the rows for missing dependent variables


# In[25]:


df.dropna(subset=["Fire/Not Fire"],axis=0, inplace=True)
print(df)


# In[26]:


df.count()


# In[27]:


x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values


# In[28]:


##calculating the skewness of each row to check what kind of imputation to consider 


# In[29]:


from scipy.stats import skew
df.skew(axis = 0, skipna = True)


# In[44]:


from sklearn.experimental import enable_iterative_imputer 
# now you can import normally from sklearn.impute
from sklearn.impute import IterativeImputer
imp = IterativeImputer()
# Fit to the dataset containing missing values
imp.fit(x)


# In[34]:


x


# In[35]:


# Transform the dataset containing missing values


# In[36]:


x=pd.DataFrame(x,columns=["temp","td","rh","ws","wg","wdir","pres","vis","precip","rndays","sog"])
x.count()


# In[37]:


print(x)


# In[34]:


y=pd.DataFrame(y,columns=["Fire/Not Fire"])
y.count()


# In[38]:


df1 = pd.concat([x,y], axis=1)
print(df1)


# Preprocessing of Data 

# In[39]:


print(x)
print(y)


# VISUALIZATION OF THE CLEAN DATA

# In[36]:


sns.countplot(x='Fire/Not Fire',data=df)
plt.xlabel('Fire Detection')
plt.ylabel('Number of Observations')
plt.title('Bar Chart for Fire Detection')
plt.show()


# PIE-CHART

# In[40]:


import matplotlib.pyplot as plt
values=df1['Fire/Not Fire'].value_counts()
labels=['Fire','No-Fire']
plt.pie(values,labels=labels,radius = 1,explode = (0.1, 0),shadow=True,startangle=120,autopct='%1.1f%%') 
plt.title('Forest Fire Detection',fontsize=25)
plt.legend()
plt.show()


# In[41]:


plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(dataset.corr(), vmin=-1, vmax=1, annot=False)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':13}, pad=13)
plt.show()


# Splitting dataset into training and test set

# In[42]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)


# In[43]:


print(x_train)
print(x_test)
print(y_train)
print(y_test)


# In[44]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


# LASSO
# 

# In[45]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
lin_reg_y_pred = lin_reg.predict(x_test)
mse = mean_squared_error(y_test, lin_reg_y_pred)
print(mse)


# In[46]:


lin_reg.coef_


# In[47]:


from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
lasso = Lasso()
lasso.fit(x_train, y_train)
y_pred_lasso = lasso.predict(x_test)
mse = mean_squared_error(y_test, y_pred_lasso, squared=True)
print(mse)


# In[37]:


lasso.coef_


# In[48]:


from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(x_train, y_train)
y_pred_ridge = ridge.predict(x_test)
mse = mean_squared_error(y_test, y_pred_ridge,squared=True)
print(mse)


# In[49]:


ridge.coef_


# In[50]:


plt.figure(figsize=(30,6))
z = [ 'Lasso', 'linear','Ridge']
y1 = np.array([-0.,0.15582913,0.15582913])
y2 = np.array([0., -0.0432623,-0.0432623])
y3 = np.array([0., -0.18124843,-0.18124843])
y4 = np.array([0.,0.1070943,0.1070943])
y5 = np.array([0., -0.02373324,-0.02373324])
y6 = np.array([0.,-0.0145852,-0.0145852 ])
y7 = np.array([0., 0.0035039,0.0035039])
y8 = np.array([0.,-0.00628179,-0.00628179 ])
y9 = np.array([0.,-0.08407087,-0.08407087 ])
y10 = np.array([0.,0.05173443,0.05173443 ])
y11 = np.array([0., -0.00233666, -0.00233666])
fig, axes = plt.subplots(ncols=1, nrows=1)
plt.bar(z, y1, color = 'black')
plt.bar(z, y2, bottom=y1, color='b')
plt.bar(z, y3, bottom=y1+y2, color='g')
plt.bar(z, y4, bottom=y1+y2+y3, color='r')
plt.bar(z, y5, bottom=y1+y2+y3+y4, color='magenta')
plt.bar(z, y6, bottom=y1+y2+y3+y4+y5, color='brown')
plt.bar(z, y7, bottom=y1+y2+y3+y4+y5+y6, color='cyan')
plt.bar(z, y8, bottom=y1+y2+y3+y4+y5+y6+y7, color='yellow')
plt.bar(z, y9, bottom=y1+y2+y3+y4+y5+y6+y7+y8, color='pink')
plt.bar(z, y10, bottom=y1+y2+y3+y4+y5+y6+y7+y8+y9, color='grey')
plt.bar(z, y11, bottom=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10, color='orange')
plt.xlabel("Models")
plt.ylabel("Coefficients")
plt.title("Comparing coefficients of different models")
axes.set_xticklabels(['Lasso', 'Ridge'])


# In[51]:


from sklearn.linear_model import LassoCV

# Lasso with 5 fold cross-validation
model = LassoCV(cv=5, random_state=0, max_iter=10000)

# Fit model
model.fit(x_train, y_train)


# In[52]:


model.alpha_


# In[53]:


lasso = Lasso()
lasso.fit(x_train,y_train)
train_score=lasso.score(x_train,y_train)
test_score=lasso.score(x_test,y_test)
coeff_used = np.sum(lasso.coef_!=0)
print ("training score:", train_score)
print ("test score: ", test_score)
print ("number of features used: ", coeff_used)
lasso001 = Lasso(alpha=0.0001, max_iter=10e5)
lasso001.fit(x_train,y_train)
train_score001=lasso001.score(x_train,y_train)
test_score001=lasso001.score(x_test,y_test)
coeff_used001 = np.sum(lasso001.coef_!=0)
print( "training score for alpha=0.01:", train_score001 )
print ("test score for alpha =0.01: ", test_score001)
print ("number of features used: for alpha =0.01:", coeff_used001)
lasso2 = Lasso(alpha=0.002, max_iter=10e5)
lasso2.fit(x_train,y_train)
train_score2=lasso2.score(x_train,y_train)
test_score2=lasso2.score(x_test,y_test)
coeff_used02 = np.sum(lasso2.coef_!=0)
print ("training score for alpha=0.00029214457393486354:", train_score2 )
print ("test score for alpha =0.0.00029214457393486354: ", test_score2)
print ("number of features used: for alpha =0.00029214457393486354:", coeff_used02)
lr = LinearRegression()
lr.fit(x_train,y_train)
lr_train_score=lr.score(x_train,y_train)
lr_test_score=lr.score(x_test,y_test)
print( "LR training score:", lr_train_score )
print( "LR test score: ", lr_test_score)
plt.subplot(1,2,1)
plt.plot(lasso.coef_,alpha=0.7,linestyle='none',marker='*',markersize=5,color='red',label=r'Lasso; $\alpha = 1$',zorder=7) # alpha here is for transparency
plt.plot(lasso001.coef_,alpha=0.5,linestyle='none',marker='d',markersize=6,color='blue',label=r'Lasso; $\alpha = 0.01$') # alpha here is for transparency

plt.xlabel('Coefficient Index',fontsize=16)
plt.ylabel('Coefficient Magnitude',fontsize=16)
plt.legend(fontsize=13,loc=4)
plt.subplot(1,2,2)
plt.plot(lasso.coef_,alpha=0.7,linestyle='none',marker='*',markersize=5,color='red',label=r'Lasso; $\alpha = 1$',zorder=7) # alpha here is for transparency
plt.plot(lasso001.coef_,alpha=0.5,linestyle='none',marker='d',markersize=6,color='blue',label=r'Lasso; $\alpha = 0.0001$') # alpha here is for transparency
plt.plot(lasso2.coef_,alpha=0.8,linestyle='none',marker='v',markersize=6,color='black',label=r'Lasso; $\alpha = 0.00029214457393486354$') # alpha here is for transparency
plt.plot(lr.coef_,alpha=0.7,linestyle='none',marker='o',markersize=5,color='green',label='Linear Regression',zorder=2)
plt.xlabel('Coefficient Index',fontsize=16)
plt.ylabel('Coefficient Magnitude',fontsize=16)
plt.legend(fontsize=13,loc=4)
plt.tight_layout()
plt.show()


# PCA

# In[54]:


from sklearn.decomposition import PCA
pca=PCA(n_components=9)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)
pca.explained_variance_ratio_


# In[55]:


np.cumsum(pca.explained_variance_ratio_)


# In[56]:


pca=PCA().fit(x_train)
x=np.arange(1,10,step=1)
y = np.cumsum(pca.explained_variance_ratio_)
plt.plot(x,y,linestyle="--",marker="o",color="blue")
plt.grid()
plt.axhline(y=0.95,linestyle='dashdot',color="red")
plt.xlabel("Number of components")
plt.ylabel("Cumulative Variance Explained")
plt.title("The optimal number of components to explain a specified variance")
plt.show()


# LOGISTIC REGRESSION

# In[57]:


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)


# In[58]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred=classifier.predict(x_test)
cm_lg=confusion_matrix(y_test,y_pred)
print(cm_lg)
accuracy_score(y_test,y_pred)


# In[ ]:





# In[60]:


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# K nearest neighbours

# ELbow method 

# In[61]:


from sklearn.cluster import KMeans
WCSS=[]
for i in range(1,20):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  WCSS.append(KMeans.inertia_)
plt.plot(range(1,20),WCSS)
plt.title("the elbow method")
plt.xlabel("number of clusters")
plt.ylabel("WCSS")
plt.show()


# In[62]:


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(x_train,y_train)


# In[63]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred1=classifier.predict(x_test)
cm_KN=confusion_matrix(y_test,y_pred1)
print(cm_KN)
accuracy_score(y_test,y_pred1)


# In[65]:


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# Naive Bayes

# In[64]:


from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)


# In[66]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred2=classifier.predict(x_test)
cm_NB=confusion_matrix(y_test,y_pred2)
print(cm_NB)
accuracy_score(y_test,y_pred2)


# In[67]:


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# Decision Tree

# In[68]:


from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)


# In[69]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred3=classifier.predict(x_test)
cm_DT=confusion_matrix(y_test,y_pred3)
print(cm_DT)
accuracy_score(y_test,y_pred3)


# In[70]:


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# **Random Forest Classifier**

# In[71]:


from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)


# In[72]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred4=classifier.predict(x_test)
cm_RF=confusion_matrix(y_test,y_pred4)
print(cm_RF)
accuracy_score(y_test,y_pred4)


# In[73]:


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# **SVM Classifier**

# from sklearn.svm import SVC
# classifier=SVC(kernel='rbf',random_state=0)
# classifier.fit(x_train,y_train)

# from sklearn.metrics import confusion_matrix ,accuracy_score
# y_pred5=classifier.predict(x_test)
# cm_svm=confusion_matrix(y_test,y_pred5)
# print(cm_svm)
# accuracy_score(y_test,y_pred5)

# from sklearn.model_selection import cross_val_score
# accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)
# print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
# print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

# XGBOOST

# In[ ]:


from xgboost import XGBClassifier
classifier= XGBClassifier()
classifier.fit(x_train,y_train)


# In[ ]:


from sklearn.metrics import confusion_matrix ,accuracy_score
y_pred5=classifier.predict(x_test)
cm_xg=confusion_matrix(y_test,y_pred5)
print(cm_xg)
accuracy_score(y_test,y_pred5)
