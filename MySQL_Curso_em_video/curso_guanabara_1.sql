select * from usuarios;

select * from gafanhotos;

select * from cursos;

select * from cursos
order by nome;

select * from cursos
order by nome desc;

select nome, carga, ano from cursos
order by ano, nome;

select idcurso, nome, descricao, carga from cursos
where ano = '2016'
order by nome;

select idcurso, nome, descricao, ano from cursos
where ano < 2017
order by ano, nome;

select nome, ano from cursos
where ano between 2014 and 2016
order by idcurso;

select nome, ano, carga from cursos
where ano in (2014, 2016, 2018)
order by idcurso;

select * from cursos
where carga > 35 and totaulas < 30;

select nome, descricao, carga, totaulas from cursos
where carga > 35 or totaulas < 30
order by ano;

select * from cursos
where nome = 'php';

select * from cursos
where nome like 'p%';

select * from cursos
where nome not like '%a%';

select * from cursos
where nome like 'ph%p_';

select * from cursos
where nome like '%a';

select * from gafanhotos
where nome like '%silva%';

select distinct carga from cursos;

select distinct nacionalidade from gafanhotos;

select count(*) from cursos;

select max(totaulas) from cursos
where ano = '2016';

select nome, min(totaulas) from cursos
where ano = '2016';

select sum(totaulas) from cursos
where ano = '2016';

select avg(totaulas) from cursos
where ano = '2016';

show columns from gafanhotos;

select nome from gafanhotos
where sexo = 'f'
order by nome;

select nascimento from gafanhotos;

select * from gafanhotos
where sexo = 'm' and profissao = 'programador'
order by nome;

select * from gafanhotos
where nome like 'j%' and sexo = 'f' and nacionalidade = 'brasil';

select nome, nacionalidade from gafanhotos
where nome like '%silva%' and nacionalidade != 'brasil' and peso < 100;

select * from gafanhotos;

select max(altura) from gafanhotos
where sexo = 'm' and nacionalidade = 'brasil';

select avg(peso) from gafanhotos;

select count(nome) from gafanhotos
where sexo = 'f' and altura > 1.90;

select * from gafanhotos 
where nascimento between '2000-01-01' and '2015-12-31'
order by nascimento;

select min(peso) from gafanhotos
where sexo ='F' and nascimento between '1990-01-01' and '2000-12-31';

select * from gafanhotos
where sexo = 'm' and nascimento between '2000-01-01' and '2005-01-01'
order by nascimento;

select * from gafanhotos;

select carga, count(nome) from cursos
group by carga;

select totaulas, count(*) from cursos
group by totaulas order by totaulas;

select * from cursos
where totaulas = 30;

select * from cursos
where totaulas = 12;

select * from cursos
where totaulas > 20;

select carga, count(nome) from cursos
where totaulas = 30
group by carga;

select carga, count(nome) from cursos
group by carga having count(nome) > 3 ;

select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*) desc;

select avg(carga) from cursos;

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);

select profissao, count(*) from gafanhotos
group by profissao;

select sexo, count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'brasil'
group by nacionalidade
having count(nacionalidade) >= 3;

select altura, count(*) from gafanhotos
where peso > 100
group by altura
having altura > (select avg(altura) from gafanhotos);

select * from gafanhotos;

desc gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido)
references cursos(idcurso);

desc gafanhotos;
desc cursos;

select * from gafanhotos;

update gafanhotos
set cursopreferido = '6'
where id = '1';

select g.nome, c.nome, c.ano
from gafanhotos as g join cursos as c
on c.idcurso = g.cursopreferido
order by g.nome;

select g.nome, c.nome, c.ano
from gafanhotos as g left join cursos as c
on c.idcurso = g.cursopreferido;

create table gafanhoto_assiste_curso (
id int not null auto_increment,
data date,
idgafanhoto int,
idcurso int,
primary key (id),
foreign key (idgafanhoto) references gafanhotos (id),
foreign key (idcurso) references cursos (idcurso)
) default charset = utf8;

desc gafanhoto_assiste_curso;

insert into gafanhoto_assiste_curso values
(default, '2014-03-01', '1', '2'),
(default, '2014-09-04', '5', '3'),
(default, '2015-03-31', '2', '9'),
(default, '2015-12-22', '3', '6'),
(default, '2018-06-28', '12', '22'),
(default, '2014-07-23', '11', '25');

select * from gafanhoto_assiste_curso;

select g.nome, c.nome from gafanhotos as g
join gafanhoto_assiste_curso as a
on g.id = a.idgafanhoto
join cursos as c
on c.idcurso = a.idcurso
order by g.nome;