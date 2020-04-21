# first neural network with keras make predictions
from numpy import loadtxt
from keras.models import Sequential,load_model
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
model = load_model('my_model.h5')
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
total_prediction = 0
for i in range(len(X)):
	if predictions[i] == y[i]:
		total_prediction += 1
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

print(total_prediction,len(X), (total_prediction/len(X)))
