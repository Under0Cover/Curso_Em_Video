create database cadastro_curso_guanabara;

create table pessoas(
nome varchar(30),
idade tinyint,
sexo char(1),
peso float,
altura float,
nacionalidade varchar(20)
);

describe pessoas;

drop database cadastro_curso_guanabara;

CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8
default collate utf8_general_ci;

create table pessoas (
id int not null auto_increment,
nome varchar (50) not null, 
nascimento date not null,
sexo varchar (15),
peso decimal (5,2),
altura decimal (3,2),
nacionalidade varchar (40) default 'Brasil',
primary key (id)
) default charset = utf8;

drop table pessoas;

insert into pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
values
('Godofredo', '1984-01-02', 'Masculino', '78,5', '1,73', 'Brasil');

select * from pessoas;

insert into pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
values
('Maria', '1999-12-30', 'Feminino', '78,5', '1,83', 'Brasil');

insert into pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
values
('João', '1989-03-25', 'Masculino', '78.5', '1.83', 'Brasil');

insert into pessoas values
(default, 'Gonzaga', '1974-01-30', 'Feminino', '54.5', '1.58', default);

insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'Creuza', '1920-12-30', 'Feminino', '50.2', '1.65', default);

insert into pessoas values
(default, 'Ana', '1975-12-22', 'Feminino', '52.3', '1.45', 'Estados Unidos'),
(default, 'Pedro', '2000-07-15', 'Masculino', '88.6', '1.76', 'Portugal'),
(default, 'Maria das Dores', '1963-05-30', 'Feminino', '52.8', '1.68', 'Canadá');

alter table pessoas
add column profissao varchar(10);

alter table pessoas
drop column profissao;

desc pessoas;

alter table pessoas
add column profissao varchar(10)
after nome;

alter table pessoas
modify column profissao varchar(25);

alter table pessoas
change column profissao prof varchar(25);

alter table pessoas
rename to usuarios;

desc usuarios;

create table if not exists cursos (
nome varchar(30) not null unique,
descricao text,
carga_horaria int unsigned,
total_aulas int unsigned,
ano year
) default charset =utf8;

drop table cursos;

alter table cursos
add column idcurso int first;

desc cursos;

alter table cursos
add primary key (idcurso);

select * from usuarios;

insert into cursos value
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '40', '37', '2014'),
('4', 'PGP', 'Curso de PHP para Iniciantes', '40', '20', '2014'),
('5', 'Jarva', 'Introdução ao Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso Completo de Word', '30', '15', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2016'),
('9', 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'Youtuber', 'Gerar polêmica para ganhar inscritos', '5', '2', '2018');

select * from cursos;

select * from usuarios;

update cursos
set nome = 'Html5'
where idcurso = '1';

update cursos
set nome = 'PHP'
where idcurso = '4';

update cursos
set ano = '2015'
where idcurso = '4';

update cursos
set nome = 'Java', ano = '2015'
where idcurso = '5';

update cursos
set carga_horaria = '50'
where idcurso = '5';

update usuarios
set peso = '76.45', altura = '1.75'
where id = '1';

update usuarios
set peso = '65.44', altura = '1.45'
where id = '2';

select * from usuarios;

select * from cursos;

update cursos
set ano = '2018'
where idcurso = '8';

update usuarios
set nome = 'Benedita', nascimento = '1935-05-28', peso = '65.34', altura = '1.44'
where id = '4';

delete from cursos
where ano = '2018'
limit 3;

drop database test;

show tables;
desc cursos;
desc usuarios;

select * from amigos;

use exemplo;

use cadastro;
