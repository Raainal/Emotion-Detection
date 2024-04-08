# Load the saved model
import tensorflow as tf
model = tf.keras.models.load_model('emotion_detection_model_adam_final.h5')

# Print the model architecture
model.summary()