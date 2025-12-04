from django.shortcuts import render
from core.forms import ReviewForm

def main(request):
    cities=["Москва","Санкт-Петербург","Саратов","Казань","Самара","Екатеринбург"]
    path=request.path
    path=path.replace("/","")
    if path == "":
        path="main"
    print(path)
    return render(request, f'{path}.html',{"cities":cities})
