from django.http import HttpResponse
from django.shortcuts import render
from snippet.models import Snippet

def top(request):
    snippet = Snippet.objects.all()
    context = {"snippet":snippet}
    return render(request, "snippet/top.html", context)

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    return HttpResponse('スニペットの詳細閲覧')

