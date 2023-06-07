-- GLOBAL SOLUTION: Raízes Solidárias

-- Integrantes:
-- Bruna Menegatti Vienna RM: 96848
-- Kaue Caponero Figueiredo RM: 96466
-- Mariana Santos Fernandes de Sousa RM: 97503

--01: CRIANDO AS TABELAS
CREATE TABLE alimento(
    id_alimento NUMBER(8) CONSTRAINT pk_id_alimento PRIMARY KEY,
    nome_alimento VARCHAR(100) CONSTRAINT uk_nm_alimento UNIQUE CONSTRAINT nn_nm_alimento NOT NULL,
    tempo_colheita NUMBER(9) CONSTRAINT nn_tc_alimento NOT NULL,
    qtd_irrigacao NUMBER(9) CONSTRAINT nn_qtd_irr_alimento NOT NULL,
    preco_alimento NUMBER(9) CONSTRAINT nn_preco_alimento NOT NULL,
    qtd_alimento NUMBER(9) CONSTRAINT nn_qtd_alimento NOT NULL
);

CREATE TABLE plantio(
    id_plantio NUMBER(9) CONSTRAINT pk_id_plantio PRIMARY KEY,
    data_plantio DATE CONSTRAINT nn_dt_plantio NOT NULL,
    espaco_plantio NUMBER(9) CONSTRAINT nn_esp_plantio NOT NULL,
    id_alimento NUMBER(9) CONSTRAINT fk_alm_plantio REFERENCES alimento(id_alimento) CONSTRAINT nn_alm_plantio NOT NULL
);

CREATE TABLE colheita(
    id_colheita NUMBER(9) CONSTRAINT pk_id_colheita PRIMARY KEY,
    data_colheita DATE CONSTRAINT nn_dt_colheita NOT NULL,
    descricao_colheita VARCHAR(200)
);

CREATE TABLE usuario(
    id_usuario NUMBER(9) CONSTRAINT pk_id_usuario PRIMARY KEY,
    cpf_usuario CHAR(14) CONSTRAINT uk_cpf_usuario UNIQUE CONSTRAINT nn_cpf_usuario NOT NULL,
    nome_usuario VARCHAR(250) CONSTRAINT nN_nm_usuario NOT NULL,
    email_usuario VARCHAR(250) CONSTRAINT uk_email_usuario UNIQUE CONSTRAINT nn_email_usuario NOT NULL,
    cel_usuario CHAR(15) CONSTRAINT uk_cel_usuario UNIQUE CONSTRAINT nn_cel_usuario NOT NULL,
    senha_usuario VARCHAR(20) CONSTRAINT nn_sen_usuario NOT NULL,
    status_usuario VARCHAR(20) CONSTRAINT nn_stts_usuario NOT NULL
);

CREATE TABLE voluntario(
    id_usuario NUMBER(9) CONSTRAINT fk_id_voluntario REFERENCES usuario(id_usuario) CONSTRAINT pk_id_voluntario PRIMARY KEY,
    data_registro_voluntario DATE CONSTRAINT nn_dt_voluntario NOT NULL
);

CREATE TABLE doador(
    id_usuario NUMBER(9) CONSTRAINT fk_id_doador REFERENCES usuario(id_usuario) CONSTRAINT pk_id_doador PRIMARY KEY,
    nivel_doador NUMBER(9) CONSTRAINT nn_nvl_doador NOT NULL,
    moedas_doador NUMBER(9) CONSTRAINT nn_md_doador NOT NULL
);

CREATE TABLE receptor(
    id_usuario NUMBER(9) CONSTRAINT fk_id_receptor REFERENCES usuario(id_usuario) CONSTRAINT pk_id_receptor PRIMARY KEY,
    carga_receptor NUMBER(9) CONSTRAINT nn_cargar_receptor NOT NULL,
    endereco_receptor VARCHAR(250) CONSTRAINT nn_end_receptor NOT NULL
);

