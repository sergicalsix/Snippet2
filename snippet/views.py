from django.http import HttpResponse,HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from snippet.models import Snippet
from snippet.forms import SnippetForm

def top(request):
    snippet = Snippet.objects.all()
    context = {"snippet":snippet}
    return render(request, "snippet/top.html", context)

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet , pk = snippet_id)
    #snippet = Snippet.object.all()
    return render(request, 'snippet/snippet_detail.html', {'snippet':snippet})

#ログインしていないユーザーがアクセスしたらログイン画面に吹っ飛ばす
@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_vaild():
            snippet = form.save(commit = False)
            snippet.created_by =  request.user 
            snippet.save()
            return redirect('snippet_detail', snippet_id = snippet.id)
    else:
        form = SnippetForm()
    return render(request, "snippet/snippet_new.html",{'form':form})

@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet , pk = snippet.id)
    if snippet.created_by.id != request.user.id:
        return HttpResponseForbidden('Forbidden!!')
    if request.method == 'POST':
        form = SnippetForm(request.POST , instance = snippet)
        if form.is_vaild():
            form.save()
            return redirect('snippet_detail', snippet_id = snippet.id)
    else:
        form = SnippetForm( instance = snippet)
    return render(request, "snippet/snippet_edit.html",{'form':form})

        
