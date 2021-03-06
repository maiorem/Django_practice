from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.
def index(request) :
    page=request.GET.get('page', 1) # page 이름으로 넘어오는 정보가 없으면 1
    board_list = Board.objects.order_by('-create_date') # 정렬 순서를 create_date decending
    # 페이징 처리
    paginator=Paginator(board_list, 5) # 페이징 기준을 5개 리스트로(6개째부터 2페이지)
    page_obj=paginator.get_page(page)
    context = {'board_list' : page_obj }
    return render(request, 'bbsnote/board_list.html', context)
    # return HttpResponse("bbsnote에 오신 것을 환영합니다.");

def detail(request, board_id) :
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id) :
    board = Board.objects.get(id=board_id)
    # comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # comment.save()
    # Board 모델과 Comment 모델이 Foreign key로 묶여 있는 경우 _set으로 해주면 자동으로 표현이 됨
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now()) 
    return redirect('bbsnote:detail', board_id=board.id)

def board_create(request) :
    if request.method=='POST' :
        form=BoardForm(request.POST)
        if form.is_valid() :
            board=form.save(commit=False) # 저장은 하되 커밋은 하지 말 것.
            board.create_date=timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else :
        form=BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})