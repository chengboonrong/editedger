from django.shortcuts import render

# Create your views here.
def countDown(request):
	return render(request, 'countdown.html')
