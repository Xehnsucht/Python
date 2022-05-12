import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# The input and output, i.e. truth table, of a OR gate
x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "uint8")
y_train = np.array([[1], [1], [1], [0]], "uint8")

# Create neural networks model
model = Sequential()
# Add layers to the model
model.add(Dense(3, activation='relu', input_dim=2))     # first hidden layer
model.add(Dense(3, activation='relu'))                   # second hidden layer
model.add(Dense(1, activation='sigmoid'))               # output layer

# Compile the neural networks model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Train the neural networks model
model.fit(x_train, y_train, epochs=5000)

# Test the output of the trained neural networks based NAND gate
y_predict = model.predict(x_train)
print(y_predict)

# save model as h5 file
model.save("nand.h5")