# Módulo para interação com o banco de dados
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://andriwrsuperbi:Leumas9819@cluster0.iu5jk2p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = cluster["gestor_de_vendas"]

collection = db["clientes"]


#add
post = {"_id": 0, "nome": "João", "cpf": "000.000.000-00"}

collection.insert_one(post)

#mongodb+srv://andriwrsuperbi:Leumas9819@cluster0.iu5jk2p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0