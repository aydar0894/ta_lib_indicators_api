from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from PRIPS_workflow import run_workflow
from .MatrixCalculation import MultiplierCorrelationCalculator, MongoConnector
import json
from bson import ObjectId

from pymongo import MongoClient


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)




@csrf_exempt
def add_indicators(request):
    if request.method == 'GET':
        client = MongoClient('localhost',
                        authSource='bitcoin')
        db = client.bitcoin
        ind = request.GET.get('indicators')
        indicators_to_add = json.loads(ind)
        
        indicators = db.indicators
        result = {}
        cursor = indicators.insert_many(indicators_to_add)
        i = 0
        for document in cursor:
            result.update({str(i): JSONEncoder().encode(document)})
            i +=1
        return JsonResponse(result, safe=False)
    return JsonResponse({"message": "Error"}, safe=False)



@csrf_exempt
def indicators_list(request):
    if request.method == 'GET':
        client = MongoClient('localhost',
                        authSource='bitcoin')
        db = client.bitcoin
        indicators = db.indicators
        result = {}
        cursor = indicators.find({})
        i = 0
        for document in cursor:
            result.update({str(i): JSONEncoder().encode(document)})
            i +=1
        return JsonResponse(result, safe=False)
    return JsonResponse({"message": "Error"}, safe=False)
