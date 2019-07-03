from django.shortcuts import render


from blog.models import Post

def listing(request):
	posts_list = Post.objects.all()
	paginator = Paginator(posts_list, 2)

	page = request.GET.('page')
	posts = paginator.get_page(page)
	return render(request, 'posts_list.html', {'posts':posts})
