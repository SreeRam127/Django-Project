from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from home.models import Books
from home.models import Sign
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'index.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name = name, email = email, phone = phone, desc = desc)
        ins.save()
    return render(request,'contact.html')

def books(request):
    if request.user.is_anonymous:
        return redirect('/login')
    allbooks = Books.objects.all()
    context = {'book':allbooks}
    return render(request,'books.html',context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

# def sign_Up(request):
    # if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # print(username)
        # password1 = request.POST['password1']
        # if password != password1:
            # redirect('signUp')
        # ins = Sign(username=username,password=password)
        # ins.save()
        # redirect('/login')
    # return render(request,'sign_Up.html')            

def sign_Up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect('/login')
    return render(request,'sign_Up.html')     


# class SearchView(ListView):
    # model = Books
    # template_name = 'books.html'
    # context_object_name = 'all_search_results'
# 
    # def get_queryset(self):
        # result = super(SearchView, self).get_queryset()
        # query = self.request.GET.get('search')
        # if query:
            # postresult = Books.objects.filter(title__contains=query)
            # result = postresult
        # else:
            # result = None
        # return result    


def searchView(request):
    search_term = ''
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == 'GET':
        search_term = request.GET['searchTxt']
        contents = Books.objects.filter(title  = search_term )
        return render(request, 'searchIt.html', {'contents' : contents})  

    return redirect('/books')


# def searchView(request):
    # search_term = ''
    # if request.user.is_anonymous:
        # return redirect('/login')
    # if request.method == 'GET':
        # search_term = request.GET['searchTxt']
        # if search_term:
            # contents = Books.objects.filter(title  = search_term )
            # result = contents
            # return render(request, 'searchIt.html', {'contents' : contents,result:'result'})  
        # else:
            # result = 0
            # return render(request, 'searchIt.html',{result:'result'})
            # return redirect('/books')
    # return redirect('/books')    


     
     
     
     
    