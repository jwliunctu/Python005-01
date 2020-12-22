from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from hanziconv import HanziConv

# Create your views here.

def index(request):
    return HttpResponse('Hello Django!')

def movie(request):
    search = request.GET.get('q','') #取得網址q參數
    search = HanziConv.toSimplified(search) #轉簡體
    data = Comment.objects.filter(content__contains=search,star__gte=4).exclude(star=0).order_by('-created_at').all()
    return render(request, 'movie.html', locals())
