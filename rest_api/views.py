from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET'])
def apiMain(request):
    api_urls = {
        'All todos': 'all',
        'Specific Todo': 'todo/<str:pk>/',
        'Create Todo': 'todo-create/',
        'Update Todo': 'todo-update/<str:pk>/',
        'Delete Todo': 'todo-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def todoAll(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def todoById(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response('Todo not found!')


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Couldn't save Todo!")


@api_view(['POST'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Couldn't update Todo!")


@api_view(['DELETE'])
def todoDelete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response('Todo deleted!')
    except Todo.DoesNotExist:
        return Response("Todo doesn't exist!")
