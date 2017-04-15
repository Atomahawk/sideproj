from sklearn import tree

# Dataset of 11 people

#	[height, weight, shoesize]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],
	 [190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],
	 [181,85,43]]

Y = ['male','female','female','female','male','male','male','female','male','female','male']

# decision tree classifier (clf)
clf = tree.DecisionTreeClassifier()

# store result in the clf variable
# "fit" method trains decision tree on our data
clf = clf.fit(X,Y)

# predict gender given a new value
prediction = clf.predict([[150,50,36]])

print(prediction)

# the best classifier from svm, per, KNN
index = np.argmax([acc_svm, acc_per, acc_KNN])
classifiers = {0: 'SVM',1: 'Perceptron',2: 'KNN'}
print('Best gender classifier is {}'.format(classifiers[index]))