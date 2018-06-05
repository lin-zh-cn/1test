from django.shortcuts import render
from webmoni.publicFunc import get_index_pie
from genericFunc import check_login
# Create your views here.
@check_login
def index(request):
    if request.method == 'GET':
        pie_data = get_index_pie()
    return render(request, 'index.html',{'pie_data':pie_data})
