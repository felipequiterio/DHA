import numpy as np
from tensorflow.keras import layers, models

# Define the training data
train_x = np.array(['turn on the lights', 'play some music', 'set a reminder'])
train_y = np.array(['lights_on', 'play_music', 'set_reminder'])

# Define the vocabulary and the number of classes
vocab_size = 10000
num_classes = len(set(train_y))

# Tokenize the training data
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(train_x)
sequences = tokenizer.texts_to_sequences(train_x)
maxlen = max(len(x) for x in sequences)
train_x = pad_sequences(sequences, maxlen=maxlen)

# Define the model architecture
model = models.Sequential()
model.add(layers.Embedding(vocab_size, 64, input_length=maxlen))
model.add(layers.LSTM(64))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])

# Train the model
one_hot_train_y = to_categorical(train_y, num_classes=num_classes)
model.fit(train_x, one_hot_train_y, epochs=10, batch_size=32, validation_split=0.2)
