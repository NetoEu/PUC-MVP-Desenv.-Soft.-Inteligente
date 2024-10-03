from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Modelo()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./machineLearning/data/data_train_test/test_dataset_bankChurn.csv"
colunas = ['credit_score', 
           'age', 
           'tenure', 
           'balance', 
           'products_number', 
           'credit_card', 
           'active_member', 
           'estimated_salary', 
           'country_France',
           'country_Germany',
           'country_Spain',
           'gender_Female',
           'gender_Male',
           'churn']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
x = array[:,0:-1]
y = array[:,-1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"

# def test_modelo_lr():  
#     # Importando o modelo de regressão logística
#     lr_path = './machineLearning/models/diabetes_lr.pkl'
#     modelo_lr = Modelo.carrega_modelo(lr_path)

#     # Obtendo as métricas da Regressão Logística
#     acuracia_lr = Avaliador.avaliar(modelo_lr, X, y)
    
#     # Testando as métricas da Regressão Logística 
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_lr >= 0.78 
#     # assert recall_lr >= 0.5 
#     # assert precisao_lr >= 0.5 
#     # assert f1_lr >= 0.5 
 
# Método para testar modelo KNN a partir do arquivo correspondente

# def test_modelo_knn():
#     # Importando modelo de KNN
#     knn_path = './MachineLearning/models/diabetes_knn.pkl'
#     modelo_knn = Modelo.carrega_modelo(knn_path)

#     # Obtendo as métricas do KNN
#     acuracia_knn = Avaliador.avaliar(modelo_knn, X, y)
    
#     # Testando as métricas do KNN
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_knn >= 0.78
#     # assert recall_knn >= 0.5 
#     # assert precisao_knn >= 0.5 
#     # assert f1_knn >= 0.5 
    
# Método para testar pipeline XGBClassifier a partir do arquivo correspondente
def test_modelo_xgb():
    # Importando pipeline de XGBClassifier
    xgb_path = './machineLearning/pipelines/xgb_bankChurn.pkl'
    modelo_rf = Pipeline.carrega_pipeline(xgb_path)

    # Obtendo as métricas do XGBClassifier
    acuracia_xgb = Avaliador.avaliar(modelo_rf, x, y)
    
    # Testando as métricas do XGBClassifier
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_xgb >= 0.78
    # assert recall_rf >= 0.5 
    # assert precisao_rf >= 0.5 
    # assert f1_rf >= 0.5