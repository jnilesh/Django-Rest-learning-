from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

	def get(self, request, format=None):
		# Create your views here.
		an_apiview = [
			'Some string text',
			'other text'

		]

		return Response({'message':'hello', 'an_apiview': an_apiview })