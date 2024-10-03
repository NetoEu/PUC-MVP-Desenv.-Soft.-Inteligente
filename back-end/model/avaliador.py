from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.model import Modelo

class Avaliador:

    def avaliar(model, x_test, y_test):
        """ 
            Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
            avaliação, entre outros.
        """
        predicoes = Modelo.realiza_predicao(model, x_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(y_test, predicoes)