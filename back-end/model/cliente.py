from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Credit Score,Age,Tenure,Balance,
# Products Number,Credit Card,Active Member,
# Estimated Salary, country France, country Germany, 
# country Spain,gender Female,gender Male, churn

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    credit_score = Column("CreditScore", Integer)
    age = Column("Age", Integer)
    tenure = Column("Tenure", Integer)
    balance = Column("Balance", Float)
    products_number = Column("ProductsNumber", Integer)
    credit_card = Column("CreditCard", Float)
    active_member = Column("ActiveMember", Integer)
    estimated_salary = Column("EstimatedSalary", Float)
    country_France = Column("CountryFrance", Integer)
    country_Germany = Column("CountryGermany", Integer)
    country_Spain = Column("CountrySpain", Integer)
    gender_Female = Column("GenderFemale", Integer)
    gender_Male = Column("GenderMale", Integer)
    churn = Column("Churn", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now)
    
    def __init__(self, name:str, credit_score:int, age:int, tenure:int, balance:float,
                 products_number:int, credit_card:float, active_member:int, 
                 estimated_salary:float, country_France:int, country_Germany:int,
                 country_Spain:int, gender_Female:int, gender_Male:int, churn:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            name: nome do paciente
            credit_score: Pontuação de crédito
            age: idade
            tenure: posses
            balance: saldo bancário
            products_number: numero de produtos
            credit_card: cartão de crédito
            active_member: membro ativo
            estimated_salary: salário estimado
            country_France: França
            country_Germany: Alemanha
            country_Spain: Espanha
            gender_Female: sexo Feminino
            gender_Male: sexo Masculino
            churn: Taxa de rotatividade (saída de clientes)
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name = name
        self.credit_score = credit_score
        self.age = age
        self.tenure = tenure
        self.balance = balance
        self.products_number = products_number
        self.credit_card = credit_card
        self.active_member = active_member
        self.estimated_salary = estimated_salary
        self.country_France = country_France
        self.country_Germany = country_Germany
        self.country_Spain = country_Spain
        self.gender_Female = gender_Female
        self.gender_Male = gender_Male
        self.churn = churn

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao