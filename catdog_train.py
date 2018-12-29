import pickle
import tensorflow
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense,Dropout


windows=3

x = pickle.load(open('Pickles/X.pickle','rb'))
y = pickle.load(open('Pickles/Y.pickle','rb'))

print(x.shape)
print(x.shape[1:])

x=x/255

#create model
model = Sequential()

#flattening not required 

#input layer (convolution)#hidden layer with pooling
model.add(Conv2D(64,(3,3), input_shape = x.shape[1:], activation = 'relu'))
'''ARG for Conv2D is( no of nodes
requires, (no of window,no of window))'''
model.add(MaxPooling2D(pool_size = (3,3)))

#second layer
model.add(Conv2D(64,(3,3), activation = 'relu'))
model.add(MaxPooling2D( pool_size = (3,3) ))

#flatten layer
model.add(Flatten())

"""Input shape should be applied to input layer only so we need not specifie input shape"""
# dense layers
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.3))
model.add(Dense(128, activation ='relu'))
model.add(Dropout(0.3))

#finaly layer
model.add(Dense(2, activation = 'softmax'))

#compile
model.compile(optimizer = 'adam',loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])
print(model.fit.__doc__)
#fit
model.fit(x,y, epochs = 3, validation_split = 0.1 )
'''validating_split: out of the total data the model is spliting the data into training set and
    validating set'''
#validate

#save
#model.save('Models/catsdogs_1.model')
