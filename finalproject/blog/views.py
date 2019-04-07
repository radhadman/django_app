from django.shortcuts import render

posts = [
	{
		'author': 'Haddon',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 6'
	},
	
	{
		'author': 'James',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 6'
	}
]
def home(request):
	context = {
		'posts': posts
		}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About the blog'})

