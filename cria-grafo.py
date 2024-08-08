#aqui será desenvolvido um programa para montar o grafo
import numpy as np
max = 100000
limX3 = int(max/3)
limX2 = int(max/2)
min = 0

def paridade(num:int):
  if(num%2==0):
    return True
  return False

def operacoes(num:int):
  conexoes = []
  if(num<max):
    conexoes.append(num+1)
  if(num>min):
    conexoes.append(num-1)
  if(num != 0):
    if(num<limX2):
      conexoes.append(num*2)
    if(num<limX3):
      conexoes.append(num*3)
    if(paridade(num)):
      conexoes.append(int(num/2))
  return conexoes

def monta_estrutura():
  lista_adjacencias = {}
  for i in range (100001):
    lista_adjacencias.update({
      i: operacoes(i)
    })
  print(lista_adjacencias)
  
def main():
  monta_estrutura()
  
main()