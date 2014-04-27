from django.shortcuts import render, get_object_or_404
from headlinesBlog.models import Headtable

# Create your views here.
def index(request):
	posts = Headtable.objects.filter(published=True)
	return render(request, 'headlinesBlog/index.html', {'posts': posts})

def post(request, slug):
	post = get_object_or_404(Headtable, slug=slug)
	return render(request, 'headlinesBlog/post.html', {'post':post})