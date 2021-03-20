from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def index(request) :
    board_list = Board.objects.order_by('-create_date') # 정렬 순서를 create_date decending
    context = {'board_list' : board_list }
    return render(request, 'bbsnote/board_list.html', context)
    # return HttpResponse("bbsnote에 오신 것을 환영합니다.");