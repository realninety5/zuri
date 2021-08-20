from my_resume.serializers import AboutSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Experience, Education, About, Skill
# Create your views here.
from rest_framework.decorators import api_view
from .send_mail import mail
import json

@api_view(['POST', 'GET'])
def contact(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        from_email = data['email']
        subject = data['subject']
        body = data['body']

        mail(subject, body, from_email)
        return JsonResponse({"message": "Message is sent"}, status=201)
    else:
        return JsonResponse({"message": "Wrong details."}, status=404)
    

def home(request):
    return render(request, "my_resume/index.html")

@api_view(('GET',))
def resume(request, value):
   
    if value == "about":
        res = About.objects.all()[0]
        serializer = AboutSerializer(res)
        return Response(serializer.data)

    if value == 'education':
        res = Education.objects.all()
        serializer = EducationSerializer(res, many=True)
        return Response(serializer.data)

    if value == 'experience':
        res = Experience.objects.all()
        serializer = ExperienceSerializer(res, many=True)
        return Response(serializer.data)


    if value == 'skill':
        res = Skill.objects.all()
        serializer = SkillSerializer(res, many=True)
        return Response(serializer.data)
    return HttpResponse("440044")