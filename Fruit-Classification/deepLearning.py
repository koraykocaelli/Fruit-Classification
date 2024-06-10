import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img_dim = (224, 224, 3)

model = Sequential()
model.add(MobileNet(weights='imagenet', include_top=False, input_shape=img_dim))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(16, activation='softmax'))

model.compile(loss='binary_crossentropy',
              optimizer=Adam(learning_rate=1e-3),
              metrics=['acc'])

model.summary()

train_data = 'dataset/train'
validation_data = 'dataset/validation'
test_data = 'dataset/test'

train_datagen = ImageDataGenerator(
      rescale=1./255, 
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest'
)

train_generator = train_datagen.flow_from_directory(
        train_data,
        target_size=(224, 224),
        batch_size=16,
)

validation_datagen = ImageDataGenerator(
        rescale=1./255
)

validation_generator = validation_datagen.flow_from_directory(
        validation_data,
        target_size=(224, 224),
        batch_size=16,
)

history = model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=50,
)

model.save('classification_model.h5')

test_datagen = ImageDataGenerator(
        rescale=1./255
)

test_generator = test_datagen.flow_from_directory(
        test_data,
        target_size=(224, 224),
        batch_size=32,
)

results = model.evaluate(test_generator) 
print("test loss, test acc:", results)
