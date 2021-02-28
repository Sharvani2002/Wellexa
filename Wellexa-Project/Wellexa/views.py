from django.http import HttpResponse
from django.shortcuts import render
# import joblib
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from django.shortcuts import redirect

from . import notif_rem

import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# from tensorflow.python.keras.backend import set_session
# # import tensorflow as tf
# import tensorflow.compat.v1 as tf

# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.applications.imagenet_utils import decode_predictions
# import matplotlib.pyplot as plt
# import numpy as np
# from keras.applications import vgg16
# import datetime
# import traceback
# from . import models


def home(request):
    # return HttpResponse("<h1>This is Home</h1>")
    return render(request, "home.html")
def index(request):
    # return HttpResponse("<h1>This is Home</h1>")
    return render(request, "index.html")

def result(request):
    # cls = joblib.load("best_model.h5")
    lis = []
    lis.append(request.GET['Name'])
    # ans = cls.predict([lis])
    ans = 5
    return render(request, "result.html",{'ans': ans, 'lis': lis})

import time
import schedule

def speech(request):
    if request.method == 'POST':
        notif_rem.greeting()
        time1 = request.form['time1']
        time2 = request.form['time2']
        time3 = request.form['time3']
        time1=int(time1)
        time2=int(time2)
        schedule.every(time1).hours.do(water_notification)
        schedule.every(time2).minutes.do(take_a_break)  
        schedule.every().day.at("09:00").do(take_medication)
        schedule.every().day.at("22:00").do(bedtime)
        schedule.every().day.at("07:00").do(wish)
        while True:
        	schedule.run_pending()
        	time.sleep(1)

        response = 0
        return render(request,'text2speech.html', response)
    else:
        return render(request,'text2speech.html')


def monitor(request):
    response = redirect("http://23dbe3e00a99.ngrok.io/")
    # response = redirect("http://stackoverflow.com/")
    return response

# def index(request):
#     if  request.method == "POST":
#         f=request.FILES['sentFile'] # here you get the files needed
#         response = {}
#         file_name = "pic.jpg"
#         file_name_2 = default_storage.save(file_name, f)
#         file_url = default_storage.url(file_name_2)


#         # with tf.Session():
#         original = load_img(file_url, target_size=(224, 224))
#         numpy_image = img_to_array(original)
#         # image_batch = np.expand_dims(numpy_image, axis=0)
#         # prepare the image for the VGG model
#         # processed_image = vgg16.preprocess_input(image_batch.copy())
    
#     # get the predicted probabilities for each class
#         with settings.GRAPH1.as_default():
#             set_session(settings.SESS)
#             label = models.predict(numpy_image)
#             # predictions=settings.VGG_MODEL.predict(processed_image)
    
#         # label = decode_predictions(predictions)
    

        
#         label = list(label)[0]
#         response['name'] = str(label)
#         tf.keras.backend.clear_session()
#         return render(request,'form_page.html',response)

#     else:
#         return render(request,'form_page.html')