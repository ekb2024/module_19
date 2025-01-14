from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer , Game

def  func_platform(request):
   return  render(request,"platform.html")
def  func_games(request):
      list = []
      games = Game.objects.all()
      for g in games:
          list.append(f' {g.title} | {g.description} Стоимость {g.cost}')
      context = {'games':list}
      return  render(request,"games.html",context)
def  func_cart(request):
     return  render(request,"cart.html")


users =['lom','istr','jem','kevi','link']
info = {}
def  sign_up_by_html(request):
     if request.method == 'POST':
        username= request.POST.get("username")
        password = request.POST.get('password')
        repeat_password= request.POST.get('repeat_password')
        age = request.POST.get('age')
        buyers = Buyer.objects.all()
        name_in = False
        for i in buyers:
             if i.name.upper() == username.upper():
                name_in = True
                break
        if name_in == False and password==repeat_password :

            Buyer.objects.create(name=username, balance=0, age=age)
            return render(request, 'registration_page.html', {'username':f'Приветствуем,{username} !'})
        else:
           if password != repeat_password : info.update({'error':'Пароли не совпадают'})
           if name_in == True: info.update({'error':'Пользователь уже существует'})
           return render(request, 'registration_page.html',info)
     return  render(request,'registration_page.html')


def  sign_up_by_django(request):
     if request.method == 'POST':
         form = UserRegister(request.POST)
         if form.is_valid():
             username = form.cleaned_data["username"]
             password = form.cleaned_data['password']
             repeat_password = form.cleaned_data['repeat_password']
             age = form.cleaned_data['age']
             buyers = Buyer.objects.all()
             name_in = False
             for i in buyers:
                 if i.name.upper() == username.upper():
                     name_in = True
                     break
             if name_in == False and password == repeat_password:
                 Buyer.objects.create(name=username, balance=0, age=age)
                 return render(request, 'registration_page.html', {'username': f'Приветствуем,{username} !'})
             else:
                 if password != repeat_password: info.update({'error': 'Пароли не совпадают'})
                 if name_in == True: info.update({'error': 'Пользователь уже существует'})
                 return render(request, 'registration_page.html', info)

     else:
         form = UserRegister()
     return render(request, 'registration_page.html',{'form':form})

