import pyodbc
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
text_file = open("ml.html", "w")
text_file.write(html)
text_file.close()

from flask import Flask, render_template
app = Flask(_name_)

@app.route('/')
def home():
   return render_template('ml.html')
if _name_ == '_main_':
   app.run()