from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
from .user_forms import UserForm
from django.shortcuts import redirect

# Create your views here.
def user_list(request):
	return render(request, 'dashboard/user_list.html',{"users": User.objects.all})

def user_new(request):
	if request.method == "POST" :
		form = UserForm(request.POST)
		if form.is_valid() :
			post = form.save(commit=False)
			# post.user_name = request.user
			# post.about_myself = request.about_myself
			# post.college = request.college
			post.save()
			return redirect('user_list')
	form = UserForm()
	return render(request, 'dashboard/user_edit.html',{'form': form})

	