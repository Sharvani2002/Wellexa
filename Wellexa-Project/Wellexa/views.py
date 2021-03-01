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
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from tensorflow.python.keras.backend import set_session
# import tensorflow as tf
import tensorflow.compat.v1 as tf
import numpy as np
import datetime
import traceback
from . import models


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
        ifremind = request.POST.get('ifremind','')
        time1 = request.POST.get('time1','')
        time2 = request.POST.get('time2','')
        time3 = request.POST.get('time3','')
        time1=int(time1)
        time2=int(time2)
        schedule.every(time1).hours.do(notif_rem.water_notification)
        schedule.every(time2).minutes.do(notif_rem.take_a_break)  
        schedule.every().day.at("09:00").do(notif_rem.take_medication)
        schedule.every().day.at("22:00").do(notif_rem.bedtime)
        schedule.every().day.at("07:00").do(notif_rem.wish)
        while ifremind == "yes":
        	schedule.run_pending()
        	time.sleep(1)

        #It'll keep on running
        return render(request,'text2speech.html')

    else:
        return render(request,'text2speech.html')


def monitor(request):
    response = redirect("http://23dbe3e00a99.ngrok.io/")
    # response = redirect("http://stackoverflow.com/")
    return response

# import sys
# from PIL import Image
# sys.modules['Image'] = Image 


def tmonitor(request):
    if  request.method == "POST":
        f=request.FILES['sentFile'] # here you get the files needed
        response = {}
        label, category = models.predict(f)
        
        # label = list(label)[0]
        # response['name'] = str(label)
        response['name'] = str(category)
        tf.keras.backend.clear_session()
        return render(request,'form_page.html',response)

    else:
        return render(request,'form_page.html')