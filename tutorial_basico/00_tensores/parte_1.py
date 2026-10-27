# Instalado o Pytorch
'''
- Para instalar o Pytorch execute os comando:
	pip3 install torch torchvision
- Esse comando irá instalar o ***Pytorch*** e o ***torhvision***
	- torch é o framework principal do Pytorch
	- torchvision é framework de visão computacional
'''
 
# Para saber se  código funcionou execute:
# Irá criar um tensor de 5 linhas e 3 colunas com valor entre 0 e 1

import torch
x = torch.rand(5, 3)
print(x)


