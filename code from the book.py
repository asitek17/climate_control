from tensorflow import *
from keras import*
from numpy import array

dataset1=[
[18, 2, 7, 10, 100],
[32, 3, 30, 30, -400],
[44, 2, 10, 15, -100],
[50, 4, -3, 2, 0],
[20, 1, -30, -20, 400],
[3, 1, -30, -30, 600],
[44, 4, -7, -3, 250],
[52, 1, -30, -30, 0]
]

data_array=array(dataset1)

input=data_array[0:8,0:4]
output=data_array[0:8,4]


model=Sequential()
#Input layer input must be 4
model.add(layers.Dense(units=16,input_shape=[4]))
#Interlayer
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=64))
#Outputlayer units must be 1
model.add(layers.Dense(units=1))

model.compile(loss='mean_squared_error',optimizer='adam')

model.fit(x=input,y=output,epochs=15000)

tom=array([[22,4,-8,-4]])
lisa=array([[40,2,4,6]])
print(model.predict(tom))
print(model.predict(lisa))
