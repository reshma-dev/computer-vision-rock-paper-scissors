from time import sleep
import cv2
from keras.models import load_model
import numpy as np

# Return the output of the Keras model
def get_prediction(frame):
    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    print(prediction)
    return 

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

prediction = get_prediction(frame)
cv2.imshow('frame', frame)
sleep(4)
print(prediction)

# Destroy all the windows
cv2.destroyAllWindows()