CREATE TABLE agendamento(
    id_agendamento NUMBER(9) CONSTRAINT pk_id_agendamento PRIMARY KEY,
    data_agendamento DATE CONSTRAINT nn_dt_agendamento NOT NULL,
    turno_agendamento VARCHAR(20) CONSTRAINT nn_trn_agendamento NOT NULL,
    id_usuario NUMBER(9) CONSTRAINT fk_id_usuario_agendamento REFERENCES usuario(id_usuario) CONSTRAINT nn_id_usuario_agendamento NOT NULL
);

CREATE TABLE doacao(
    id_doacao NUMBER(9) CONSTRAINT pk_id_doacao PRIMARY KEY,
    id_usuario NUMBER(9) CONSTRAINT fk_id_usuario_doacao REFERENCES doador(id_usuario) CONSTRAINT nn_id_usuario_doacao NOT NULL,
    data_doacao DATE CONSTRAINT nn_dt_doacao NOT NULL,
    qtd_moedas_doacao NUMBER(9) CONSTRAINT nn_moedas_doacao NOT NULL
);

CREATE TABLE destino(
    id_destino NUMBER(9) CONSTRAINT pk_id_destino PRIMARY KEY,
    endereco_destino VARCHAR(250) CONSTRAINT nn_end_destino NOT NULL,
    responsavel_destino VARCHAR(250) CONSTRAINT nn_resp_destino NOT NULL,
    cel_destino CHAR(15) CONSTRAINT nn_cel_destino NOT NULL,
    qtd_dependentes_destino NUMBER(9) CONSTRAINT nn_dep_destino NOT NULL
);

CREATE TABLE receptor_destino(
    id_usuario NUMBER(9) CONSTRAINT fk_id_receptor_destino REFERENCES receptor(id_usuario) CONSTRAINT nn_id_receptor_destino NOT NULL,
    id_destino NUMBER(9) CONSTRAINT fk_id_destino_receptor REFERENCES destino(id_destino) CONSTRAINT nn_id_destino_receptor NOT NULL
);

CREATE TABLE plantio_voluntario(
    id_plantio NUMBER(9) CONSTRAINT fk_id_plantio_voluntario REFERENCES plantio(id_plantio) CONSTRAINT nn_id_plantio_voluntario NOT NULL,
    id_usuario NUMBER(9) CONSTRAINT fk_id_voluntario_plantio REFERENCES voluntario(id_usuario) CONSTRAINT nn_id_voluntario_plantio NOT NULL
);

CREATE TABLE plantio_colheita(
    id_plantio NUMBER(9) CONSTRAINT fk_id_plantio_colheita REFERENCES plantio(id_plantio) CONSTRAINT nn_id_plantio_colheita NOT NULL,
    id_colheita NUMBER(9) CONSTRAINT fk_id_colheita_plantio REFERENCES colheita(id_colheita) CONSTRAINT nn_id_colheita_plantio NOT NULL
);

CREATE TABLE colheita_voluntario(
    id_colheita NUMBER(9) CONSTRAINT fk_id_colheita_voluntario REFERENCES colheita(id_colheita) CONSTRAINT nn_id_colheita_voluntario NOT NULL,
    id_usuario NUMBER(9) CONSTRAINT fk_id_voluntario_colheita REFERENCES voluntario(id_usuario) CONSTRAINT nn_id_voluntario_colheita NOT NULL
);


--02: INSERTS
INSERT INTO alimento VALUES (001, 'alface', 21, 2, 5, 100);
INSERT INTO alimento VALUES (002, 'tomate', 28, 8, 8, 220);
INSERT INTO alimento VALUES (003, 'cenoura', 22, 5, 7, 264);
INSERT INTO alimento VALUES (004, 'pepino', 35, 3, 4, 252);
INSERT INTO alimento VALUES (005, 'rabanete', 14, 4, 3, 173);
INSERT INTO alimento VALUES (006, 'beterraba', 23, 7, 5, 355);
INSERT INTO alimento VALUES (007, 'rucula', 21, 8, 4, 433);
INSERT INTO alimento VALUES (008, 'agriao', 21, 3, 5, 231);
INSERT INTO alimento VALUES (009, 'mandioca', 12, 6, 7, 311);
INSERT INTO alimento VALUES (010, 'batata', 17, 2, 9, 291);


