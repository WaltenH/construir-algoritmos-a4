import pandas as pd

def predicao(arquivo)
  dados = pd.read_csv(arquivo)
  area = dados["area_util_m2"].to_list()
  quartos = dados["quantidade_quartos"].to_list()
  preco = dados["preco_venda"].to_list()
  print(f"$area, $quartos, $preco")
  
predicao()
#B0 é o valor inicial
#Este valor de B0 + B1*A e B2*Q 
#B1 e B2 seria o valor de cada m2 na área e o valor de cada quarto?
#?
#?
#?
