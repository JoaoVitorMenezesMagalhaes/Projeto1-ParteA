import json
from pathlib import Path

def extract_route(request):
    extract = request.split()[1]
    return extract[1:]  

#def read_file1(args):
#    lista_args = args.split('.')
#    if lista_args[1] in ['.txt', '.html', '.css', '.js']:
#        filepath = open(args, "r")
#    else:
#        filepath = open(args, "rb")
#    return filepath.read

def read_file(args):
    if args.suffix in ['.txt', '.html', '.css', '.js']:
        mode = 'r'
    else:
        mode = 'rb'

    with open(args, mode=mode) as file:
        return file.read()

def load_data(path):
    with open('data/{}'.format(path), 'r') as arquivo:
        conteudo = arquivo.read()
    return json.loads(conteudo)

def load_template(caminho):
    with open ('templates/' + caminho, "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def adiciona_dicionario(anotacao):
    carrega = load_data('notes.json')
    carrega.append(anotacao)
    with open('data/notes.json', 'w') as new_notes:
        anotacao = json.dump(carrega)
        new_notes.write(anotacao)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        headers=f"\n{headers}"
    response = f"HTTP/1.1 {code} {reason}{headers}\n\n{body}".encode()
    return response

def delete(body, database):
    corpo_split = body.split('=')
    if corpo_split[0] == 'deleteNote':
        database.delete(corpo_split[1])
        return True