from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from membership.models import Member
from membership.serializers import MemberSerializer

class MemberView(APIView):

    def get(self, request):
        members = Member.objects.all()
        serializer= MemberSerializer(members,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MemberSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status = 400)