from django.shortcuts import render

# Create your views here.
def home(request):
    print(request.GET)
    name=request.GET.get("name")
    email=request.GET.get("email")
    rating=request.GET.get("rating")
    review=request.GET.get("review")
    return render(request,"index.html",{"name":name,"email":email,"rating":rating,"review":review})