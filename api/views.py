from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
import requests
# Create your views here.
def index(request):
    dic={}
    if request.method=='POST':
        username=request.POST.get('username')
        url='https://api.github.com/users/%s' %username
        response=requests.get(url)
        user=response.json()
        # print(user['message'])
        if response.status_code==200:
            response=requests.get('https://api.github.com/users/%s/repos' %username)
            public_repo=response.json()
            if len(public_repo)>0:
                dic['repos']=public_repo
            
        dic['git_user']=user
        
    return render(request,'index.html',dic)

