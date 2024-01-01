from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse
def create(request):
    if request.method == "POST":
        project_name = request.POST["pname"]
        description = request.POST['desc']
        startDate = request.POST['start_date']
        endDate = request.POST['end_date']
        new_project = Project.objects.create(name=project_name,description=description,start_date=startDate,end_date=endDate)
    return render(request,'create.html')
def task(request):
    if request.method == "POST":
        task_title = request.POST["title"]
        task_status = request.POST['status']
        task_deadline = request.POST['dead_line']
        new_task = Task.objects.create(title=task_title,deadline=task_deadline,status=task_status)
    return render(request,'task.html')
class create_Project(APIView):
    def get(self,request):
        project = Project.objects.all().values()
        project_name = self.request.query_params.get('name')
        if project_name is None :
            return HttpResponse(project)
        else:
            specific_project = Project.objects.filter(name= project_name).values()
            return HttpResponse(specific_project)
            
    def put(self,request):
        update_project_data = Project.objects.filter(name=request.data.get('name')).update(name=request.data.get('name'),description=request.data.get('description'),start_date=request.data.get('start_date'),end_date=request.data.get('end_date'))
        return Response({'message':'project updated succesfully'})
    def delete(self,request):
        delete_project = Project.objects.filter(name=request.data.get('name')).delete()
        return Response({'message':'project deleted succesfully'})

class Create_Task(APIView):
    def get(self,request):
        task = Task.objects.all().values()
        task_status = self.request.query_params.get('status')
        if task_status is None:
            return HttpResponse(task)
        else :
            specific_task_status = Task.objects.filter(status= task_status).values()
            return HttpResponse(specific_task_status)
    def put(self,request):
        update_task_data = Task.objects.filter(title=request.data.get('title')).update(title=request.data.get('title'),status=request.data.get('status'),deadline=request.data.get('deadline'))
        return Response({'message':'Task updated succesfully'})
    def delete(self,request):
        delete_task = Task.objects.filter(title=request.data.get('title')).delete()
        return Response({'message':'Task deleted succesfully'})     
class Team_Member(APIView):
    def post(self,request):
        new_member = Team_member(name = request.data.get("name"),task = request.data.get('task'),project = request.data.get('project'))
        return Response({'message':'Member created'})
    def get(self,request):
        member = Team_member.objects.all()
        member_name = self.request.query_params.get('name')
        if member_name is None:
            specific_member = Team_member.objects.filter(name= member_name).values()
            return HttpResponse(specific_member)
    def put(self,request):
        update_member_data = Team_member.objects.filter(name=request.data.get('name')).update(name=request.data.get('name'),task=request.data.get('task'),project=request.data.get('project'))
        return Response({'message':'Member updated succesfully'})
    def delete(self,request):
        delete_member = Task.objects.filter(name=request.data.get('name')).delete()
        return Response({'message':'Member deleted succesfully'})     
