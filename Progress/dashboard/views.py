from django.shortcuts import render
from .models import User

# Create your views here.
def user_list(request):
	return render(request, 'dashboard/user_list.html',{"users": User.objects.all})
