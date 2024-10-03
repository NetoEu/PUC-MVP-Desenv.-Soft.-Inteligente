from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessador:

    # def separa_teste_treino(self, dataset, percentual_teste, seed=7):
    #     """ Cuida de todo o pré-processamento. """
    #     # limpeza dos dados e eliminação de outliers

    #     # feature selection

    #     # divisão em treino e teste
    #     x_train, x_test, y_train, y_test = self.__preparar_holdout(dataset,
    #                                                               percentual_teste,
    #                                                               seed)
    #     # normalização/padronização
        
    #     return (x_train, x_test, y_train, y_test)
    
    # def __preparar_holdout(self, dataset, percentual_teste, seed):
    #     """ Divide os dados em treino e teste usando o método holdout.
    #     Assume que a variável target está na última coluna.
    #     O parâmetro test_size é o percentual de dados de teste.
    #     """
    #     dados = dataset.values
    #     x = dados[:, 0:-1]
    #     y = dados[:, -1]
    #     return train_test_split(x, y, test_size=percentual_teste, random_state=seed)
    
    def preparar_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """


        # # Variáveis categóricas (One-Hot Encoding)
        # gender_Female = int(form.gender == 0)
        # gender_Male = int(form.gender == 1)
        # country_France = int(form.country_France == 1)
        # country_Germany = int(form.country_Germany == 1)
        # country_Spain = int(form.country_Spain == 1)


        x_input = np.array([form.credit_score, 
                            form.age, 
                            form.tenure, 
                            form.balance, 
                            form.products_number, 
                            form.credit_card, 
                            form.active_member, 
                            form.estimated_salary,
                            form.country_France,
                            form.country_Germany,
                            form.country_Spain,
                            form.gender_Female,
                            form.gender_Male
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando uma unica amostra
        x_input = x_input.reshape(1, -1)
        return x_input
    
    # def scaler(x_train):
    #     """ Normaliza os dados. """
    #     # normalização/padronização
    #     scaler = pickle.load(open(r'C:\Users\Notbook\Desktop\PUC\Eng. Software\MVP\MVP - Qualidade de Software e Sistemas Inteligentes\machineLearning\scalers\std_bankChurn.pkl', 'rb'))
    #     reescaled_x_train = scaler.transform(x_train)
    #     return reescaled_x_train