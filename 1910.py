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
  visitados[O] = (True, 0)
  
  fila = [O]
  
  while fila:
    no_atual = fila.pop()
    visitado, distancia = visitados[no_atual]
    
    for canal in grafo[no_atual]:
      if(canal == D):
        visitados[canal] = (True, distancia + 1)
        return visitados[D]
      
      foi_visitado, _ = visitados[canal]
      if(not foi_visitado):
        visitados[canal] = (True, distancia + 1)
        fila.append[canal]
        
  return (False, -1)

def main():
  while(True):
    O, D, K = leitura_ODK()
    if(O == 0, O == D, O == K):
      break
    proibidos = leitura_proibidos(K)
    visitados = criaVisitados()
    visitados = impede_proibidos(proibidos)
    _, resultado = bfs(O, D, visitados)
    print(resultado)

grafo = []

main()