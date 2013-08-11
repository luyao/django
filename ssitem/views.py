# Create your views here.
#-*- coding:utf-8 -*-

from django.http 	import Http404, HttpResponse, HttpResponseRedirect
from django.template 	import RequestContext
from django.shortcuts 	import render_to_response, get_object_or_404
from django.db.models 	import Q
from django.contrib.auth.decorators 	import login_required
from django.contrib.contenttypes.models import ContentType

from sscomment.models 	import Qcomment
from ssitem.models 	import Shise
from sscomment.forms 	import QcommentForm 
from ssuser.models import RegistrationProfile

class urlInfo:
	url=""
	name=""

class averageScore:
	class commentCate:
		name=""
		score=5.0

	class userSkinType:
		skinType=""
		score=4.0
		nTotal=1

	total=0.0
	cate=[]
	type=[]


def getCommentCate(scoreList):
	nameList = ["吸收度", "持久度", "防晕染", "性价比", "色彩度"]
	list=[]
	for index in range(len(nameList)):
		cate = averageScore.commentCate()
		cate.name = nameList[index]
		cate.score = scoreList[index]
		list.append(cate)
	return list

def getUserSkinType(scoreList):
	totalList = [52, 46, 29, 13, 11]
	nameList  = ["混合性", "中性", "油性", "干性", "敏感性"]
	list=[]
	for index in range(len(nameList)):
		cate = averageScore.commentCate()
		cate.name   = nameList[index]
		cate.score  = scoreList[index]
		cate.nTotal = totalList[index]
		list.append(cate)
	return list

def getScoreList(qcommentall):
	list = [0.0, 0.0, 0.0, 0.0, 0.0]
	index = 0
	for comment in qcommentall:
		list[0] += comment.absorption
		list[1] += comment.durability
		list[2] += comment.anti_blooming
		list[3] += comment.ppr
		list[4] += comment.color
		index += 1
	if index == 0:
		return list

	for i in range(0, len(list)):
		list[i] /= index
	
	return list

def shiseview(request, sid, form_class=QcommentForm, template_name="shise/item.html"):
	item = get_object_or_404(Shise, id=sid)
	creator = object
	try:
		creator = item.author
	except:
		creator.username="default"

	qcommentall   = item.qcomments.all()
	qcommentcount = qcommentall.count()
	scoreList = getScoreList(qcommentall)
	cntList   = [3.7, 4.8, 5, 2, 1.0]
	average_score = averageScore()
	average_score.total = round( sum(scoreList)/len(scoreList), 1)
	average_score.cate  = getCommentCate(scoreList)
	average_score.type  = getUserSkinType(cntList)

	#for items in the same brand
	items_in_same_brand = Shise.objects.filter(brand=item.brand)
	if request.method == 'POST':
		successurl = '#in'
		#处理添加评论请求
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			content = form.cleaned_data.get("content",'')
			try:
				qcom = form.GetComment()
			except:
				qcom = Qcomment(content=content, lights=10)

			qcom.author = request.user
			qcom.content_object = item 
			qcom.save()
		else:
			successurl = '%s#postfailed' %(item.get_absolute_url())
			return HttpResponseRedirect(successurl)
	else:
		form = form_class()

	context = RequestContext(request)
	return render_to_response(template_name, 
		{'item':item,
		 'items_in_same_brand':items_in_same_brand,
		 'top_offset':1800,
		 'average_score':average_score,
		 'creator': creator,
		 'form':form, 'qcommentlist':qcommentall, 'qcommentcount':qcommentcount},
		context_instance=context)
