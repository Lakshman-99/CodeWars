from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
from django.http import HttpResponse
import os


def index(request):
    return render(request, 'index.html')

def editor(request):
    return render(request, 'editor.html')

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
                os.system('gcc program.c')
                os.system('type nul > output.txt')
                os.system('a.exe>output.txt')
                output = open('output.txt', 'r').read()


            elif(lang == 'cpp'):
                coding = open('program.cpp','a')
                coding.write(code)
                coding.close()
                os.system('g++ program.cpp')
                os.system('output.txt')
                os.system('a.exe>output.txt')
                output = open('output.txt', 'r').read()

            else:
                coding = open('program.js','a')
                coding.write(code)
                coding.close()
                os.system('output.txt')
                os.system('node program.js>output.txt')
                output = open('output.txt', 'r').read()


            try:
                os.system('del program.cpp')
                os.system('del program.c')
                os.system('del program.js')
                os.system('del output.txt')
                os.system('del file.txt')
                os.system('del a.exe')

            except:
                print("")



        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e


    return HttpResponse(output)
