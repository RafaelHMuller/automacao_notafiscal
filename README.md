<h1 align="center">
📄<br>README - Projeto Automação Notas Fiscais
</h1>

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Implantação](#implantação)
* [Bibliotecas](#bibliotecas)

# Descrição do projeto
> Este repositório é meu projeto Python de automação de notas fiscais. O objetivo é, a partir de arquivos de uma DANFE (Documento Auxiliar da Nota
Fiscal Eletrônica) na extensão xml, por meio de análise de dados, criar um dataframe e exportá-lo como planilha excel somente com as informações de interesse.

# Funcionalidades e Demonstração da Aplicação
Criação de planilha excel com as informações de interesse coletadas a partir de notas fiscais.

Nota fiscal usada na automação:<br>
![Screenshot_1](https://user-images.githubusercontent.com/128300382/227984213-5b7e12ff-40a7-4cfc-94c9-548331581509.png)

Planilha excel criada:<br>
![Screenshot_2](https://user-images.githubusercontent.com/128300382/227984284-d750e504-01c0-462c-8f5d-b8d36edb9cef.png)


## Pré requisitos

* Sistema operacional Windows
* IDE de python (ambiente de desenvolvimento integrado de python)
* Microsoft Office (Excel)
* Arquivo DANFE na extensão xml (Documento Auxiliar da Nota Fiscal Eletrônica)

## Execução

Na execução deste código, as notas fiscais (.xml) que constam na pasta 'Notas_Fiscais', dentro do diretório no qual está o arquivo Python, serão integradas ao código e, a partir de análise de dados, algumas informações relevantes serão inseridas em um dataframe e, então, este será exportado como planilha Excel (.xlsx).

## Implantação

É possível adaptar este projeto a qualquer nota fiscal DANFE na extensão xml, desde que seja uma nota fiscal federal, uma vez que notas ficais estaduais podem ter formatação e organização diferentes.

## Bibliotecas

* <strong>xmltodict:</strong> biblioteca de integração de arquivo xml, transformando este arquivo em um dicionário Python<br>
* <strong>pandas:</strong> bibliotecas de integração de arquivos excel, csv e outros, possibilitando análise de dados<br>
* <strong>os:</strong> bibliotecas de integração de pastas e arquivos do computador<br>
* <strong>pprint:</strong> bibliotecas que permite uma leitura (display) mais organizada de dicionários complexos<br>
