
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import h5py
from keras.models import load_model
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from tensorflow.python.keras.backend import set_session
# import tensorflow as tf
import tensorflow.compat.v1 as tf

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
# import matplotlib.pyplot as plt
import numpy as np
from keras.applications import vgg16
import datetime
import traceback
from . import models

def predict(f):

    #get the file
    file_name = "pic.jpg"
    file_name_2 = default_storage.save(file_name, f)
    file_url = default_storage.url(file_name_2)
    file_url = file_url[1:]

    # with tf.Session():
    original = load_img(file_url, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # prepare the image for the VGG model
    processed_image = vgg16.preprocess_input(image_batch.copy())
    
    #NOTES:------------------------------------
    #Since Graphs in tf are better, try to use graphs 
    #instead of eagerly mode
    #------------------------------------------
    # get the predicted probabilities for each class
        # with settings.GRAPH1.as_default():
        #     set_session(settings.SESS)
        #     tf.config.run_functions_eagerly(False)
        #     # label = models.predict(numpy_image)
        #     predictions=tf.function(settings.VGG_MODEL.predict(processed_image))
        # tf.config.run_functions_eagerly(False)
            # label = models.predict(numpy_image)

        # predictions=settings.VGG_MODEL.predict(processed_image)
        
        # label = decode_predictions(predictions)


    # model = load_model('best_model.h5')
    ans = settings.MY_MODEL.predict(processed_image)
    classes_list = ['butter_chicken', 'butter_naan', 'chicken_fried_rice', 'chole_bhature', 
    'dahi_bhalla', 'dal_makhani', 'gajar_halwa', 'hilsa_fish_curry', 'idli', 'jalebi',
    'kachori', 'kadai_paneer','kulfi', 'masala_dosa', 'nalli_nihari', 
    'pasta', 'peda', 'pizza', 'rasgulla', 'samosa', 'vada_pav']
    ans = np.argmax(ans)
    category = classes_list[ans]
    return ans, category