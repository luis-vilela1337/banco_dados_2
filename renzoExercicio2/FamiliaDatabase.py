class FamiliaDatabase:
    def __init__(self, database):
        self.db = database

    def get_engenheiros(self):
        query = "MATCH (p:Person:Engineer) RETURN p.name AS nome_engenheiro"
        results = self.db.execute_query(query)
        return [result["nome_engenheiro"] for result in results]

    def get_filhas_de_sebastiao(self):
        query = "MATCH (p1:Person)-[:FILHA_DE]->(p2:Person {name: 'Sebastião Vilela'}) RETURN p1.name AS filhas"
        results = self.db.execute_query(query)
        return [result["filhas"] for result in results]

    def get_cachorros(self):
        query = "MATCH (p1:Person)-[:DONO_DE]->(p2:Dog) RETURN p2.name AS nome_cachorro"
        results = self.db.execute_query(query)
        return [result["nome_cachorro"] for result in results]
