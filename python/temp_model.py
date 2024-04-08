import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define image dimensions and other parameters
img_width, img_height = 48, 48
batch_size = 32
epochs = 20

# Define directories for training and testing data
train_data_dir = 'D:\Studies\Mini Project 2\Emotion Datasets\Emotion Detection\\train'
test_data_dir = 'D:\Studies\Mini Project 2\Emotion Datasets\Emotion Detection\\test'

# Create data generators for training and testing data
train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir, target_size=(img_width, img_height), batch_size=batch_size, class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    test_data_dir, target_size=(img_width, img_height), batch_size=batch_size, class_mode='categorical')

# Build the CNN model
model = Sequential([
  Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
  MaxPooling2D((2, 2)),
  Conv2D(64, (3, 3), activation='relu'),
  MaxPooling2D((2, 2)),
  Conv2D(128, (3, 3), activation='relu'),
  MaxPooling2D((2, 2)),
  Flatten(),
  Dense(128, activation='relu'),
  Dropout(0.5),
  Dense(train_generator.num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='nadam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
  train_generator,
  steps_per_epoch=train_generator.samples // batch_size,
  epochs=epochs,
  validation_data=test_generator,
  validation_steps=test_generator.samples // batch_size
)

# Save the trained model
model.save('emotion_detection_model_adam.h5')
