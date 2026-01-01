"""
CONTANTE = "Variáveis" que não vão mudar. 
Muitas condições no mesmo if. (ruim)
Boas práticas na programação e nao usar muitos if, mas passar as conparações diretamente para uma variável com um nome significativo.

"""

velocidade = 61
local_carro = 100

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # a distância do radar pega


velocidade_carro_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade > RADAR_1:
    print('Velocodade corro passou do radar 1')

if carro_multado_radar_1 and velocidade_carro_radar_1  :
    
    print('O carro multado no radar 1')