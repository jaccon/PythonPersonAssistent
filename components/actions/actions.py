import os

def listen(req):
    if req == 'listadecomandos':
        print ('')
        print ("Lista de ações:")
        print ('')
        print ("digadata: fala a data e hora atual")
        print ("limparlixeira: limpa a lixeira do mac")
        print ("abrirfinder: abre o finder do mac")
    elif req == 'digadata':
        os.system('tput clear')
        print ('A data atual é')
