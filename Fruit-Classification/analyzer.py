from keras.applications.mobilenet import preprocess_input
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from matplotlib import pyplot as plt
import numpy as np
from PySide6.QtGui import QPixmap
from io import BytesIO

class Analyzer:

    def __init__(self):
        # Class names
        self.nameArray = [
            "freshapples", "freshbanana", "freshgrapes", "freshkiwi", "freshoranges",
            "freshpear", "freshstrawberry", "freshwatermelon", "rottenapples",
            "rottenbanana", "rottengrapes", "rottenkiwi", "rottenoranges",
            "rottenpear", "rottenstrawberry", 'rottenwatermelon'
        ]

    def modify_image(self, imagePath):
        # Import model
        model = load_model('classification_model.h5')
        # Assign image path
        img_path = imagePath
        try:
            img = load_img(img_path, target_size=(224, 224))
        except Exception as e:
            print(f"Error loading image: {e}")
            return None, None, None
        print("Image modification started...")
        # Convert image to array
        img_array = img_to_array(img)
        # Expand dimensions to match the model input
        img_batch = np.expand_dims(img_array, 0)
        # Preprocess the image for prediction
        img_prep = preprocess_input(img_batch)
        # Make prediction
        prediction = model.predict(img_prep)
        return prediction, img_path, img

    def prediction(self, imgData):
        prediction, img_path, img = imgData
        if prediction is None:
            return None, None
        prediction = prediction[0]
        # Choose the class with the highest predicted probability
        predicted_class_index = np.argmax(prediction)
        # Get the confidence score
        confidence = prediction[predicted_class_index]
        if predicted_class_index < len(self.nameArray):
            # Get class name
            class_name = self.nameArray[predicted_class_index]
        else:
            class_name = "Undefined Class!"
            confidence = 0
        info = (
            f"Image Path: {img_path}\n"
            f"Predicted Class Index: {predicted_class_index}\n"
            f"Predicted Class: {class_name}\n"
            f"Confidence: {confidence}"
        )
        print(info)
        confidence = np.around(confidence, 2)
        plt.figure()
        if confidence <= 0.70:
            plt.title("Undefined Class!", fontsize=20, color='#be2da8', fontweight='bold')
        else:
            plt.title(class_name.upper(), fontsize=20, color='#be2da8', fontweight='bold')
        plt.text(x=10, y=210, s="Confidence:", fontdict={"color": "b", "fontsize": 25, "style": "normal","weight": "bold"})
        plt.text(x=200, y=210, s=str(confidence), fontdict={"color": "g", "fontsize": 30, "style": "normal","weight": "bold"})
        plt.axis('off')
        plt.imshow(img)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close()
        return pixmap, info
