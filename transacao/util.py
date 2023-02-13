from .form import TrasacaoForm
from loja.models import Loja
from loja.form import LojaForm
def processFile(pathName):
    pathName = pathName[1:]

    with open(str(pathName), 'r', encoding="utf-8") as arquivo:
        lines = arquivo.readlines()
        for line in lines:
            if len(line)==82:
                tipo = line[0]
                data = f'{line[7:9]}.{line[5:7]}.{line[1:5]}'
                valor = int(line[9:19])/100
                cpf = f'{line[19:22]}.{line[22:25]}.{line[25:28]}-{line[28:30]}'
                cartao = f'{line[30:34]}.{line[34:38]}.{line[38:42]}'
                hora = f'{line[42:44]}:{line[44:46]}:{line[46:48]}'
                dono_da_loja = line[48:62]
                nome_da_loja = line[62:81]

                tracao = TrasacaoForm({
                    "tipo" : tipo,
                    "data" : data,
                    "hora" : hora,
                    "valor" : valor,
                    "cartao" : cartao,
                    "loja" : nome_da_loja
                })
                if tracao.is_valid():
                    loja_do_arquivo = Loja.objects.get(nome=nome_da_loja)
                    if not loja_do_arquivo.exists():
                        loja_do_arquivo  = LojaForm({
                            "nome_da_loja" : nome_da_loja,
                            "cpf" : cpf,
                            "dono_da_loja" : dono_da_loja
                        })
                        loja_do_arquivo.save()

                    loja_do_arquivo.transacoes.set(tracao)
                    loja_do_arquivo.save()
    return ''
