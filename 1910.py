#aqui será gerada a solução do problema

def validacoes():
  print()

def leitura_ODK():
  dados = input().split()
  O, D, K = map(int, dados)
  return O, D, K

def leitura_proibidos(K:int):
  dados = input().split()
  proibidos = [int(dado) for dado in dados]
  if(len(proibidos)!=K):
    print("?")
  return proibidos

def criaVisitados():
  visitados = {no: (False, float('inf')) for no in range(100001)}
  return visitados

def impede_proibidos(visitados:dict, proibidos:list):
  infinite = float('inf')
  for no in proibidos:
    visitados[no] = (True, infinite)
  
  return visitados

def bfs(O:int, D:int, visitados:dict):
  return

def main():
  while(True):
    O, D, K = leitura_ODK()
    if(O == 0, O == D, O == K):
      break
    proibidos = leitura_proibidos(K)
    visitados = criaVisitados()
    visitados = impede_proibidos()
    
    
    
  print("-1")

grafo = []

main()