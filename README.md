# PUC MVP-Desenv.Soft.Inteligente - Pós em Engenharia de Software
Projeto Básico Full Stack utilizando um modelo de Machine Learning - MVP Pós-Graduação PUC-Rio

##### Link do modelo no Google Colab:
https://colab.research.google.com/github/NetoEu/PUC-MVP-Desenv.-Soft.-Inteligente/blob/main/machineLearning/notebook/churn_rate.ipynb#scrollTo=12_U4YNRsAla

## API Bank Churn
Este projeto faz parte da disciplina Qualidade de Software, Segurança e Sistemas Inteligentes do curso de pós-graduação em Engenharia de Software da PUC-RIO.

O objetivo é treinar um modelo de machine learning utilizando um dataset escolhido pelo aluno e integrar esse modelo em uma aplicação no padrão MVC, composta por uma API e um front-end.

O dataset escolhido para este projeto refere-se à análise da rotatividade de clientes de um banco. O conjunto de dados contém informações como saldo bancário, número de produtos, balanço e outros dados relevantes para que o modelo de machine learning possa identificar padrões de comportamento.

#### Como executar
Para rodar a aplicação, siga três etapas principais: o treinamento do modelo, o teste de acurácia e a execução da aplicação.

#### Passo 1: Treinamento do modelo
Antes de começar, certifique-se de ter instaladas todas as bibliotecas Python listadas no arquivo requirements.txt.

Após clonar o repositório, acesse o diretório raiz pelo terminal para executar os comandos descritos a seguir.

Recomenda-se fortemente o uso de ambientes virtuais como virtualenv.

Para criar o ambiente virtual, execute o comando:

python3 -m venv env

Para ativar o ambiente virtual, execute:

source env/bin/activate

Em seguida, instale as dependências listadas em requirements.txt com o comando:

(env)$ pip install -r requirements.txt

Com o ambiente configurado, prossiga para o treinamento do modelo. O código de treinamento está em um notebook na pasta "Notebook" dentro da pasta "Machine Learning". O caminho é:

./machineLearning/notebook/churn_rate.ipynb

Execute todos os passos descritos no notebook.

##### Nota:
O modelo que apresentou os melhores resultados foi o XGBClassifier, escolhido para este projeto após a comparação com outros modelos. A otimização de hiperparâmetros foi realizada para todos os modelos testados, porém o foco final foi no modelo selecionado. Execute todo o treinamento e salve o modelo conforme descrito no notebook.

#### Passo 2: Teste de acurácia
Como parte do MVP, foi criado um script de teste para verificar a acurácia do modelo. O arquivo é test_modelos.py. Para testar a acurácia, execute o comando:

pytest -v test_modelos.py

#### Passo 3: Execução da aplicação
Depois de criar o ambiente virtual, instalar as dependências, treinar o modelo e testar sua acurácia, você pode rodar a aplicação com o seguinte comando:

(env)$ flask run --host 0.0.0.0 --port 5000

Abra o endereço http://localhost:5000/#/ no navegador para verificar o status da API. O Swagger será carregado automaticamente, permitindo o acesso à documentação das APIs.

#### Funcionamento do Back-end
O back-end utiliza um banco de dados SQLite3 com uma tabela chamada 'clientes', onde são armazenadas as informações dos clientes analisados e os resultados das análises.

As operações de leitura e escrita no banco de dados são acessadas por rotas definidas no arquivo principal do código (app.py). As rotas disponíveis são:

- get clientes: Retorna uma listagem de todos os clientes cadastrados no banco;
- get cliente: Busca um cliente pelo nome (anteriormente utilizava-se o ID, mas neste projeto o nome foi escolhido para simplificar o código);
- post cliente: Adiciona um novo cliente e a respectiva análise de churn ao banco de dados;
- delete cliente: Exclui um cliente com base no nome.

Essas funcionalidades permitem que a API faça a gestão dos dados e dos resultados das análises preditivas.

#### Funcionamento do Back-end