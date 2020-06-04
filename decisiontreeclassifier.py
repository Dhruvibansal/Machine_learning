## HERE WE GONNA READ FROM A LOCAL FILE save on ur desktop
import pandas as pd
#from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.model_selection import train_test_split  #if error in model_selection use sklearn.crossvalidation
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus as pdp
from IPython.display import Image
from sklearn.ensemble import RandomForestClassifier
###########Decision Tree Classifier##############
#HERE WE FETCH THE DATA 
cols=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima=pd.read_csv('PimaIndiansDiabetes.csv',header=None,names=cols)
print(pima.head())
feature_cols=['pregnant','age','insulin','bmi','glucose','pedigree','bp']
x=pima[feature_cols]
y=pima.label

# SPLIT THE DATA INTO TRAINING DATA SET AND TESTING DATA SET
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()
#clf=RandomForestClassifier(n_estimators=50)
clf=clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
result=confusion_matrix(y_test,y_pred)
print('Confusion Matrix')
print(result)
result1=classification_report(y_test,y_pred)
print('Classification Report: ',)
print(result1)
result2=accuracy_score(y_test,y_pred)
print('Accuracy:', result2)

##dot data is the data tht is convrted to graph : class names are the values of labels
dot_data=export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph=pdp.graph_from_dot_data(dot_data)
# to create image
graph.write_png('Tree.png')
Image(graph.create_png())
# to create pdf format
graph.write_pdf('tree.pdf')


