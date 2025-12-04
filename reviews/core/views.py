from django.shortcuts import render,redirect
from core.forms import ReviewForm 
from core.models import ReviewModel
# Create your views here.
def home(request):
    if request.method == 'GET':
        form = ReviewForm()
        try:
            entry=ReviewModel.objects.get(id=1)
            return render(request, 'index.html', {'form': form,"name":entry.name,"review":entry.review, "rating":entry.rating})
        except Exception:
        
            return render(request, 'index.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            ReviewModel.objects.create(name=name,email=email,review=review,rating=rating)
            return redirect('reviews')

        else:
            form = ReviewForm()
            return render(request,'index.html', {'form': form})