from django.shortcuts import render
from django.http import HttpResponse #add

# Create your views here.

def index(request): #default, http://localhost:2020/api/
    return HttpResponse("Hello API !") #add

def teststring(request): #test string, http://localhost:2020/api/teststring/
    testString = "There are test data!"
    return HttpResponse(testString)

def testdata(request): #test data for map, http://localhost:2020/api/testdata/
    testDic = {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    return HttpResponse(testDic)
