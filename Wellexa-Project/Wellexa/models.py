import h5py
from keras.models import load_model

def predict(image):
    model = load_model('best_model.h5')
    ans = model.predict(image)

    return predicted_class