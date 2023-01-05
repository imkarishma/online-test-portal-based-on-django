from hashlib import new
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .models import Question,Detail
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
# Create your views here.
def home(request):
    return render(request,'home.html')

class Login(TemplateView):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            questions=Question.objects.all()
            return redirect('/')
        else:
            messages.error(request,'Invailid username and password')
            return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


class Signup(TemplateView):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        user.email=email
        user.save()
        return redirect('/login/')


            # question and answer


class ShowQuestion(TemplateView):
    def get(self,request):
        # print(request.user.username)
        if request.user.username:
            questions_list=[q for q in Question.objects.all()]
            # print(questions_list)
            random.shuffle(questions_list)
            questions_list=questions_list[:5]
            return render(request,'showquestion.html',{'questions':questions_list})
        else:
            return redirect('/')
    def post(self,request):
        question_list=[]
        correct_answer=[]
        worng_answer=[]
        total_attemp=0
        # print(request.POST)
        for k in request.POST:
            if k.startswith('que'):
                question_list.append(request.POST[k])
        for i in question_list:
            que=Question.objects.get(queno=i)
            try:
                if que.answer==request.POST['q'+i]:
                    correct_answer.append(i)
                else:
                    worng_answer.append(i)
                total_attemp+=1
            except:
                pass
        score=0.0
        if total_attemp!=0:
            score=(total_attemp-len(worng_answer))/total_attemp
            score*=100
            score=round(score,1)
        detail=Detail.objects.all()
        person_detail=None
        for d in detail:
            if request.user.username==str(d.user):
                person_detail=d
                break
        # print(person_detail.name)
        person_detail.points+=len(correct_answer)*2
        person_detail.correct+=len(correct_answer)
        person_detail.worng+=len(worng_answer)
        person_detail.solved+=total_attemp
        # person_detail.save()
        return render(request,'show-ans-new.html',{'correct':len(correct_answer),'total':total_attemp})

class AddQuestion(TemplateView):
    def get(self,request):
        return render(request,'addquestion.html')
    def post(self,request):
        q=Question()
        q.question=request.POST['question']
        q.optiona=request.POST['optiona']
        q.optionb=request.POST['optionb']
        q.optionc=request.POST['optionc']
        q.optiond=request.POST['optiond']
        q.answer=request.POST['ans']
        q.category=request.POST['cate']
        # print(request.user.username)
        q.user=request.user.username
        q.save()
        messages.success(request,'Question add successfully !!')
        # print(request.POST['cate'])
        return render(request,'addquestion.html')


def showadmin_question(request):
    questions=[q for q in Question.objects.all() if q.user==request.user.username ]
    return render(request,'showAllquestion.html',{'questions':questions})


def delete(request,queno):
    question=Question.objects.get(queno=queno)
    question.delete()
    return redirect('/showall-admin-question/')

class Edit(TemplateView):
    def get(self,request,queno):
        question=Question.objects.get(queno=queno)
        return render(request,'edit.html',{'question':question})
    def post(self,request,queno):
        question=request.POST['question']
        queno=request.POST['queno']
        optiona=request.POST['optiona']
        optionb=request.POST['optionb']
        optionc=request.POST['optionc']
        optiond=request.POST['optiond']
        ans=request.POST['ans']
        cate=request.POST['cate']
        # print(cate)
        q=Question(queno=queno,question=question,optiona=optiona,optionb=optionb,optionc=optionc,optiond=optiond,answer=ans,category=cate,user=request.user.username)
        q.save()
        messages.success(request,'question edit successfully !!')
        return render(request,'edit.html',{'question':q})


def profile(request):
    # details=Detail.objects.get(user=str(request.user.username))
    # print(details.name)
    # print(request.user.username)
    detail=Detail.objects.all()
    person_detail=None
    for d in detail:
        print(d.user)
        if request.user.username==str(d.user):
            person_detail=d
            break
    user=User.objects.get(username=request.user.username)
    email=user.email
    return render(request,'myprofile.html',{'person':person_detail,'email':email})
    
class EditProfile(TemplateView):
    def get(self,request):
        detail=Detail.objects.all()
        person_detail=None
        user=User.objects.get(username=request.user.username)
        email=user.email
        for d in detail:
            if request.user.username==str(d.user):
                person_detail=d
                break
        if person_detail is None:
            return render(request,'edit-profile.html',{'email':email})
        else:
            return render(request,'edit-profile.html',{'email':email,'name':person_detail.name,'institute':person_detail.institute,'degree':person_detail.degree,'branch':person_detail.branch,})
    
    def post(self,request):
        detail=Detail.objects.all()
        person_detail=None
        for d in detail:
            if request.user.username==str(d.user):
                person_detail=d
                break
        if person_detail is None:
            new_user=Detail()
            new_user.user=User.objects.get(username=request.user.username)
            new_user.name=request.POST['name']
            new_user.institute=request.POST['institute']
            new_user.branch=request.POST['branch']
            new_user.points=0
            new_user.solved=0
            new_user.correct=0
            new_user.worng=0
            new_user.save()
            return redirect('/myprofile/')
        else:
            person_detail.name=request.POST['name']
            email=request.POST['email']
            person_detail.institute=request.POST['institute']
            person_detail.degree=request.POST['degree']
            person_detail.branch=request.POST['branch']
            person_detail.save()
            user=User.objects.get(username=request.user.username)
            user.email=email
            user.save()
            messages.success(request,'Detail update successfully !!')
            return render(request,'myprofile.html',{'person':person_detail,'email':email})


def check_name(request):
    if request.method=='GET':
        username=request.GET['user']
        user=User.objects.filter(username=username)
        data={}
        if not user:
            data['value']='true'
            return JsonResponse(data)
        else:
            data['value']='false'
            return JsonResponse(data)

def guid(request):
    return render(request,'guid.html')