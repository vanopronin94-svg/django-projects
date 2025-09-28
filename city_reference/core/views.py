from django.shortcuts import render


def main(request):
    cities=["Москва","Санкт-Петербург","Саратов","Казань","Самара"]
    path=request.path
    path=path.replace("/","")
    if path == "":
        path="main"
    print(path)
    return render(request, f'{path}.html',{"cities":cities})
