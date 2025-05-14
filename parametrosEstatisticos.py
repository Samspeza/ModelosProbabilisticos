"""
Estimação de Parâmetros Estatísticos
Resolução dos exemplos e exercícios utilizando o Python
Intervalo de confiança para a média quando  é conhecido
Exemplo 1
(Barbetta, 2004) Em uma indústria de cerveja, a quantidade de cerveja inserida em latas tem-se
comportado como uma variável aleatória distribuída normalmente com média 350 ml e desvio padrão 3 ml.
Após alguns problemas na linha de produção, suspeita-se que houve alteração na média. Uma amostra de 120
latas acusou média 346 ml. Encontre a estimativa pontual e construa um intervalo de confiança para o novo
valor da quantidade média de cerveja inserida em latas, com nível de confiança de 95%, supondo que não tenha
ocorrido alteração no desvio padrão do processo.
Utilizando o Pyhton:
"""

from scipy.stats import norm
import numpy as np
# Parâmetros do problema
media_amostral = 346 # média da amostra
desvio_padrao_populacional = 3 # desvio padrão populacional
tamanho_amostra = 120 # tamanho da amostra
nivel_confianca = 0.95 # nível de confiança
# Calculando a estimativa pontual (média da população)
estimativa_pontual = media_amostral
# Calculando o erro padrão
erro_padrao = desvio_padrao_populacional / np.sqrt(tamanho_amostra)
# Calculando o intervalo de confiança
z_score = norm.ppf((1 + nivel_confianca) / 2) # valor z para o nível de confiança
margem_de_erro = z_score * erro_padrao
intervalo_confianca = (
estimativa_pontual - margem_de_erro,
estimativa_pontual + margem_de_erro,
)
print("Estimativa Pontual:", estimativa_pontual)
print("Valor Crítico (z-score):", z_score)
print("Margem de Erro:", margem_de_erro)
print("Intervalo de Confiança (95%):", intervalo_confianca)

"""
Estimativa Pontual: 346
Valor Crítico (z-score): 1.959963984540054
2
Margem de Erro: 0.5367582431151471
Intervalo de Confiança (95%): (345.4632417568848, 346.5367582431152)
Neste código, estamos calculando a estimativa pontual, o erro padrão e o intervalo de confiança para a
média populacional da quantidade de cerveja em latas. O valor crítico de z é calculado usando a função
norm.ppf() para obter o valor z correspondente ao nível de confiança de 95%. Por fim, imprimimos a estimativa
pontual e o intervalo de confiança.
"""