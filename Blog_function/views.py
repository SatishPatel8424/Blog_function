from django.shortcuts import render


# Create your views here.
def index(requst):
    return render(requst,'jquery_test.html')
def worker(requst):
    return render(requst,'worker.html')