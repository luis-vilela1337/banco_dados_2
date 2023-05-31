Questão 1)

MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf;
MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf;
MATCH (c:City) RETURN c.name;
MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number;

Questão 2)
MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1;
MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc DESC LIMIT 1;
MATCH (c:City) RETURN avg(c.population);
MATCH (c:City {cep: '37540-000'}) RETURN replace(c.name, 'a', 'A');
MATCH (t:Teacher) RETURN substring(t.name, 3, 1);


