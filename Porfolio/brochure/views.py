from django.shortcuts import render

from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("This is my homepage, to bad you suck")
#
# def ollo(request):
#     return HttpResponse('Shampoo is better')

# def hello(request, name):
#     return HttpResponse("Hello, {}".format(name))

# def drinks(request, var1, var2):
#     if int(var1)%3 == 0:
#         return HttpResponse("buzz")
#     elif int(var2)%5 == 0:
#         return HttpResponse("fizz")
#     else:
#         return HttpResponse("FizzBuzzy")


# def hello(request, name):
#     return HttpResponse("<h1>Hello!</h1>"
#                         "<p>Your name is {}</p>".format(name))

from django.shortcuts import render_to_response

# def hello(request, name, color):
#     return render_to_response("hello.html",
#     {'name': name, 'color': color}
# )
def life(request):
    return render_to_response("personal.html")