#!/usr/bin/env python
# coding: utf-8

# # Integração Python e Arquivos XML
# 
# #### Desafio:
# Automatizar a leitura de notas fiscais (.xml) e, a partir das informações coletadas, enviá-las de maneira resumida e organizada para um arquivo Excel (.xlsx)
# 
# Obs.: as notas fiscais DANFE (federal) seguem o mesmo padrão, o qual pode variar para outras notas fiscais (estaduais)

# In[1]:


import xmltodict
import pandas as pd
import os
from pprint import pprint


# ##### 1
# Abrir os arquivos .xml da pasta do computador e transformá-los em dicionário.
# ##### 2
# Pegar as informações desejadas: valor total da nota, produto/serviço, cnpj do vendedor, nome do vendedor, cpf/cnpj do comprador, nome do comprador.
# ##### 3
# Transformar as informações coletadas em dicionário para exportá-lo para um arquivo Excel; ao colocar os valores das chaves do dicionário entre [], o python entende cada valor como lista e, então, exporta o dicionário todo dentro de 1 mesma linha no dataframe.

# In[2]:


#1

local_atual = os.getcwd()
caminho_pasta = fr'{local_atual}\Notas_Fiscais'
lista_arquivos = os.listdir(caminho_pasta)

df_final = pd.DataFrame()

for arquivo in lista_arquivos:
    dash = '-'*50
    print(f'{dash}{arquivo}{dash}')
    
    if 'xml' in arquivo[-3:]:
        arquivo_xml = open(fr'Notas_Fiscais/{arquivo}', 'rb') # 'rb' = read binary (not only text)
        dicionario = xmltodict.parse(arquivo_xml)
        pprint(dicionario)
        
        #2
        
        cpf_cnpj_comprador = dicionario['nfeProc']['NFe']['infNFe']['dest']['CPF']
        nome_comprador = dicionario['nfeProc']['NFe']['infNFe']['dest']['xNome']

        cnpj_vendedor = dicionario['nfeProc']['NFe']['infNFe']['emit']['CNPJ']
        nome_vendedor = dicionario['nfeProc']['NFe']['infNFe']['emit']['xNome']

        lista_produtos_servicos = []
        for item in dicionario['nfeProc']['NFe']['infNFe']['det']:
            p_s = item['prod']['xProd']
            lista_produtos_servicos.append(p_s)

        valor = dicionario['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF']
        
        #3
        
        dicionario_final = {
            'Valor Total': [valor],
            'CNPJ Vendedor': [cnpj_vendedor],
            'Nome Vendedor': [nome_vendedor],
            'CPF/CNPJ Comprador': [cpf_cnpj_comprador],
            'Nome Comprador': [nome_comprador],
            'Lista Produtos/Serviços': [lista_produtos_servicos],
        }
        
        df = pd.DataFrame.from_dict(dicionario_final)
        
        df_final = pd.concat([df_final, df])

df_final.to_excel('Planilha Resumo NFs.xlsx')


# In[36]:


display(df_final)

