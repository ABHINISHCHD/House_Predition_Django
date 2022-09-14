from django.shortcuts import render
import joblib
from sklearn.ensemble import RandomForestRegressor
from .models import predresult
# Create your views here.

def pred(request):
    if request.method == "POST":    
        dic={}
        dic['salary']=request.POST["salary"]
        dic['age']=request.POST["age"]
        dic['room']=request.POST["room"]
        dic['bedroom']=request.POST["bedroom"]
        dic['population']=request.POST["population"]
        model=joblib.load('house_predition.pkl')
        result=model.predict([[dic['salary'],dic['age'],dic['room'],dic['bedroom'],dic['population']]])
        dic['result']=int(result[0])
        dic['show']=1
        predresult.objects.create(salary=dic['salary'],age=dic['age'],room=dic['room'],
        bedroom=dic['bedroom'],population=dic['population'],price=dic['result'])
        
        return render(request,'predition/home.html',dic)

    else:
        return render(request,'predition/home.html')


def show(request):
    data=predresult.objects.all()
    return render(request,'predition/result.html',{'data':data})