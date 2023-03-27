<h1 align="center">
📄<br>README - Projeto Automação Cotação Moedas
</h1>

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Implantação](#implantação)
* [Bibliotecas](#bibliotecas)

# Descrição do projeto
> Este repositório é meu projeto Python de automação web e atualização de base de dados. O objetivo é, a partir de web-scrapping, encontrar as cotações atuais de algumas moedas e, então, atualizar uma base de dados de produtos.

# Funcionalidades e Demonstração da Aplicação
Atualização de base de dados (planilha excel) a partir de informações coletadas online.

Cotação atualizada de moedas:<br>
![Screenshot_2](https://user-images.githubusercontent.com/128300382/227036985-da9d05db-ba3c-44ab-8c39-3d23b1d10172.png)

Planilha atualizada:<br>
![Screenshot_1](https://user-images.githubusercontent.com/128300382/227035885-b6df944a-c90e-4061-a142-a524e5d5e96d.png)

## Pré requisitos

* Sistema operacional Windows
* IDE de python (ambiente de desenvolvimento integrado de python)
* Google Chrome
* Base de dados (planilha excel)

## Execução

Na execução deste código, devido ao modo headless da biblioteca selenium, pode-se utilizar livremente o mouse e teclado, bem como o próprio navegador durante a automação.

## Implantação

É possível adaptar este projeto a qualquer base de dados de produtos/serviços cujo valor de compra/venda dependa das cotações atualizadas de quaisquer moedas.

## Bibliotecas

* selenium: biblioteca de automação web
* webdriver_manager.chrome: biblioteca que atualiza o drive do Google Chrome
* pandas: biblioteca que permite, no caso, a integração de arquivo excel
