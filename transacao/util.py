from .form import TrasacaoForm
from loja.models import Loja
from loja.form import LojaForm
def processFile(pathName):

    with open(str(pathName), 'r', encoding="utf-8") as arquivo:
        lines = arquivo.readlines()
        for line in lines:
            if len(line)==81:
                tipo = line[0]
                data = f'{line[7:9]}.{line[5:7]}.{line[1:5]}'
                valor = int(line[9:19])/100
                cpf = f'{line[19:22]}.{line[22:25]}.{line[25:28]}-{line[28:30]}'
                cartao = f'{line[30:34]}.{line[34:38]}.{line[38:42]}'
                hora = f'{line[42:44]}:{line[44:46]}:{line[46:48]}'
                dono_da_loja = line[48:62]
                nome_da_loja = line[62:81]

                loja_da_transacao = {}
                try:
                    loja_da_transacao = Loja.objects.get(cpf=cpf)
                except:
                    loja_da_transacao  = LojaForm({
                        "nome" : nome_da_loja,
                        "cpf" : cpf,
                        "dono_da_loja" : dono_da_loja
                    })
                    if loja_da_transacao.is_valid():
                        loja_da_transacao = loja_da_transacao.save()
                trasacao = TrasacaoForm({
                    "tipo" : tipo,
                    "data" : data,
                    "hora" : hora,
                    "valor" : valor,
                    "cartao" : cartao,
                })

                if trasacao.is_valid():
                    # para ver se a operação é de entrada ou saida (Ver: Documentação sobre os tipos das transações)        
                    if tipo in ["2","3","9"]:
                        loja_da_transacao.saldo -= valor
                    else:  
                        loja_da_transacao.saldo += valor 
                    loja_da_transacao.save()

                    trasacao = trasacao.save()
                    trasacao.loja = loja_da_transacao
                    trasacao.save()
    return ''
