# Load the trained model
model = models.load_model('intent_recognition_model.h5')

# Define the vocabulary and the number of classes
vocab_size = 10000
num_classes = 3

# Define a dictionary to map the intent class indices to their corresponding labels
class_labels = {0: 'lights_on', 1: 'play_music', 2: 'set_reminder'}

# Preprocess the input string
input_str = 'Turn on the lights'
input_seq = tokenizer.texts_to_sequences([input_str])
input_seq = pad_sequences(input_seq, maxlen=maxlen)

# Predict the intent of the input string
pred_probs = model.predict(input_seq)[0]
pred_class_idx = np.argmax(pred_probs)
pred_class_label = class_labels[pred_class_idx]

# Execute the appropriate action based on the predicted intent
if pred_class_label == 'lights_on':
    turn_on_lights()
elif pred_class_label == 'play_music':
    play_music()
elif pred_class_label == 'set_reminder':
    set_reminder()
