from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response,redirect
from article.models import Article,Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf




def articles(request):
	return render_to_response('articles.html',{'articles':Article.objects.all()})

def article(request, article_id=1):
	comment_form=CommentForm
	args={}
	args.update(csrf(request))
	args['article']=Article.objects.get(id=article_id)
	args['comments']=Comments.objects.filter(comment_article_id=article_id)
	args['form']=comment_form
	return render_to_response('article.html',args)


def addlike(request,article_id):
	try:
		if article_id in request.COOKIES:
			return redirect('/')
		else:
			article=Article.objects.get(id=article_id)
			article.article_likes+=1
			article.save()
			response=redirect('/')
			response.set_cookie(article_id,'test')
			return response
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')


def addcomment(request,article_id):
	if request.POST and ('pause' not in request.session):
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.comment_article=Article.objects.get(id=article_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause']=True
	return redirect('/articles/get/%s/'%article_id)



