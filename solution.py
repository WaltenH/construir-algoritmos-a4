import pandas as pd
import numpy as np

def predicao(arquivo):
  dados = pd.read_csv(arquivo)
  area = dados["area_util_m2"].to_list()
  quartos = dados["quantidade_quartos"].to_list()
  preco = dados["preco_venda"].to_list()

  Y = np.array(preco)

  X = np.column_stack((np.ones(len(area)), area, quartos))
  Xt = np.transpose(X)

  XtX = np.dot(Xt, X)
  XtXR = np.linalg.inv(XtX)
  XtY = np.dot(Xt, Y)

  beta = np.dot(XtXR, XtY)

  #aquela balela ali em cima é uma DESCONSTRUÇÃO do B = (Xt * X)-¹ * Xt * Y, devido a
  #sintaxe não dar certo usando np.dot(np.dot(np.linalg.inv)), então eu tive que 
  #desconstruir a conta e fazer uma parte de cada vez
  return beta
  
resultado = predicao("imoveis_lar_perfeito.csv")
print(resultado)
