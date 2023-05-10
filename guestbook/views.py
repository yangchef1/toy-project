from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from .models import GuestBook
# Create your views here.

@require_http_methods(["GET", "DELETE"])
def get_or_delete_GuestBook(request, id):
    guestbook = get_object_or_404(GuestBook, pk = id)
    
    if request.method == "GET":
        guestbook_json = {
            'id' : guestbook.id,
            'writer' : guestbook.writer,
            'content' : guestbook.content,
            'created_at' : guestbook.created_at
        }

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 조회 성공',
            'result' : guestbook_json
        })
    elif request.method == "DELETE":
        guestbook.delete()
    
        return JsonResponse({
            'status' : 200,
            'message' : '방명록 삭제 성공',
            'result' : None
        })
        

@require_http_methods(["GET", "POST"])
def create_or_getAll_GuestBook(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))

        new_guestbook = GuestBook.objects.create(
            writer = body['writer'],
            content = body['content']
        )

        new_guestbook_json = {
            'id' : new_guestbook.id,
            'writer' : new_guestbook.writer,
            'content' : new_guestbook.content,
            'created_at' : new_guestbook.created_at
        }

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 생성 성공',
            'result' : new_guestbook_json
        })
    elif request.method == "GET":
        all_guestbook = GuestBook.objects.all()
    
        guestbook_list = []

        for guestbook in all_guestbook:
            guestbook_json = {
                "id" : guestbook.id,
                "writer" : guestbook.writer,
                "content" : guestbook.content,
                "created_at" : guestbook.created_at
            }

            guestbook_list.append(guestbook_json)

        return JsonResponse({
            'status' : 200,
            'message' : '전체 방명록 조회 성공',
            'result' : guestbook_list
        })
   