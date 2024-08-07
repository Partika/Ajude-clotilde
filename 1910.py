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

def main():
  while(True):
    O, D, K = leitura_ODK()
    proibidos = leitura_proibidos(K)
    if(O == 0, O == D, O == K):
      break
    
  print("-1")

grafo = []

main()