from django.shortcuts import render
from rest_framework import generics
from .mutantDetector import isMutant
from rest_framework.response import Response


# Create your views here.
class MutantView(generics.CreateAPIView):
    def post(self, request):
        dna = request.data["dna"]
        if isMutant(dna):
            return Response(None, status=200)
        return Response(None, status=403)
