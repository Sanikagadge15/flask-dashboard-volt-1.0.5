[08:06, 3/26/2022] Pratam Jain: import pyodbc
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from IPython.display import HTML


server = 'sqlite:///site.db' 
database = 'appseed-flask' 
username = 'appseed' 
password = 'pass'  
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = "SELECT [CountryRegionCode], [Name] FROM Person.CountryRegion;"
df1 = pd.read_sql(query, cnxn)


nRowsRead = 'None'
nRow, nCol = df1.shape

df1_shuffled = df1.sample(frac = 1)
df1_splits = np.array_split(df1_shuffled, 4)

# Mental disability
mind_df = df1_splits[0]
# Locomotive disability
loco_df = df1_splits[1]
# Deaf and dumb
dnd_df = df1_splits[2]
# Vision
vision_df = df1_splits[3]

total_scho = df_final["Scholarship Headcount"].sum()

df_final.columns = ['acad_yr', 'tap_code', 'fed_code', 'tap_name', 'tap_grp', 'scho_head', 'scho_fte', 'scho_amt', 'dis_type', 'dis_per']

df_final_splits = np.array_split(df_final, 4)
#df_final_splits

mind_df_final = df_final_splits[0]
loco_df_final = df_final_splits[1]
dnd_df_final = df_final_splits[2]
vision_df_final = df_final_splits[3]



plt.bar(mind_df_final['acad_yr'], mind_df_final['scho_head'], color = 'blue', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Number of Scholarships")
plt.title("Mental Scholarships By Year")
plt.savefig('mentalnum_byyr.png')

plt.bar(loco_df_final['acad_yr'], loco_df_final['scho_head'], color = 'blue', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Number of Scholarships")
plt.title("Locomotive Scholarships By Year")
plt.savefig('loconum_byyr.png')

plt.bar(dnd_df_final['acad_yr'], dnd_df_final['scho_head'], color = 'blue', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Number of Scholarships")
plt.title("Deaf & Dumb Scholarships By Year")
plt.savefig('dndnum_byyr.png')

plt.bar(vision_df_final['acad_yr'], vision_df_final['scho_head'], color = 'blue', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Number of Scholarships")
plt.title("Vision Scholarships By Year")
plt.savefig('visionnum_byyr.png')

plt.bar(mind_df_final['acad_yr'], mind_df_final['scho_amt'], color = 'red', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Total Scholarship Amount")
plt.title("Mental Scholarship Amount By Year")
plt.savefig('mentalamt_byyr.png')

plt.bar(loco_df_final['acad_yr'], loco_df_final['scho_amt'], color = 'red', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Total Scholarship Amount")
plt.title("Locomotive Scholarship Amount By Year")
plt.savefig('locoamt_byyr.png')

plt.bar(dnd_df_final['acad_yr'], dnd_df_final['scho_amt'], color = 'red', width = 0.4)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Total Scholarship Amount")
plt.title("Deaf & Dumb Scholarship Amount By Year")
plt.savefig('dndamt_byyr.png')

plt.bar(vision_df_final['acad_yr'], vision_df_final['scho_amt'], color = 'red', width = 0.5)
plt.xticks([2015, 2016, 2017, 2018])
plt.xlabel("Academic Year")
plt.ylabel("Total Scholarship Amount")
plt.title("Vision Scholarship Amount By Year")
plt.savefig('visionamt_byyr.png')

plt.pie([sum(mind_df_final['scho_amt']), sum(loco_df_final['scho_amt']), sum(dnd_df_final['scho_amt']), sum(vision_df_final['scho_amt'])], labels = ['Mental', 'Locomotive', 'Deaf & Dumb', 'Blind'], autopct = "%1.1f%%")
plt.title("Scholarship Amount by Type of Disability")
plt.savefig('schoamt_distype.png')

plt.pie([sum(mind_df_final['scho_head']), sum(loco_df_final['scho_head']), sum(dnd_df_final['scho_head']), sum(vision_df_final['scho_head'])], labels = ['Mental', 'Locomotive', 'Deaf & Dumb', 'Blind'], autopct = "%1.1f%%")
plt.title("Total Scholarships by Type of Disability")
plt.savefig('schocount_distype.png')

df_updated = pd.read_csv('data.csv')
df_updated['status'] = [0 if x < 7.0 else 1 for x in df_updated['score']]
plt.pie(df_updated['status'].value_counts(normalize = True), labels = ["Active", "Inactive"], autopct='%1.1f%%')
[08:09, 3/26/2022] Pratam Jain: import pyodbc
import pandas as pd
import io
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from IPython.display import HTML

server = 'sqlite:///site.db' 
database = 'appseed-flask' 
username = 'appseed' 
password = 'pass'  

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = "SELECT [CountryRegionCode], [Name] FROM Person.CountryRegion;"
df = pd.read_sql(query, cnxn)

df.drop(['tap_code', 'fed_code' , 'tap_name','tap_grp','dis_type'],1,inplace=True)
s = (df['percent'](0.4) + df['dis_per'](0.3) - df['fam_inc'](2) + df['no_of_sib'](2.5))/5
df['score'] = s
df.loc[df['score'] <= 7, 'status'] = 0
df.loc[df['score'] > 7, 'status'] = 1
X = df.drop(columns = ['status'])
y = df['status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
knn = KNeighborsClassifier()
#create a dictionary of all values we want to test for n_neighbors
params_knn = {'n_neighbors': np.arange(1, 25)}
#use gridsearch to test all values for n_neighbors
knn_gs = GridSearchCV(knn, params_knn, cv=5)
#fit model to training data
knn_gs.fit(X, y)
knn_best = knn_gs.best_estimator_

#check best n_neigbors value
print(knn_gs.best_params_)
rf = RandomForestClassifier()

#create a dictionary of all values we want to test for n_estimators
params_rf = {'n_estimators': [50, 100, 200]}

#use gridsearch to test all values for n_estimators
rf_gs = GridSearchCV(rf, params_rf, cv=5)

#fit model to training data
rf_gs.fit(X_train, y_train)
rf_best = rf_gs.best_estimator_

#check best n_estimators value
print(rf_gs.best_params_)
log_reg = LogisticRegression()

#fit the model to the training data
log_reg.fit(X_train, y_train)
#print('knn: {}'.format(knn_best.score(X_test, y_test)))
#print('rf: {}'.format(rf_best.score(X_test, y_test)))
#print('log_reg: {}'.format(log_reg.score(X_test, y_test)))

estimators=[('knn', knn_best), ('rf', rf_best), ('log_reg', log_reg)]

#create our voting classifier, inputting our models
ensemble = VotingClassifier(estimators, voting='hard')

#fit model to training data
ensemble.fit(X_train, y_train)

#test our model on the test data
ensemble.score(X_test, y_test)

X_test.sort_values(by="score",ascending=False).to_csv('file2.csv')


html = df.to_html()

# write html to file
text_file = open("dashboard.html", "w")
text_file.write(html)
text_file.close()