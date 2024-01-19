#! /usr/bin/env python3
#--------------------------------------------------------------------------------#
#  __  __   _   _   _               __      _____   _                            #
# |  \/  | (_) | | | |             / _|    / ____| | |                           #
# | \  / |  _  | | | | __     ___ | |_    | (___   | |_    ___    _ __     ___   #
# | |\/| | | | | | | |/ /    / _ \|  _|    \___ \  | __|  / _ \  | '_ \   / _ \  #
# | |  | | | | | | |   <    | (_) | |      ____) | | |_  | (_) | | | | | |  __/  #
# |_|  |_| |_| |_| |_|\_\    \___/|_|     |_____/   \__|  \___/  |_| |_|  \___|  #
#                                                                                #
#--------------------------------------------------------------------------------#
#                                                                                #
#          MilkofStone Prospecção de Dados e Tecnologia Ltda.                    #
#                                                                                #
#                         https://milkofstone.com                                #
#                                                                                #
#--------------------------------------------------------------------------------#
# Versão:                                                                        #
#     7.0                                                                        #
#                                                                                #
# Infraestrutura:                                                                #
#     Python 3.5                                                                 #
#                                                                                #
# Descrição:                                                                     #
#     Esse programa orquestra a todas as fases do sistema                        #
#                                                                                #
# Dependencias:                                                                  #
#     import sys                                                                 #
#        └── Nativo Python 3.5                                                   #
#     import os                                                                  #
#         └── Nativo Python 3.5                                                  #
#     import subprocess                                                          #
#         └── Nativo Python 3.5                                                  #
#     import datetime                                                            #
#         └── Nativo Python 3.5                                                  #
#     import logging                                                             #
#         └── Nativo Python 3.5                                                  #
#     import traceback                                                           #
#         └── Nativo Python 3.5                                                  #
#                                                                                #
#     [ARGV]:                                                                    #
#          [SEM]                                                                 #
#                                                                                #
# Observaçoes de uso:                                                            #
#                                                                                #
# Diário em editor de texto                                                      #
# 
# Esse tem o proposito de abrir um editor de texto simples, editando
# um arquivo texto, cujo nome corresponde ao dia corrente.      
#--------------------------------------------------------------------------------#
# Execução:                                                                      #
#     /usr/bin/python3 [Programa]                                                #
#--------------------------------------------------------------------------------#
# Autor: Wilson Nunes - wilson@milkofstone.com                                   #
# Data criação: 24/10/2023                                                       #
#--------------------------------------------------------------------------------#
# 

import  os
import  subprocess
import  pathlib
from    pathlib     import Path
import  datetime
from    datetime    import date
import  sys

# ----------------------------------------------
#   Obtem o nome do programa
#
nome_programa = os.path.basename(sys.argv[0])



agora = datetime.datetime.now()
data_timestamp = agora.strftime('%Y-%m-%d-%H-%M-%S')
data_ano_AAAA  = agora.strftime('%Y')

#---
# Definições para o arquivo de diário
#

#---
# Data atual para definição do nome de arquivo do diário
diario_AAAA_MM_DD_TXT=agora.strftime('%Y-%m-%d') + '.txt'

#---
# Diretório base para armazenamento dos arquivos de diário
diario_diretorio='/home/wilson/Documentos/usr/wil/Atividades/Diario'

#---
# Śub-diretório para o ano corrente
diario_diretorio_AAAA=os.path.join(diario_diretorio, data_ano_AAAA)

#---
# Nome completo do do arquivo de diário.
diario_arquivo=os.path.join(diario_diretorio_AAAA, diario_AAAA_MM_DD_TXT)
###print(diario_diretorio_AAAA)
###print(diario_arquivo)

#---
# Meu editor de texto
#
# O argumento '--new-window' serve para o sublime abrir uma nova janela,
# específica para o arquivo de diário.
# 

meu_editor_de_texto = '/opt/sublime_text/sublime_text --new-window '

#---
# Cria o diretório com o ano corrente, caso não exista.
#

if Path(diario_diretorio_AAAA).exists():
    print('Diretório existe: ' + str(diario_diretorio_AAAA))
else:
    print('Diretório será criado: ' + str(diario_diretorio_AAAA))
    try:
        Path(diario_diretorio_AAAA).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(e.errno)
        print(e)

#---
# Cria o arquivo de diário, caso não exista.
#

if Path(diario_arquivo).exists():
    print('arquivo_entrada existe  : ' + str(diario_arquivo))
    ###exit(9)
else:
    #---
    # Cria o arquivo de diário
    #
    print('arquivo_entrada NÃO existe  : ' + str(diario_arquivo))
    f= open(diario_arquivo,"w+")
    f.write(diario_arquivo)
    f.close()
    ###exit(0)

# ----------------------------------------------
#   Executando o editor de texto passando o arquivo diario como argumento.
#
linha_de_comando =  meu_editor_de_texto  + diario_arquivo

print('Linha de Comando: ' + linha_de_comando)

Codigo_de_Retorno = subprocess.run(linha_de_comando, shell=True, stdout=subprocess.PIPE)
if Codigo_de_Retorno.returncode == 0:
    print('Execucao bem sucedida, Codigo_de_Retorno.returncode: %s' % Codigo_de_Retorno.returncode)
else:
    print('Execucao mal sucedida, Codigo_de_Retorno.returncode: %s' % Codigo_de_Retorno.returncode)

#--- fim do arquivo ---#    