from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
import sys,os
import subprocess


def index(request):
    return render(request, 'index.html')

def editor(request):
    return render(request, 'editor.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
        	form = CreateUserForm(request.POST)
        	if form.is_valid():
        		form.save()
        		user = form.cleaned_data.get('username')
        		messages.success(request, 'Account was created for ' + user)

        		return redirect('login')


        context = {'form':form}
        return render(request, 'account/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
    	if request.method == 'POST':
    		username = request.POST.get('username')
    		password =request.POST.get('password')

    		user = authenticate(request, username=username, password=password)

    		if user is not None:
    			login(request, user)
    			return redirect('index')
    		else:
    			messages.info(request, 'Username OR password is incorrect')

    	context = {}
    	return render(request, 'account/login.html', context)


@csrf_exempt
def code(request):
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['language']


        try:

            if(lang == 'python'):
                original_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w')
                exec(code)  #example =>   print("hello world")
                sys.stdout.close()
                sys.stdout = original_stdout
                output = open('file.txt', 'r').read()

            elif(lang == 'c'):
                coding = open('program.c','a')
                coding.write(code)
                coding.close()
                p1 = subprocess.run('tdm/bin/gcc program.c -o program.exe', capture_output=True, text=True, shell=False)
                if(p1.stderr):
                    result_compiler = str(p1.stderr)
                    output=result_compiler
                else:
                    p2 = subprocess.run('program.exe', capture_output=True, shell=False)
                    output=p2.stdout.decode("UTF-8")

            elif(lang == 'cpp'):
                coding = open('program.cpp','a')
                coding.write(code)
                coding.close()
                p1 = subprocess.run('tdm/bin/g++ program.cpp -o program.exe', capture_output=True, text=True, shell=False)
                if(p1.stderr):
                    result_compiler = str(p1.stderr)
                    output=result_compiler
                else:
                    p2 = subprocess.run('program.exe', capture_output=True, shell=False)
                    output=p2.stdout.decode("UTF-8")

            else:
                coding = open('program.js','a')
                coding.write(code)
                coding.close()
                p1 = subprocess.run('node program.js ', capture_output=True, text=True, shell=False)
                if(p1.stderr):
                    result_compiler = str(p1.stderr)
                    output=result_compiler
                else:
                    output=p1.stdout

            try:
                os.system('del program.cpp')
                os.system('del program.c')
                os.system('del program.js')
                os.system('del file.txt')
                os.system('del program.exe')

            except:
                print("")


        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    return HttpResponse(output)

def practice(request):
    return render(request, 'practice.html')
