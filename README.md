""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""  Projeto de Sistemas Distribuidos de Cadastro de Monografias   ""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                                 
O projeto é composto por:                                         
                                                                  
-Back-end feito em Django e transoformado em API Rest                  
-Banco Local em Postgresql ou Banco em Nuvem Azure (Postgresql)                 
-Front end em vue JS                                                 
                                                                  
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                     Configuração                               ""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                                 
  Para configurar o sistema basta seguir a instrução de instalação do
Back e do Front que se encontra no arquivo README de cada aplicação.
Cada aplicação se encontra na respectiva pasta: Monografia_Back e 
Monografia_Front.                                               

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                       Banco de Dados                           ""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                                  
  Para instalar o Banco local basta seguir o passo a passo do site: 
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-pt

As configurações de banco usados foram:

Nome do Banco: monografias
Usuário: postgres
Senha: adminadmin
hospedagem(local):
Porta(padrão): 5432 

  Caso opte pelo banco em nuvem, basta comentar a configuração do
banco local e descomentar o banco em nuvem, que se encontra no 
arquivo settings.py na pasta app dentro da pasta da Monografia_back.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                      Colaboradores                             ""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  Os colaboradores desse projeto foram os alunos da turma de Sistema
Distribuidos do curso de Sistema de Informação da UFVJM lecionado por
Alexandre Vivas:

-Guilherme Jardim Neves Pereira
-Túliu Alves Cordeiro
-Brenda Pereira de Souza Orlandi
-Lorena Simões de Ávila
-Marcos Vitor Ferraz Lima
