from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .util import processFile
from .models import Transacao
from loja.models import Loja

def upload(request):
    context = {}
    # Encaminhamento do arquivo CNAB recebido para a fn decoding()
    if request.method == "POST":
        if 'document' in request.FILES:
            file_txt = request.FILES['document']
        else: 
            raise Exception("Sem arquivo.")
        fs = FileSystemStorage(location="tmp/")
        name = fs.save(file_txt.name, file_txt)
        context['url'] = "tmp/"+fs.url(name)
        processFile(pathName=context['url'])
    return render(request, 'index.html')



def lista(request):
    resp = {"data_response": {}}
    for loja in Loja.objects.all():
        resp["data_response"][loja.nome] = {
            'dados': loja,
            'trasacoes': Transacao.objects.filter(loja_id=loja.id)
        }

    return render(request, 'resultado.html', resp)