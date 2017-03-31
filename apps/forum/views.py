from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import Post, Comment
from ..logreg.models import User, Admin

# Create your views here.
def index(request):
	try:
		User.objects.get(id = request.session['id'])
	except:
		return redirect(reverse('login:home'))
	message = ""
	if not 'page' in request.session:
		request.session['page'] = 1
	request.session['page'] = int(request.session['page'])
	value = request.session['page'] * 10
	##if value > 10000:
		##value = 10
	posts = Post.objects.all()
	if request.session['page'] == 1:
		posts = Post.objects.all().order_by('-created_at')[:10]
	else:
		posts = Post.objects.annotate(total = Count('id')).order_by('-created_at')[value - 10:value]
		message += "<a href = '{}'>Previous:</a> ".format(reverse("forum:previous"))
	if len(posts) >= 10:
		try:
			next = Post.objects.annotate(total = Count('id'))[value]
		except IndexError:
			pass
		else:
			message += "<a href = '{}'>Next:</a><br>".format(reverse("forum:next"))
	pages = ""
	all = Post.objects.all()
	num = len(all) / 10
	##print num
	if num > 1:
		for i in range(1, num + 2):
			if not i == request.session['page']:
				pages += "<a href = '{}'>{}</a> ".format(reverse("forum:page", kwargs={'id': i}), i)
	context = {
		"posts": posts,
		"message": message,
		"pages": pages,
		"privilege": 0
	}
	try:
		user = User.objects.get(id = request.session['id'])
		admincheck = Admin.objects.get(users__id = request.session['id'])
		context['privilege'] = admincheck.privilege_level
		print "tried"
	except:
		pass
	return render(request, 'forum/index.html', context)

def add(request):
	text = request.POST['text']
	user = User.objects.get(id = request.session['id'])
	Post.objects.create(text = text, poster = user)
	request.session['comment'] = 1
	return redirect(reverse('forum:index'))

def next(request):
	request.session['page'] += 1
	return redirect(reverse('forum:index'))

def previous(request):
	request.session['page'] -= 1
	return redirect(reverse('forum:index'))

def nextcomment(request, id):
	request.session['comment'] += 1
	return redirect(reverse('forum:post', kwargs={'id': id}))

def previouscomment(request, id):
	request.session['comment'] -= 1
	return redirect(reverse('forum:post', kwargs={'id': id}))

def init(request, id):
	request.session['comment'] = 1
	return redirect(reverse('forum:post', kwargs={'id': id}))

def page(request, id):
	request.session['page'] = id
	return redirect(reverse('forum:index'))

def commentpage(request, id, page):
	request.session['comment'] = page
	return redirect(reverse('forum:post', kwargs={'id': id}))

def post(request, id):
	post = Post.objects.get(id = id)
	comments = Comment.objects.filter(post = post)
	message = ""
	pages = ""
	context = {}
	if not 'comment' in request.session:
		request.session['comment'] = 1
	request.session['comment'] = int(request.session['comment'])
	##if request.session['comment'] > 10000:
		##int(request.session['comment']) = 1
	if request.session['comment'] == 1:
		comments = Comment.objects.filter(post = post).order_by('created_at')[:9]
		if len(comments) >= 9:
			value = (request.session['page']) * 10
			try:
				next = Comment.objects.filter(post = post)[value - 1]
			except IndexError:
				pass
			else:
				print next.text
				message += "<a href = '{}'>Next:</a><br>".format(reverse("forum:nextcomment", kwargs={'id': id}))
		context = {
			"header": post,
			"post": post,
			"comments": comments,
			"message": message,
			"privilege": 0
		}
	else:
		value = request.session['comment'] * 10
		header =  Comment.objects.filter(post = post).order_by('created_at')[value - 11]
		comments = Comment.objects.filter(post = post).order_by('created_at')[value - 10: value - 1]
		message += "<a href = '{}'>Previous:</a><br>".format(reverse("forum:previouscomment", kwargs={'id': id}))
		if len(comments) >= 9:
			value = (request.session['comment']) * 10
			try:
				next = Comment.objects.filter(post = post)[value-1]
			except IndexError:
				pass
			else:
				message += "<a href = '{}'>Next:</a><br>".format(reverse("forum:nextcomment", kwargs={'id': id}))
		context = {
			"header": header,
			"post": post,
			"comments": comments,
			"message": message,
			"privilege": 0
		}
	request.session['comment'] = int(request.session['comment'])
	all = Comment.objects.filter(post = post)
	num = len(all) / 10
	##print num
	if num > 1:
		for i in range(1, num + 2):
			if not i == request.session['comment']:
				pages += "<a href = '{}'>{}</a> ".format(reverse("forum:commentpage", kwargs={'id': id, "page": i}), i)
	context["pages"] = pages
	try:
		user = User.objects.get(id = request.session['id'])
		admincheck = Admin.objects.get(users__id = request.session['id'])
		context['privilege'] = admincheck.privilege_level
		print "tried"
	except:
		pass
	return render(request, 'forum/post.html', context)

def comment(request, id):
	post = Post.objects.get(id = id)
	text = request.POST['text']
	user = User.objects.get(id = request.session['id'])
	Comment.objects.create(text = text, poster = user, post = post)
	return redirect(reverse('forum:post', kwargs={'id': id}))

def back(request):
	request.session['page'] = 1
	return redirect(reverse('forum:index'))

def delete(request, id):
	Post.objects.get(id = id).delete();
	request.session['page'] = 1
	return redirect(reverse('forum:index'))

def delcom(request, id, comment):
	Comment.objects.get(id = comment).delete();
	request.session['comment'] = 1
	return redirect(reverse('forum:post', kwargs={'id': id}))

def logout(request):
	del request.session['first_name']
	del request.session['id']
	return redirect(reverse('login:home'))
