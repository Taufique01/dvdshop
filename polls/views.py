from django.shortcuts import render, get_object_or_404
from .models import Catagory,Movie,Basket,BasketDetails
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import  MovieShortSerializer,BasketSerializer,BasketDetailsSerializer
from django.http import HttpResponse, JsonResponse
from .forms import SignUpForm
import json
import requests
# Create your views here.
def home(request):

   
    movies = Movie.objects.filter(catagory='action')
    catagory = Catagory.objects.all().order_by('catagory')
    return render(request,'home.html',{'movies':movies,'catagories':catagory})

def movie_by_cat(request,catagory):
    movies = Movie.objects.filter(catagory=catagory)
    catagory = Catagory.objects.all().order_by('catagory')
    return render(request,'home.html',{'movies':movies,'catagories':catagory})

def movie_details(request,catagory,pk):
    movie = Movie.objects.get(pk=pk)
    return render(request,'details.html',{'movie':movie})

def get_basket(request):
    basket = Basket.objects.get(user=request.user)
    basket=BasketSerializer(basket,context={"request": request})
    data = basket.data
    print(data)
 
    return render(request,'basket.html',{'basket':data})
    
def add_to_basket(request,pk):
    if request.method=="POST":
        basket=request.user.basket_user
        movie=Movie.objects.get(id=pk)
        quantity=request.POST['quantity']
        basket_details,created=BasketDetails.objects.get_or_create(basket=basket,movie=movie)

        basket_details.quantity=int(quantity)
        basket_details.save()
        basket.total=basket.total+int(quantity)*movie.price
        basket.save()
       
            
        return JsonResponse({'status':'success'})
    
def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            
            user = authenticate(request,username=username, password=password1)
            if user is not None:
                login(request,user)
                Basket.objects.create(user=user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'form':form})  
    form=SignUpForm()
    return render(request,'signup.html',{'form':form})
            



     

    
    