INSERT INTO plantio VALUES (1, '10-mai-20', 1, 1);
INSERT INTO plantio VALUES (2, '14-jun-20', 2, 2);
INSERT INTO plantio VALUES (3, '26-jun-20', 3, 2);
INSERT INTO plantio VALUES (4, '30-jun-20', 4, 3);
INSERT INTO plantio VALUES (5, '04-jul-20', 5, 1);
INSERT INTO plantio VALUES (6, '09-jul-20', 6, 4);
INSERT INTO plantio VALUES (7, '01-ago-20', 7, 2);
INSERT INTO plantio VALUES (8, '16-ago-20', 8, 5);
INSERT INTO plantio VALUES (9, '21-ago-20', 9, 6);
INSERT INTO plantio VALUES (10, '30-ago-20', 10, 7);


INSERT INTO colheita VALUES (1, '02-out-20', 'Alface com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (2, '12-out-20', 'Tomate com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (3, '20-out-20', 'Cenoura com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (4, '02-nov-20', 'Pepino com controle de pragas, aproveitamento parcial');
INSERT INTO colheita VALUES (5, '16-nov-20', 'Rabanete com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (6, '28-nov-20', 'Beterraba com controle de pragas, aproveitamento parcial');
INSERT INTO colheita VALUES (7, '01-jan-21', 'Rucula com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (8, '04-jan-21', 'Agriao com controle de pragas, aproveitamento parcial');
INSERT INTO colheita VALUES (9, '12-jan-21', 'Mandioca com controle de pragas e bom aproveitamento até o momento');
INSERT INTO colheita VALUES (10, '19-jan-21', 'Batata com controle de pragas, aproveitamento parcial');


INSERT INTO usuario VALUES (1, '405.241.587-44', 'Mariana', 'mariana@mari.com', '(11) 98457-6251', 'mari123', 'ativo');
INSERT INTO usuario VALUES (2, '458.746.528-77', 'Thiago', 'thiago@thi.com', '(11) 9587-4254', 'thithi321', 'ativo');
INSERT INTO usuario VALUES (3, '325.874.569-85', 'Sabrina', 'sabrina@sasa.com', '(11) 98354-1289', 'sabABC', 'ativo');
INSERT INTO usuario VALUES (4, '254.158.749-88', 'Ricardo', 'ricardo@ric.com', '(11) 95872-4154', 'ricardin000', 'ativo');
INSERT INTO usuario VALUES (5, '354.251.487-55', 'Joana', 'joana@jojo.com', '(11) 95587-4963', 'jojoAAA', 'ativo');
INSERT INTO usuario VALUES (6, '698.574.857-48', 'Kaue', 'kaue@kako.com', '(11) 96985-7458', '%kako%', 'ativo');
INSERT INTO usuario VALUES (7, '325.145.254-12', 'Leticia', 'let@lele.com', '(11) 9587-4211' , '@let12@', 'inativo');
INSERT INTO usuario VALUES (8, '689.578.475-80', 'Mario', 'mario@marin.com', '(11) 96586-6587', 'marin012', 'ativo');
INSERT INTO usuario VALUES (9, '356.985.624-55', 'Bruna', 'bruna@bru.com', '(11) 9869-8557', 'brubru', 'ativo');
INSERT INTO usuario VALUES (10, '201.545.878-58', 'Bruno', 'brunin@bruno.com', '(11) 98744-4592', 'brunoABC', 'ativo');
INSERT INTO usuario VALUES (11, '405.141.587-24', 'Marina', 'mari@mari.com', '(11) 98457-6221', 'ma333', 'ativo');
INSERT INTO usuario VALUES (12, '458.346.528-17', 'Thales', 'thales@tha.com', '(11) 95874-1154', 'thales321', 'ativo');
INSERT INTO usuario VALUES (13, '325.474.569-15', 'Sansao', 'sansao@sasa.com', '(11) 98322-1289', 'sasaABC', 'inativo');
INSERT INTO usuario VALUES (14, '254.758.749-58', 'Richard', 'rich@rich.com', '(11) 95873-3154', 'richard400', 'ativo');
INSERT INTO usuario VALUES (15, '354.751.487-65', 'Juliana', 'juli@juju.com', '(11) 95447-4963', 'jujuAAA', 'ativo');
INSERT INTO usuario VALUES (16, '698.674.857-78', 'Karine', 'kaka@karine.com', '(11) 95874-4789', '%kaka', 'inativo');
INSERT INTO usuario VALUES (17, '325.545.254-82', 'Larissa', 'lari@lala.com', '(11) 9587-4771', '@larisss', 'ativo');
INSERT INTO usuario VALUES (18, '689.478.475-90', 'Marco', 'marco@marquin.com', '(11) 96557-4587', 'marc012', 'ativo');
INSERT INTO usuario VALUES (19, '356.485.624-05', 'Brenda', 'brenda@bru.com', '(11) 9869-8587', '*brendinha!', 'ativo');
INSERT INTO usuario VALUES (20, '201.245.878-78', 'Breno', 'breno@bre.com', '(11) 98747-7592', 'breno222', 'inativo');


INSERT INTO voluntario VALUES (1, '01-jan-19');
INSERT INTO voluntario VALUES (2, '04-jan-19');
INSERT INTO voluntario VALUES (3, '12-jan-19');
INSERT INTO voluntario VALUES (4, '25-jan-19');
INSERT INTO voluntario VALUES (5, '30-jan-19');
INSERT INTO voluntario VALUES (16, '09-fev-19');
INSERT INTO voluntario VALUES (17, '13-fev-19');
INSERT INTO voluntario VALUES (18, '22-fev-19');
INSERT INTO voluntario VALUES (19, '02-mar-19');
INSERT INTO voluntario VALUES (20, '19-mar-19');


INSERT INTO doador VALUES (2, 1, 120);
INSERT INTO doador VALUES (5, 0, 89);
INSERT INTO doador VALUES (6, 1, 103);
INSERT INTO doador VALUES (8, 2, 303);
INSERT INTO doador VALUES (12, 1, 103);
INSERT INTO doador VALUES (14, 0, 103);
INSERT INTO doador VALUES (15, 2, 356);
INSERT INTO doador VALUES (17, 1, 103);
INSERT INTO doador VALUES (19, 2, 400);
INSERT INTO doador VALUES (20, 0, 443);


INSERT INTO receptor VALUES (1, 50, 'Av. Nações Unidas, 200');
INSERT INTO receptor VALUES (3, 30, 'Av. Faria Lima, 190');
INSERT INTO receptor VALUES (4, 22, 'Av. Lacerda Frango, 22');
INSERT INTO receptor VALUES (7, 12, 'Av. Lins de Vasconcelos, 938');
INSERT INTO receptor VALUES (9, 45, 'Rua Paulo Orizombo, 111');
INSERT INTO receptor VALUES (10, 23, 'Avenia Paulista, 225');
INSERT INTO receptor VALUES (11, 12, 'Rua Pereira Barreto, 32');
INSERT INTO receptor VALUES (13, 53, 'Rua Independência, 93');
INSERT INTO receptor VALUES (16, 31, 'Rua Mesquita, 65');
INSERT INTO receptor VALUES (18, 28, 'Rua Inglês de Souza, 59');


INSERT INTO agendamento VALUES (1, '11-jan-23', 'Manhã', 1);
INSERT INTO agendamento VALUES (2, '11-jan-23', 'Tarde', 3);
INSERT INTO agendamento VALUES (3, '11-jan-23', 'Manhã', 5);
INSERT INTO agendamento VALUES (4, '10-fev-23', 'Manhã', 2);
INSERT INTO agendamento VALUES (5, '10-fev-23', 'Tarde', 4);
INSERT INTO agendamento VALUES (6, '10-fev-23', 'Manhã', 16);
INSERT INTO agendamento VALUES (7, '11-mar-23', 'Manhã', 17);
INSERT INTO agendamento VALUES (8, '11-mar-23', 'Tarde', 18);
INSERT INTO agendamento VALUES (9, '11-mar-23', 'Manhã', 19);
INSERT INTO agendamento VALUES (10, '12-jun-23', 'Manhã', 20);


INSERT INTO doacao VALUES (1, 2, '20-fev-23', 30);
INSERT INTO doacao VALUES (2, 5, '20-fev-23', 20);
INSERT INTO doacao VALUES (3, 6, '24-fev-23', 10);
INSERT INTO doacao VALUES (4, 8, '26-fev-23', 20);
INSERT INTO doacao VALUES (5, 12, '28-fev-23', 30);
INSERT INTO doacao VALUES (6, 14, '07-mar-23', 60);
INSERT INTO doacao VALUES (7, 15, '18-mar-23', 40);
INSERT INTO doacao VALUES (8, 17, '25-mar-23', 60);
INSERT INTO doacao VALUES (9, 19, '03-jun-23', 50);
INSERT INTO doacao VALUES (10, 20, '24-jun-23', 80);
INSERT INTO doacao VALUES (11, 17, '25-mar-23', 60);
INSERT INTO doacao VALUES (12, 17, '03-jun-23', 50);
INSERT INTO doacao VALUES (13, 17, '24-jun-23', 80);


INSERT INTO destino VALUES (1, 'Avenida Sapopemba', 'João', '(11) 98454-4468', 150);
INSERT INTO destino VALUES (2, 'Avenida Sao João', 'Pedro', '(11) 98484-5238', 230);
INSERT INTO destino VALUES (3, 'Rua Galvão Bueno', 'Marilda', '(11) 95488-8478', 143);
INSERT INTO destino VALUES (4 ,'Rua Tabor', 'Cristiane', '(11) 98483-4678', 165);
INSERT INTO destino VALUES (5 ,'Rua do Brás', 'Robson', '(11) 98422-5678', 170);
INSERT INTO destino VALUES (6 ,'Rua Canário', 'Andrea', '(11) 98481-1678', 153);
INSERT INTO destino VALUES (7 ,'Avenida Ibirapuera', 'Aparecida', '(11) 98412-5678', 135);
INSERT INTO destino VALUES (8 ,'Rua Macuco', 'Marli', '(11) 98484-6338', 176);
INSERT INTO destino VALUES (9 ,'Rua Limeira', 'Gabriela', '(11) 98484-5524', 220);
INSERT INTO destino VALUES (10 ,'Rua Sabiá', 'Verana', '(11) 98154-5666', 212);


INSERT INTO receptor_destino VALUES(1, 1);
INSERT INTO receptor_destino VALUES(1, 2);
INSERT INTO receptor_destino VALUES(3, 1);
INSERT INTO receptor_destino VALUES(4, 3);
INSERT INTO receptor_destino VALUES(1, 4);
INSERT INTO receptor_destino VALUES(7, 5);
INSERT INTO receptor_destino VALUES(18, 1);
INSERT INTO receptor_destino VALUES(16, 1);
INSERT INTO receptor_destino VALUES(13, 1);
INSERT INTO receptor_destino VALUES(16, 2);


INSERT INTO plantio_voluntario VALUES(1, 1);
INSERT INTO plantio_voluntario VALUES(6, 2);
INSERT INTO plantio_voluntario VALUES(3, 5);
INSERT INTO plantio_voluntario VALUES(4, 3);
INSERT INTO plantio_voluntario VALUES(5, 4);
INSERT INTO plantio_voluntario VALUES(4, 5);
INSERT INTO plantio_voluntario VALUES(2, 16);
INSERT INTO plantio_voluntario VALUES(9, 19);
INSERT INTO plantio_voluntario VALUES(8, 20);
INSERT INTO plantio_voluntario VALUES(9, 20);


INSERT INTO plantio_colheita VALUES(1, 1);
INSERT INTO plantio_colheita VALUES(2, 2);
INSERT INTO plantio_colheita VALUES(3, 5);
INSERT INTO plantio_colheita VALUES(4, 3);
INSERT INTO plantio_colheita VALUES(5, 4);
INSERT INTO plantio_colheita VALUES(6, 5);
INSERT INTO plantio_colheita VALUES(7, 9);
INSERT INTO plantio_colheita VALUES(8, 1);
INSERT INTO plantio_colheita VALUES(9, 7);
INSERT INTO plantio_colheita VALUES(10, 8);


INSERT INTO colheita_voluntario VALUES(1, 1);
INSERT INTO colheita_voluntario VALUES(2, 2);
INSERT INTO colheita_voluntario VALUES(5, 3);
INSERT INTO colheita_voluntario VALUES(3, 4);
INSERT INTO colheita_voluntario VALUES(4, 5);
INSERT INTO colheita_voluntario VALUES(5, 16);
INSERT INTO colheita_voluntario VALUES(9, 17);
INSERT INTO colheita_voluntario VALUES(1, 18);
INSERT INTO colheita_voluntario VALUES(7, 19);
INSERT INTO colheita_voluntario VALUES(8, 20);
INSERT INTO colheita_voluntario VALUES(8, 18);
INSERT INTO colheita_voluntario VALUES(8, 19);
INSERT INTO colheita_voluntario VALUES(8, 2);


--03: SELECTS
--03.01: CONSULTA SIMPLES (três exemplos)

--03.01.01: Aqui buscamos na tabela alimentos o nome e o preço do alimento com valores entre 5 e 7 (inclusive) ordenados pelo seu preço
SELECT nome_alimento alimento, preco_alimento preço FROM alimento 
WHERE preco_alimento BETWEEN 5 AND 7 
ORDER BY preco_alimento;

--03.01.02: Aqui buscamos o espaço e a data do plantio que estiverem nos espaços 5, 6, 8 e 9 na tabela plantio ordenados de forma decrescente pela data do plantio.
SELECT espaco_plantio espaço, data_plantio data FROM plantio
WHERE espaco_plantio IN (5, 6, 8, 9) 
ORDER BY data_plantio DESC;

--03.01.03: Aqui buscamos a data e a descrição da colheita que em sua descrição possua a palavra "bom" ordenados de forma decrescente pela data da colheita.
SELECT data_colheita data, descricao_colheita descrição FROM colheita
WHERE descricao_colheita LIKE '%bom%' ORDER BY data_colheita DESC;

--03.02: CONSULTA COM JUNÇÃO DE TABELAS (três exemplos)

--03.02.01: Aqui buscamos o id e nome do receptor (transportador dos alimentos), o nome do responsável e endereço do destino, nas tabelas receptor_destino, destino e usuário.
SELECT rd.id_usuario receptor,
u.nome_usuario "NOME RECEPTOR",
d.endereco_destino "ENDEREÇO DESTINO",
d.responsavel_destino responsável FROM receptor_destino rd
INNER JOIN usuario u ON u.id_usuario = rd.id_usuario
INNER JOIN destino d ON d.id_destino = rd.id_destino;


--03.02.02: Aqui buscamos todos os dados dos usuários que são doadores juntando as tabelas usuário e doador
SELECT usuario.id_usuario usuário, usuario.cpf_usuario cpf,
usuario.nome_usuario nome, usuario.email_usuario email,
usuario.cel_usuario celular, usuario.senha_usuario senha,
usuario.status_usuario status, 
doador.nivel_doador nível, doador.moedas_doador moedas
FROM usuario
INNER JOIN doador ON usuario.id_usuario = doador.id_usuario;

--03.02.03: Aqui buscamos os dados do plantio, do alimento e do voluntário juntando as tabelas e ordenando pelo nome do alimento
SELECT pv.id_plantio plantio, p.data_plantio "DATA PLANTIO", a.nome_alimento alimento,
u.nome_usuario voluntário, v.data_registro_voluntario "DATA DE REGISTRO"
FROM plantio_voluntario pv
JOIN plantio p ON pv.id_plantio = p.id_plantio
JOIN usuario u ON pv.id_usuario = u.id_usuario
JOIN voluntario v ON u.id_usuario = v.id_usuario
JOIN alimento a ON p.id_alimento = a.id_alimento
ORDER BY a.nome_alimento;


--03.03 FUNÇÃO DE GRUPO E AGRUPAMENTO (três exemplos)
--03.03.01: Aqui buscamos o número de plantios por voluntário agrupados pelo voluntário e ordenados de forma decrescente pela quantidade de plantios:
SELECT v.id_usuario usuário, u.nome_usuario nome, COUNT(*) "QUANTIDADE DE PLANTIOS"
FROM voluntario v
INNER JOIN usuario u ON v.id_usuario = u.id_usuario
INNER JOIN plantio_voluntario pv ON v.id_usuario = pv.id_usuario
GROUP BY v.id_usuario, u.nome_usuario
ORDER BY "QUANTIDADE DE PLANTIOS" DESC;

--03.03.02: Aqui buscamos o total de doações por doador agrupados pelo doador e ordenados de forma decrescente pela quantidade de moedas:
SELECT u.nome_usuario "NOME", SUM(d.qtd_moedas_doacao) "TOTAL DOAÇÕES"
FROM usuario u
JOIN doacao d ON u.id_usuario = d.id_usuario
GROUP BY u.nome_usuario
ORDER BY "TOTAL DOAÇÕES" DESC;

--03.03.03: Aqui buscamos a quantidade de colheitas por alimento com descrição de colheita contendo a palavra "pragas":
SELECT a.nome_alimento alimento, COUNT(c.id_colheita) "COLHEITAS COM PRAGAS"
FROM alimento a
JOIN plantio p ON a.id_alimento = p.id_alimento
JOIN colheita c ON p.id_plantio = c.id_colheita
WHERE c.descricao_colheita LIKE '%pragas%'
GROUP BY a.nome_alimento;


--03.04: FUNÇÃO DE GRUPO, AGRUPAMENTO COM FILTRO (HAVING) E JUNÇÃO DE TABELAS (três exemplos)
--03.04.01: Aqui buscamos o nome, nível e quantidade de doações do doador cuja doação tenha sido realizada em 2023 e tenha feito mais de 2 doações
SELECT u.nome_usuario nome, d.nivel_doador nível, COUNT(do.id_doacao) "QUANTIDADE DE DOAÇÕES"
FROM doador d
INNER JOIN usuario u ON u.id_usuario = d.id_usuario
JOIN doacao do ON u.id_usuario = do.id_usuario
WHERE EXTRACT(YEAR FROM do.data_doacao) = 2023
GROUP BY u.nome_usuario, d.nivel_doador
HAVING COUNT(do.id_doacao) > 2;

--03.04.02: Aqui buscamos o nome, data de registro e quantidade de colheitas do voluntário os quais tenham feito mais de 1 colheita
SELECT u.nome_usuario nome, v.data_registro_voluntario "DATA DE REGISTRO", COUNT(cv.id_colheita) AS "QUANTIDADE DE COLHEITAS"
FROM usuario u
JOIN voluntario v ON u.id_usuario = v.id_usuario
JOIN colheita_voluntario cv ON v.id_usuario = cv.id_usuario
GROUP BY u.nome_usuario, v.data_registro_voluntario
HAVING COUNT(cv.id_colheita) > 1;

--03.04.03: Aqui buscamos o nome, email e quantidade de destinos atendidos pelo receptor que só atenda 1 ou menos destinos
SELECT u.nome_usuario, u.email_usuario, COUNT(rd.id_destino) AS total_destinos
FROM usuario u
JOIN receptor_destino rd ON u.id_usuario = rd.id_usuario
GROUP BY u.nome_usuario, u.email_usuario
HAVING COUNT(rd.id_destino) <= 1;