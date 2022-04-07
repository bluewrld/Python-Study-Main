# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('o site Pudim não está acessível no momento.')
else:
    print('consegui acessar o site Pudim com sucesso!')