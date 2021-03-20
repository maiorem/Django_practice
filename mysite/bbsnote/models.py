from django.db import models

# 게시판 모델
class Board(models.Model) :
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self) :
        return self.subject


# 댓글 모델
class Comment(models.Model) :
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

