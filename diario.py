#! /usr/bin/env python3
#
# Cria arquivo de diário
# Esse programa será disparado diariamente pela crontab no inicio do dia,
# preferencialmente às 00:05:00
# 

import os
import pathlib
from pathlib import Path
import datetime
from datetime import date
import sys

# ----------------------------------------------
#   Nome do programa
#
nome_programa = os.path.basename(sys.argv[0])



agora = datetime.datetime.now()
data_timestamp = agora.strftime('%Y-%m-%d-%H-%M-%S')
data_ano_AAAA  = agora.strftime('%Y')

#---
# Definições para o diário
#
diario_AAAA_MM_DD_TXT=agora.strftime('%Y-%m-%d') + '.txt'
diario_diretorio='/home/wilson/Documentos/usr/wil/Atividades/Diario'
diario_diretorio_AAAA=os.path.join(diario_diretorio, data_ano_AAAA)
diario_arquivo=os.path.join(diario_diretorio_AAAA, diario_AAAA_MM_DD_TXT)
print(diario_diretorio_AAAA)
print(diario_arquivo)

#---
# Verifica se diretório existe
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
# Verifica existencia do arquivo de entrada
#

if Path(diario_arquivo).exists():
    print('arquivo_entrada existe  : ' + str(diario_arquivo))
    exit(9)
else:
    #---
    # Cria o arquivo de diário
    #
    print('arquivo_entrada NÃO existe  : ' + str(diario_arquivo))
    f= open(diario_arquivo,"w+")
    f.write(diario_arquivo)
    f.close()
    exit(0)

#--- fim do arquivo ---#