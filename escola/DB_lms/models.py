from django.db import models

# Create your models here.
class Aluno(models.Model):
    login = models.CharField("LOGIN", max_length=20)
    senha = models.CharField("SENHA", max_length=20)
    nome = models.CharField("NOME", max_length=50)
    email = models.EmailField("EMAIL", max_length=90)
    celular = models.CharField("CELULAR", max_length=12)
    dataExpiracao = models.DateField("DATAEXPIRACAO")

    def __str__(self):
        return self.nome
    
class Atividade(models.Model):
    titulo = models.CharField("TITULO", max_length=2000,blank=True)
    descricao = models.CharField("DESCRICAO", max_length=2000,blank=True)
    conteudo = models.CharField("CONTEUDO", max_length=2000,blank=True)
    tipo = models.CharField("TIPO", max_length=2000,blank=True)
    extra = models.CharField("EXTRA", max_length=2000,blank=True)
    idProfessor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo


class AtividadeVinculada(models.Model):
    id_atividade = models.ForeignKey("Atividade", on_delete=models.DO_NOTHING)
    id_professor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)
    id_disciplinaOfertada = models.ForeignKey("DisciplinaOfertada", on_delete=models.DO_NOTHING)
    rotulo = models.CharField("ROTULO", max_length=2000,blank=True)
    status = models.CharField("STATUS", max_length=2000,blank=True)
    dt_inicio_respostas = models.DateField("DT_INICIO_RESPOSTAS",blank=True)
    dt_fim_respostas = models.DateField("DT_FIM_RESPOSTAS",blank=True)


    def __str__(self):
        return self.id_atividade


class Coordenador(models.Model):
    login = models.CharField("LOGIN", max_length=20)
    senha = models.CharField("SENHA", max_length=20)
    nome = models.CharField("NOME", max_length=50)
    email = models.EmailField("EMAIL", max_length=90)
    celular = models.CharField("CELULAR", max_length=12)
    dataExpiracao = models.DateField("DATAEXPIRACAO", blank=True)

    def __str__(self):
        return self.login


class Curso(models.Model):
    nome = models.CharField("NOME", max_length=50)

    def __str__(self):
        return self.nome



class Disciplina(models.Model):
     nome = models.CharField("NOME", max_length=60)
     date = models.DateField("DATE")
     status = models.CharField("STATUS", max_length=50, blank=True)
     planoDeEnsino = models.CharField("PLANO_DE_ENSINO", max_length=2000, blank=True)
     cargaHoraria = models.IntegerField("CARGA_HORARIA")
     competencias = models.CharField("COMPETENCIAS", max_length=2000, blank=True)
     habilidade = models.CharField("HABILIDADES", max_length=2000, blank=True)
     ementa = models.CharField("EMENTA", max_length=2000, blank=True)
     conteudoProgramatico = models.CharField("CONTEUDO_PROGRAMATICO", max_length=2000, blank=True)
     bibliografiaBasica = models.CharField("BIBLIOGRAFIA_BASICA", max_length=2000, blank=True)
     bibliografiaComplementar = models.CharField("BIBLIOGRAFIA_COMPLEMENTAR", max_length=2000, blank=True)
     percentualPratico = models.FloatField("PERCENTUAL_PRATICO", blank=True)
     percentualTeorico = models.FloatField("PERCENTUAL_TEORICO", blank=True)
     id_professor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)
     id_coordenador = models.ForeignKey("Coordenador", on_delete=models.DO_NOTHING)

     def __str__(self):
         return self.nome


class DisciplinaOfertada(models.Model):
    data_inicio = models.DateField("DATA_INICIO", blank=True)
    data_fim = models.DateField("DATA_FIM", blank=True)
    ano = models.DateField("ANO", blank=True)
    semestre= models.IntegerField("SEMESTRE", blank=True)
    turma = models.CharField("TURMA", max_length=80,blank=True)
    metodologia = models.CharField("METODOLOGIA", max_length=2000,blank=True)
    recursos = models.CharField("RECURSOS", max_length=2000, blank=True)
    citerio_avaliacao = models.CharField("CRITERIO_AVALIACAO", max_length=2000, blank=True)
    plano_de_ensino = models.CharField("PLANO_DE_AULAS", max_length=2000, blank=True)
    id_coordenador = models.ForeignKey("Coordenador", on_delete=models.DO_NOTHING)
    id_professor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)
    id_disciplina = models.ForeignKey("Disciplina", on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey("Curso", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_coordenador


class Entrega(models.Model):
    titulo = models.CharField("TITULO", max_length=2000, blank=True)
    RESPOSTA = models.CharField("RESPOSTA", max_length=2000, blank=True)
    data_entrega = models.DateField("DT_ENTREGA", blank=True)
    status = models.CharField("STATUS", max_length=2000, blank=True)
    nota = models.FloatField("NOTA", blank=True)
    dt_avaliacao = models.DateField("DT_AVALIACAO", blank=True)
    obs = models.CharField("OBS", max_length=2000, blank=True)
    id_aluno = models.ForeignKey("Aluno", on_delete=models.DO_NOTHING)
    id_atividade_vinculada = models.ForeignKey("AtividadeVinculada", on_delete=models.DO_NOTHING)
    id_professor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_aluno


class Mensagem(models.Model):
    assunto = models.CharField("ASSUNTO", max_length=80, blank=True)
    referencia = models.CharField("REFERENCIA", max_length=2000, blank=True)
    conteudo = models.CharField("CONTEUDO", max_length=2000, blank=True)
    status = models.CharField("STATUS", max_length=2000, blank=True)
    dt_envio = models.DateField("DT_ENVIO", blank=True)
    resposta = models.CharField("RESPOSTA", max_length=2000, blank=True)
    dt_resposta = models.DateField("DT_RESPOSTA", blank=True)
    id_aluno = models.ForeignKey("Aluno", on_delete=models.DO_NOTHING)
    id_professor = models.ForeignKey("Professor", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_aluno


class Professor(models.Model):
    login = models.CharField("LOGIN", max_length=20)
    senha = models.CharField("SENHA", max_length=20)
    nome = models.CharField("NOME", max_length=50)
    email = models.EmailField("EMAIL", max_length=90)
    celular = models.CharField("CELULAR", max_length=12)
    dataExpiracao = models.DateField("DATAEXPIRACAO")
    apelido = models.DateField("APELIDO", max_length=50, blank=True)

    def __str__(self):
        return self.login


class SolicitacaoMatricula(models.Model):
    data_solicitacao = models.DateField("DATA_SOLICITACAO", blank=True)
    status = models.CharField("STATUS", max_length=2000,blank=True)
    id_aluno = models.ForeignKey("Aluno", on_delete=models.DO_NOTHING)
    id_disciplinaOfertada = models.ForeignKey("DisciplinaOfertada", on_delete=models.DO_NOTHING)
    id_coordenador = models.ForeignKey("Coordenador", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_aluno