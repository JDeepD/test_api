from django.shortcuts import render
from django .http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app1.models import Jokes
from app1.serializers import Jokes_Serializer

@csrf_exempt
def joke_list(request):
    """
    GET: It will list all jokes
    POST: Will add a new joke into the database
    """

    if request.method == 'GET':
        all_jokes = Jokes.objects.all()
        serialized_jokes = Jokes_Serializer(all_jokes, many=True)
        return JsonResponse(serialized_jokes.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialized_data = Jokes_Serializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data, status=201)
        return JsonResponse(serialized_data.errors, status=400)




@csrf_exempt
def jokes_detail(request, pk):
    try:
        joke = Jokes.objects.get(pk=pk)
    except Jokes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialized_joke = Jokes_Serializer(joke)
        return JsonResponse(serialized_joke.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialized_data = Jokes_Serializer(joke, data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data)
        return JsonResponse(serialized_data.errors, status=400)

    elif request.method == 'DELETE':
        joke.delete()
        return HttpResponse(status=204)


