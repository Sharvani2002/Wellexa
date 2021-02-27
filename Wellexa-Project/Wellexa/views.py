from django.http import HttpResponse
from django.shortcuts import render
# import joblib


def home(request):
    # return HttpResponse("<h1>This is Home</h1>")
    return render(request, "home.html")

def result(request):

    # cls = joblib.load("best_model.h5")

    lis = []
    lis.append(request.GET['Name'])

    # print(lis)

    # ans = cls.predict([lis])
    ans = 5

    return render(request, "result.html",{'ans': ans, 'lis': lis})