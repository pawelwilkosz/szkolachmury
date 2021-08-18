import numpy as np
import matplotlib.pyplot as plt
from keras.applications import MobileNet
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.mobilenet import preprocess_input
%matplotlib inline

mobilenet=MobileNet(weights='imagenet') 

filename = 'image.jpg'
original = load_img(filename, target_size=(224, 224))
plt.imshow(original)
plt.show()

numpy_image = img_to_array(original)
image_batch = np.expand_dims(numpy_image, axis=0)

processed_image = preprocess_input(image_batch.copy())
predictions = mobilenet.predict(processed_image)
label = decode_predictions(predictions)
print(label)