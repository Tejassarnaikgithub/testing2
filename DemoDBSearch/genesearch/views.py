# Create your views here.
from django.shortcuts import render
import pandas as pd

def display_variants(request):
    excel_data = pd.read_excel('genesearch/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')

    query = request.GET.get('q')
    filtered_data = data

    if query:
        # Filter the data based on the query
        filtered_data = [item for item in data if query in str(item)]

    return render(request, 'genesearch/display_variants.html', {'data': filtered_data, 'query': query})


from django.shortcuts import render
import pandas as pd

def home(request):
    return render(request,'genesearch/home.html')

def login(request):
    return render(request,'genesearch/login.html')

def loginIN(request):
    return render(request,'genesearch/loginIN.html')

def search(request):
    return render(request,'genesearch/search.html')


def searchnew(request):
    return render(request,'genesearch/searchnew.html')

def searchgene(request):
    return render(request,'genesearch/searchgene.html')

def dhdds(request):
    return render(request,'genesearch/dhdds.html')

def prpf3(request):
    return render(request,'genesearch/prpf3.html')

def samd11(request):
    return render(request,'genesearch/samd11.html')

def crb1(request):
    return render(request,'genesearch/crb1.html')

from django.shortcuts import render
import pandas as pd

def filter_data(data, query):
    if query:
        return [item for item in data if query in str(item)]
    return data

def search(request):
    excel_data = pd.read_excel('genesearch/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')
    query = request.GET.get('q')
    filtered_data = filter_data(data, query)
    return render(request, 'genesearch/search.html', {'data': filtered_data, 'query': query})

def search_results(request):
    query = request.GET.get('q')
    excel_data = pd.read_excel('genesearch/data/disease.xlsx')
    data = excel_data.to_dict(orient='records')
    filtered_data = filter_data(data, query)
    return render(request, 'genesearch/search_results.html', {'data': filtered_data, 'query': query})





