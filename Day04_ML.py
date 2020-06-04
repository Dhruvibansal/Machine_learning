
##Day04
#SUDO install pip3 sklearn
### Python version
##import sys
##print('Python: {}'.format(sys.version))
### scipy
##import scipy
##print('scipy: {}'.format(scipy.__version__))
### numpy
##import numpy
##print('numpy: {}'.format(numpy.__version__))
### matplotlib
##import matplotlib
##print('matplotlib: {}'.format(matplotlib.__version__))
### pandas
##import pandas
##print('pandas: {}'.format(pandas.__version__))
### scikit-learn
##import sklearn
##print('sklearn: {}'.format(sklearn.__version__))
##print('###########################################################')
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url,names=column_names)
# output = (150, 5)
print(dataset.shape)
print('__________________________________________________________________________')
#OUTPUT
#sepal-length  sepal-width  petal-length  petal-width        class
#0            5.1          3.5           1.4          0.2  Iris-setosa
#1            4.9          3.0           1.4          0.2  Iris-setosa
#2            4.7          3.2           1.3          0.2  Iris-setosa
#3            4.6          3.1           1.5          0.2  Iris-setosa
#4            5.0          3.6           1.4          0.2  Iris-setosa
#5            5.4          3.9           1.7          0.4  Iris-setosa
#6            4.6          3.4           1.4          0.3  Iris-setosa
#7            5.0          3.4           1.5          0.2  Iris-setosa
#8            4.4          2.9           1.4          0.2  Iris-setosa
#9            4.9          3.1           1.5          0.1  Iris-setosa
#10           5.4          3.7           1.5          0.2  Iris-setosa
#11           4.8          3.4           1.6          0.2  Iris-setosa
#12           4.8          3.0           1.4          0.1  Iris-setosa
#13           4.3          3.0           1.1          0.1  Iris-setosa
#14           5.8          4.0           1.2          0.2  Iris-setosa
#15           5.7          4.4           1.5          0.4  Iris-setosa
#16           5.4          3.9           1.3          0.4  Iris-setosa
#17           5.1          3.5           1.4          0.3  Iris-setosa
#18           5.7          3.8           1.7          0.3  Iris-setosa
#19           5.1          3.8           1.5          0.3  Iris-setosa
__________________________________________________________________________
print(dataset.head(20))
print('__________________________________________________________________________') 	
# descriptions
print(dataset.describe())
print('__________________________________________________________________________')
# class distribution
print(dataset.groupby('class').size())
print('__________________________________________________________________________')

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

##print('__________________________________________________________________________')
### histograms
dataset.hist()

##print('__________________________________________________________________________')
### scatter plot matrix
scatter_matrix(dataset)

##print('__________________________________________________________________________')
'''Preprocessing of data'''
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,test_size=validation_size, random_state=seed)
##print('__________________________________________________________________________')
### Test options and evaluation metric
##seed = 7
scoring = 'accuracy'
##print('__________________________________________________________________________')
### Spot Check Algorithms
'''Create a model'''

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

### evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
##print('__________________________________________________________________________')
### Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
x = fig.add_subplot(111)
plt.boxplot(results)
#ax.set_xticklabels(names)
plt.show()
##print('__________________________________________________________________________')
##
### Make predictions on validation dataset (making models here of knn type)
knn = KNeighborsClassifier()

''' Apply fitting the data on the model always on training dataset'''
knn.fit(X_train, Y_train)

'''Deploy or say apply predict on your model'''
predictions = knn.predict(X_validation)
print(predictions)
print(accuracy_score(Y_validation, predictions))
#it tells how much accuracy is in our model
print(confusion_matrix(Y_validation, predictions))
#accurate v/s predicted data = confusion matrix 
print(classification_report(Y_validation, predictions))
##
p=list(predictions)
p.count('iris-virginica')
# to know the count of verginica tht is 10
 p.count('Iris-setosa')
# 7
