from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente
import json
import numpy as np

class ClienteSchema(BaseModel):
    """ 
        Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Maria"
    credit_score: int = 600
    age: int = 26
    tenure: int = 3
    balance: float = 35000
    products_number: int = 2
    credit_card: int = 1
    active_member: float = 0.627
    estimated_salary: float = 5005
    country_France: int = 1
    country_Germany: int = 0
    country_Spain: int = 0
    gender_Female: int = 1
    gender_Male: int = 0
    
class ClienteViewSchema(BaseModel):
    """
        Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Maria"
    credit_score: int = 600
    age: int = 26
    tenure: int = 3
    balance: float = 35000
    products_number: int = 2
    credit_card: int = 1
    active_member: float = 0.627
    estimated_salary: float = 5005
    country_France: int = 1
    country_Germany: int = 0
    country_Spain: int = 0
    gender_Female: int = 1
    gender_Male: int = 0
    churn: int = None
    
class ClienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"

class ListaClienteSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[ClienteSchema]

    
class ClienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um paciente    
def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": cliente.id,
        "name": cliente.name,
        "credit_score": cliente.credit_score,
        "age": cliente.age,
        "tenure": cliente.tenure,
        "balance": cliente.balance,
        "products_number": cliente.produtcs_number,
        "credit_card": cliente.credit_card,
        "active_member": cliente.active_member,
        "estimated_salary": cliente.estimated_salary,
        "country_France": cliente.country_France,
        "country_Germany": cliente.country_Germany,
        "country_Spain": cliente.country_Spain,
        "gender_Female": cliente.gender_Female,
        "gender_Male": cliente.gender_Male,
        "churn": cliente.churn
    }
    
# Apresenta uma lista de pacientes
def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
                "id": cliente.id,
                "name": cliente.name,
                "credit_score": cliente.credit_score,
                "age": cliente.age,
                "tenure": cliente.tenure,
                "balance": cliente.balance,
                "products_number": cliente.produtcs_number,
                "credit_card": cliente.credit_card,
                "active_member": cliente.active_member,
                "estimated_salary": cliente.estimated_salary,
                "country_France": cliente.country_France,
                "country_Germany": cliente.country_Germany,
                "country_Spain": cliente.country_Spain,
                "gender_Female": cliente.gender_Female,
                "gender_Male": cliente.gender_Male,
                "churn": cliente.churn
        })

    return {"clientes": result}