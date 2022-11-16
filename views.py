# views.py

from django.shortcuts import render
from .models import 모델이름 # DB 모델 불러오기
from django.contrib import messages

from django.views.generic import View
from django.http import HttpResponse 
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate

# 메인 페이지
def main(request):
    return render(request,'main/main.html')

# 로그인 페이지
def login(request):
    return render(request,'main/login.html')

# 회원가입 페이지
def signup(request):
    return render(request,'main/signup.html')

# 수강신청 페이지 (학생용)
def registration(request):
    return render(request,'main/rfc.html')

# 개설교과목 페이지 (교수용)
def course(request):
    return render(request,'main/course.html')

# 이하 DB code (명세서에 알고리즘 항목 작성을 위해서 최종적으로 아래 코드와 models.py 작성해 주시면 됩니다! 코드는 DB 설계하신 거에 맞춰서 작성해 주세요!)

# 로그인/회원가입 (교수/학생)

# student use-case start

# 수강신청 등록

# 수강신청 취소

# student use-case end

# doctor use-case start

# 개설교과목 조회

# 개설교과목 등록

# 개설교과목 삭제

# doctor use-case end 