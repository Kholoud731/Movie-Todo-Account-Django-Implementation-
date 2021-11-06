from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):

#     return render(request, 'todo/home.html')


def get_tasks(request):

    return render(request, 'todo/home.html', context={'d' : my_task_list})


def get_task(request, **kwargs):

    p = int(kwargs['task_id'])
    el = my_task_list[ p - 1]
    return render(request, 'todo/view.html', context=el)


def update_task(request, **kwargs):
    p = int(kwargs['task_id'])
    el = my_task_list[ p - 1]
    el['name'] = el['name'].replace('-', " ")
    my_task_list[ p - 1] = el

    return render(request, 'todo/home.html', context={'d' : my_task_list})



def delete_task(request, **kwargs):
    p = int(kwargs['task_id'])
    ele = list(filter(lambda d: d.get('id') == p, my_task_list))
    index_of_task = my_task_list.index(ele[0])
    my_task_list.pop(index_of_task)
    return render(request, 'todo/home.html', context={'d' : my_task_list})





my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
]
