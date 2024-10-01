from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização, remoção e predição de churn")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de pacientes
@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_clientes():
    """Lista todos os pacientes cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os clientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    clientes = session.query(Cliente).all()
    
    if not clientes:
        # Se não houver pacientes
        return {"clientes": []}, 200
    else:
        logger.debug(f"%d pacientes econtrados" % len(clientes))
        print(clientes)
        return apresenta_clientes(clientes), 200
    

# Rota de adição de paciente
@app.post('/paciente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ClienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        name (str): nome do cliente
        credit_score (int): Pontuação de crédito: CreditScore
        age (int): Idade: Age
        tenure (int): Posses: Tenure
        balance (float): saldo bancário: Balance
        products_number (int): Número de produtos do banco: ProductNumber
        credit_card (int): Cartão de Crédito (0 - não ou 1 - sim): CreditCard
        active_member (int): Membro Ativo (0 - não ou 1 - sim): ActiveMember
        estimated_salary (float): Salário Estimado: EstimatedSalary
        country_France: País França: CountryFrance
        country_Germany: País Alemanha: CountryGermany
        country_Spain: País Espanha: CountrySpain
        gender_Female: Sexo Feminino: GenderFemale
        gender_Male: Sexo Masculino: GenderMale
        
    Returns:
        dict: retorna a predição se o cliente é tem tendencia a churn
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    name = form.name,
    credit_score = form.credit_score, 
    age = form.age, 
    tenure = form.tenure, 
    balance = form.balance, 
    products_number = form.products_number, 
    credit_card = form.credit_card, 
    active_member = form.active_member, 
    estimated_salary = form.estimated_salary,
    country_France = form.country_France,
    country_Germany = form.country_Germany,
    country_Spain = form.country_Spain,
    gender_Female = form.gender_Female,
    gender_Male = form.gender_Male
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './machineLearning/pipelines/xgb_bankChurn.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    churn = int(Modelo.preditor(modelo, X_input)[0])
    
    cliente = Cliente(
        name = name,
        credit_score = credit_score,
        age = age,
        tenure = tenure,
        balance = balance,
        products_number = products_number,
        credit_card = credit_card,
        active_member = active_member,
        estimated_salary = estimated_salary,
        country_France = country_France,
        country_Germany = country_Germany,
        country_Spain = country_Spain,
        gender_Female = gender_Female,
        gender_Male = gender_Male,
        churn = churn
    )
    logger.debug(f"Adicionando produto de nome: '{cliente.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se cliente já existe na base
        if session.query(Cliente).filter(Cliente.name == form.name).first():
            error_msg = "Cliente já existente na base :/"
            logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando cliente
        session.add(cliente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado cliente de nome: '{cliente.name}'")
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Rota de busca de cliente por nome
@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):    
    """Faz a busca por um cliente cadastrado na base a partir do nome

    Args:
        nome (str): nome do cliente
        
    Returns:
        dict: representação do cliente e diagnóstico associado
    """
    
    cliente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.name == cliente_nome).first()
    
    if not cliente:
        # se o cliente não foi encontrado
        error_msg = f"Cliente {cliente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{cliente.name}'")
        # retorna a representação do cliente
        return apresenta_cliente(cliente), 200
    
    # Rota de remoção de cliente por nome
@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteBuscaSchema):
    """Remove um cliente cadastrado na base a partir do nome

    Args:
        nome (str): nome do cliente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    cliente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre cliente #{cliente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    cliente = session.query(Cliente).filter(Cliente.name == cliente_nome).first()
    
    if not cliente:
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente '{cliente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(cliente)
        session.commit()
        logger.debug(f"Deletado paciente #{cliente_nome}")
        return {"message": f"Cliente {cliente_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)