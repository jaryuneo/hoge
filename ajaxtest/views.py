from django.shortcuts import render
import math
# Create your views here.
import json
from django.http import HttpResponse,Http404

#https://intellectual-curiosity.tokyo/2019/07/13/django%E3%81%A7ajax%E5%87%A6%E7%90%86%E3%82%92%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95%EF%BC%88get%EF%BC%8Fpost%EF%BC%89/

def index(req):
    return render(req,'freetest.html')

def write(req):
    if req.method == 'GET':
        def fib(n):
            fibonacci=1/math.sqrt(5)*(((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)
            return fibonacci

        num=int(req.GET.get('input_data'))
        num_l=num-1
        if num >= 1:
            fact=fib(num)/fib(num_l)
        else:
            fact = "None"
        response = json.dumps(fact)  # JSON形式に直す。(ダンプ)
        return HttpResponse(response,content_type="text/javascript")
        #https://yura2.hateblo.jp/entry/2015/03/31/Django_1.7%E3%81%A7%E3%81%AFmimetype%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%8Fcontent_type%E3%82%92%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B