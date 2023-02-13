from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .util import processFile
from .models import Transacao

def upload(request):
    context = {}
    # Encaminhamento do arquivo CNAB recebido para a fn decoding()
    if request.method == "POST":
        file_txt = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(file_txt.name, file_txt)
        context['url'] = fs.url(name)
        processFile(pathName=context['url'])
    return render(request, 'index.html')