# Generated by Django 2.0.4 on 2018-05-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB_lms', '0002_atividade'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeVinculada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_atividade', models.IntegerField(blank=True, verbose_name='ID_ATIVIDADE')),
                ('id_professor', models.IntegerField(blank=True, verbose_name='ID_PROFESSOR')),
                ('id_disciplinaOfertada', models.IntegerField(blank=True, verbose_name='ID_DISCIPLINA_OFERTADA')),
                ('rotulo', models.CharField(blank=True, max_length=2000, verbose_name='ROTULO')),
                ('status', models.CharField(blank=True, max_length=2000, verbose_name='STATUS')),
                ('dt_inicio_respostas', models.DateField(blank=True, verbose_name='DT_INICIO_RESPOSTAS')),
                ('dt_fim_respostas', models.DateField(blank=True, verbose_name='DT_FIM_RESPOSTAS')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='LOGIN')),
                ('senha', models.CharField(max_length=20, verbose_name='SENHA')),
                ('nome', models.CharField(max_length=50, verbose_name='NOME')),
                ('email', models.EmailField(max_length=90, verbose_name='EMAIL')),
                ('celular', models.CharField(max_length=12, verbose_name='CELULAR')),
                ('dataExpiracao', models.DateField(blank=True, verbose_name='DATAEXPIRACAO')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='NOME')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='NOME')),
                ('date', models.DateField(verbose_name='DATE')),
                ('status', models.CharField(blank=True, max_length=50, verbose_name='STATUS')),
                ('planoDeEnsino', models.CharField(blank=True, max_length=2000, verbose_name='PLANO_DE_ENSINO')),
                ('cargaHoraria', models.IntegerField(verbose_name='CARGA_HORARIA')),
                ('competencias', models.CharField(blank=True, max_length=2000, verbose_name='COMPETENCIAS')),
                ('habilidade', models.CharField(blank=True, max_length=2000, verbose_name='HABILIDADES')),
                ('ementa', models.CharField(blank=True, max_length=2000, verbose_name='EMENTA')),
                ('conteudoProgramatico', models.CharField(blank=True, max_length=2000, verbose_name='CONTEUDO_PROGRAMATICO')),
                ('bibliografiaBasica', models.CharField(blank=True, max_length=2000, verbose_name='BIBLIOGRAFIA_BASICA')),
                ('bibliografiaComplementar', models.CharField(blank=True, max_length=2000, verbose_name='BIBLIOGRAFIA_COMPLEMENTAR')),
                ('percentualPratico', models.FloatField(blank=True, verbose_name='PERCENTUAL_PRATICO')),
                ('percentualTeorico', models.FloatField(blank=True, verbose_name='PERCENTUAL_TEORICO')),
                ('id_professor', models.IntegerField(blank=True, verbose_name='ID_PROFESSOR')),
                ('id_coordenador', models.IntegerField(blank=True, verbose_name='ID_COORDENADOR')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_coordenador', models.IntegerField(blank=True, verbose_name='ID_COORDENADOR')),
                ('data_inicio', models.DateField(blank=True, verbose_name='DATA_INICIO')),
                ('data_fim', models.DateField(blank=True, verbose_name='DATA_FIM')),
                ('id_disciplina', models.IntegerField(blank=True, verbose_name='ID_DISCIPLINA')),
                ('id_curso', models.IntegerField(blank=True, verbose_name='ID_CURSO')),
                ('ano', models.DateField(blank=True, verbose_name='ANO')),
                ('semestre', models.IntegerField(blank=True, verbose_name='SEMESTRE')),
                ('turma', models.CharField(blank=True, max_length=80, verbose_name='TURMA')),
                ('id_professor', models.IntegerField(blank=True, verbose_name='ID_PROFESSOR')),
                ('metodologia', models.CharField(blank=True, max_length=2000, verbose_name='METODOLOGIA')),
                ('recursos', models.CharField(blank=True, max_length=2000, verbose_name='RECURSOS')),
                ('citerio_avaliacao', models.CharField(blank=True, max_length=2000, verbose_name='CRITERIO_AVALIACAO')),
                ('plano_de_ensino', models.CharField(blank=True, max_length=2000, verbose_name='PLANO_DE_AULAS')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aluno', models.IntegerField(blank=True, verbose_name='ID_ALUNO')),
                ('id_atividade_vinculada', models.IntegerField(blank=True, verbose_name='ID_ATIVIDADE_VINCULADA')),
                ('titulo', models.CharField(blank=True, max_length=2000, verbose_name='TITULO')),
                ('RESPOSTA', models.CharField(blank=True, max_length=2000, verbose_name='RESPOSTA')),
                ('data_entrega', models.DateField(blank=True, verbose_name='DT_ENTREGA')),
                ('status', models.CharField(blank=True, max_length=2000, verbose_name='STATUS')),
                ('id_professor', models.IntegerField(blank=True, verbose_name='ID_PROFESSOR')),
                ('nota', models.FloatField(blank=True, verbose_name='NOTA')),
                ('dt_avaliacao', models.DateField(blank=True, verbose_name='DT_AVALIACAO')),
                ('obs', models.CharField(blank=True, max_length=2000, verbose_name='OBS')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aluno', models.IntegerField(blank=True, verbose_name='ID_ALUNO')),
                ('id_professor', models.IntegerField(blank=True, verbose_name='ID_PROFESSOR')),
                ('assunto', models.CharField(blank=True, max_length=80, verbose_name='ASSUNTO')),
                ('referencia', models.CharField(blank=True, max_length=2000, verbose_name='REFERENCIA')),
                ('conteudo', models.CharField(blank=True, max_length=2000, verbose_name='CONTEUDO')),
                ('status', models.CharField(blank=True, max_length=2000, verbose_name='STATUS')),
                ('dt_envio', models.DateField(blank=True, verbose_name='DT_ENVIO')),
                ('resposta', models.CharField(blank=True, max_length=2000, verbose_name='RESPOSTA')),
                ('dt_resposta', models.DateField(blank=True, verbose_name='DT_RESPOSTA')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='LOGIN')),
                ('senha', models.CharField(max_length=20, verbose_name='SENHA')),
                ('nome', models.CharField(max_length=50, verbose_name='NOME')),
                ('email', models.EmailField(max_length=90, verbose_name='EMAIL')),
                ('celular', models.CharField(max_length=12, verbose_name='CELULAR')),
                ('dataExpiracao', models.DateField(verbose_name='DATAEXPIRACAO')),
                ('apelido', models.DateField(blank=True, max_length=50, verbose_name='APELIDO')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aluno', models.IntegerField(blank=True, verbose_name='ID_ALUNO')),
                ('id_disciplinaOfertada', models.IntegerField(blank=True, verbose_name='ID_DISCIPLINA_OFERTADA')),
                ('data_solicitacao', models.DateField(blank=True, verbose_name='DATA_SOLICITACAO')),
                ('id_coordenador', models.IntegerField(blank=True, verbose_name='ID_COORDENADOR')),
                ('status', models.CharField(blank=True, max_length=2000, verbose_name='STATUS')),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=90, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='conteudo',
            field=models.CharField(blank=True, max_length=2000, verbose_name='CONTEUDO'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=models.CharField(blank=True, max_length=2000, verbose_name='DESCRICAO'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='extra',
            field=models.CharField(blank=True, max_length=2000, verbose_name='EXTRA'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='idProfessor',
            field=models.IntegerField(blank=True, verbose_name='ID_PROFESSOR'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='tipo',
            field=models.CharField(blank=True, max_length=2000, verbose_name='TIPO'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='titulo',
            field=models.CharField(blank=True, max_length=2000, verbose_name='TITULO'),
        ),
    ]
