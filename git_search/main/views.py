from django.shortcuts import render
#necesito importar requests
import requests
API_GITHUB_URL_SEARCH = 'https://api.github.com/search/'
# Create your views here.
def main_view(request):
    if request.method == 'POST':
        consulta = request.POST.get('busca_individuos')
        #necesito la consulta para hacer la peticion
        url_peticion = API_GITHUB_URL_SEARCH + 'users?q=' + consulta
        #necesito hacer el fetch de lo que consiga de la url anterior puesta
        response = requests.get(url_peticion)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'main.html', {'data': data})
        else:
            return render(request, 'main.html', {'error': 'No se encontraron resultados'})
    return render(request, 'main.html')

def list_view(request):
    return render(request, 'ppl_detail.html')