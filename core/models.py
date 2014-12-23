# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Associado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_associado = models.DateField(blank=True, null=True)
    data_atua = models.DateTimeField(blank=True, null=True)
    data_atua_cad = models.DateTimeField(blank=True, null=True)
    nome_instituicao = models.CharField(max_length=255, blank=True)
    matricula = models.CharField(max_length=100)
    adm = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    sess = models.CharField(max_length=255, blank=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)
    usurem = models.CharField(max_length=255, blank=True)
    outro_tipo_circuito = models.CharField(max_length=255, blank=True)
    razao_social = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    endereco = models.TextField(blank=True)
    numero = models.CharField(max_length=50, blank=True)
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=45, blank=True)
    referencia = models.TextField(blank=True)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)
    estado = models.ForeignKey('Estado', blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True)
    website = models.CharField(max_length=100, blank=True)
    res_nome = models.CharField(max_length=255, blank=True)
    res_sexo = models.CharField(max_length=3, blank=True)
    res_cpf = models.CharField(max_length=11, blank=True)
    res_cargo = models.TextField(blank=True)
    res_email = models.CharField(max_length=255, blank=True)
    res_tel1_ddd = models.CharField(max_length=3, blank=True)
    res_tel1 = models.CharField(max_length=50, blank=True)
    res_tel1_ramal = models.CharField(max_length=50, blank=True)
    res_tel2_ddd = models.CharField(max_length=3, blank=True)
    res_tel2 = models.CharField(max_length=50, blank=True)
    res_tel3_ddd = models.CharField(max_length=3, blank=True)
    res_tel3 = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=100, blank=True)
    info_atividades = models.TextField(blank=True)
    info_como_serao_utilizados = models.TextField(blank=True)
    info_cod_sabendo = models.IntegerField(blank=True, null=True)
    info_sabendo_orgao = models.CharField(max_length=50, blank=True)
    info_filmes_exibidos = models.TextField(blank=True)
    info_sabendo_outro = models.CharField(max_length=50, blank=True)
    info_pref_formato = models.CharField(max_length=50, blank=True)
    info_pref_genero = models.CharField(max_length=50, blank=True)
    info_parceiros_cult = models.TextField(blank=True)
    info_cineclube = models.CharField(max_length=255, blank=True)
    info_sess_aberto_frequencia = models.IntegerField(blank=True, null=True)
    info_sess_aberto_frequencia_outro = models.CharField(max_length=255, blank=True)
    info_sess_fechado_frequencia = models.IntegerField(blank=True, null=True)
    info_sess_fechado_frequencia_outro = models.CharField(max_length=255, blank=True)
    info_hora_sess = models.CharField(max_length=50, blank=True)
    info_media_espectadores = models.CharField(max_length=50, blank=True)
    info_perfil_espectadores = models.TextField(blank=True)
    info_sess_valor = models.FloatField(blank=True, null=True)
    info_meio_divulga = models.IntegerField(blank=True, null=True)
    leg_nome = models.CharField(max_length=255, blank=True)
    leg_sexo = models.CharField(max_length=3, blank=True)
    leg_cpf = models.CharField(max_length=11, blank=True)
    leg_cargo = models.TextField(blank=True)
    leg_email = models.CharField(max_length=255, blank=True)
    leg_tel1_ddd = models.CharField(max_length=3, blank=True)
    leg_tel1 = models.CharField(max_length=50, blank=True)
    leg_tel1_ramal = models.CharField(max_length=50, blank=True)
    leg_tel2_ddd = models.CharField(max_length=3, blank=True)
    leg_tel2 = models.CharField(max_length=50, blank=True)
    leg_tel3_ddd = models.CharField(max_length=3, blank=True)
    leg_tel3 = models.CharField(max_length=50, blank=True)
    obs = models.TextField(blank=True)
    conta_acesso = models.IntegerField(blank=True, null=True)
    est_pedidos = models.IntegerField(blank=True, null=True)
    est_programas = models.IntegerField(blank=True, null=True)
    est_publico = models.IntegerField(blank=True, null=True)
    est_dias_cadastro = models.IntegerField(blank=True, null=True)
    est_consulta_local = models.IntegerField(blank=True, null=True)
    est_acessos = models.IntegerField(blank=True, null=True)
    est_sess_realizadas = models.IntegerField(blank=True, null=True)
    info_cursos = models.IntegerField(blank=True, null=True)
    info_debate = models.IntegerField(blank=True, null=True)
    info_sess_taxa = models.IntegerField(blank=True, null=True)
    info_sess_cobrada = models.IntegerField(blank=True, null=True)
    info_acervo_proprio = models.IntegerField(blank=True, null=True)
    info_acervo = models.IntegerField(blank=True, null=True)
    info_dist_folheto = models.IntegerField(blank=True, null=True)
    info_acao_biblioteca = models.IntegerField(blank=True, null=True)
    info_realiza_prod = models.IntegerField(blank=True, null=True)
    permite_cad_ponto = models.IntegerField(blank=True, null=True)
    exibir_pontos = models.IntegerField(blank=True, null=True)
    info_sess_fechado = models.IntegerField(blank=True, null=True)
    info_sess_aberto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'associado'


class AssociadoCircuito(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    circuito_id = models.IntegerField(blank=True, null=True)
    associado_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'associado_circuito'


class AssociadoHistorico(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.DateTimeField(blank=True, null=True)
    associado_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    texto = models.TextField(blank=True)
    acao = models.CharField(max_length=255, blank=True)
    email_enviado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'associado_historico'


class AssociadoPonto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    associado = models.ForeignKey(Associado, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    local_exibicao = models.CharField(max_length=255, blank=True)
    lugares = models.CharField(max_length=50, blank=True)
    tipo_exibicao = models.IntegerField(blank=True, null=True)
    tipo_exibicao_tela = models.TextField(blank=True)
    equipo_projecao_espec = models.TextField(blank=True)
    equipo_som_espec = models.TextField(blank=True)
    tels = models.CharField(max_length=100, blank=True)
    res_nome = models.CharField(max_length=255, blank=True)
    res_email = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    estado = models.ForeignKey('Estado', blank=True, null=True)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)
    website = models.CharField(max_length=200, blank=True)
    auditorio = models.IntegerField(blank=True, null=True)
    equipo_projecao = models.IntegerField(blank=True, null=True)
    equipo_som = models.IntegerField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    principal = models.IntegerField(blank=True, null=True)
    exibir_site = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'associado_ponto'


class Atendimento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    associado = models.ForeignKey(Associado, blank=True, null=True)
    pai_id = models.IntegerField(blank=True, null=True)
    usr_nome = models.CharField(max_length=255, blank=True)
    texto = models.TextField(blank=True)
    assunto = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'atendimento'


class Circuito(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    grupo = models.ForeignKey('CircuitoGrupo', blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuito'


class CircuitoAcesso(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data_atual = models.DateTimeField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    tel1 = models.CharField(max_length=150, blank=True)
    tel2 = models.CharField(max_length=150, blank=True)
    tel3 = models.CharField(max_length=150, blank=True)
    email = models.CharField(unique=True, max_length=200, blank=True)
    adm = models.IntegerField(blank=True, null=True)
    sess = models.CharField(max_length=50, blank=True)
    grupo_id = models.IntegerField(blank=True, null=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True)
    nome_contato = models.CharField(max_length=255, blank=True)
    circuito = models.ForeignKey(Circuito, blank=True, null=True)
    confirmada = models.IntegerField(blank=True, null=True)
    bloqueada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuito_acesso'


class CircuitoGrupo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    sigla = models.CharField(max_length=5, blank=True)
    peso = models.IntegerField(blank=True, null=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuito_grupo'


class CircuitoSerie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    circuito_id = models.IntegerField(blank=True, null=True)
    serie_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuito_serie'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    data_inicio_contrato = models.DateField(blank=True, null=True)
    data_fim_contrato = models.DateField(blank=True, null=True)
    qtd_limite = models.IntegerField(blank=True, null=True)
    qtd_produzida = models.IntegerField(blank=True, null=True)
    qtd_adquirida = models.IntegerField(blank=True, null=True)
    qtd_doada = models.IntegerField(blank=True, null=True)
    qtd_estoque = models.IntegerField(blank=True, null=True)
    dados_bancarios_pat = models.TextField(blank=True)
    dados_bancarios_direito = models.TextField(blank=True)
    relatorios = models.TextField(blank=True)
    obs = models.TextField(blank=True)
    filme_id = models.BigIntegerField(blank=True, null=True)
    deposito_ref_pat = models.IntegerField(blank=True, null=True)
    remuneracao_direito = models.IntegerField(blank=True, null=True)
    disponivel_aquisicao = models.IntegerField(blank=True, null=True)
    disponivel_renovacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'


class ContratoAssinatura(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contrato_id = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    obs = models.TextField(blank=True)
    quantidade = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'contrato_assinatura'


class ContratoDeposito(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contrato = models.ForeignKey(Contrato, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    banco = models.CharField(max_length=100, blank=True)
    agencia = models.CharField(max_length=100, blank=True)
    conta = models.CharField(max_length=50, blank=True)
    obs = models.TextField(blank=True)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato_deposito'


class Convenio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    convenio = models.CharField(max_length=50, blank=True)
    nome = models.CharField(max_length=200, blank=True)
    ano = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'convenio'


class Cupom(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cupom = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    perfil_id = models.IntegerField(blank=True, null=True)
    desconto = models.IntegerField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cupom'


class Curador(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data = models.DateTimeField(blank=True, null=True)
    data_atual = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    nome_artistico = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=17, blank=True)
    endereco = models.TextField(blank=True)
    cep = models.CharField(max_length=16, blank=True)
    cidade_id = models.BigIntegerField(blank=True, null=True)
    estado_id = models.BigIntegerField(blank=True, null=True)
    tel1 = models.CharField(max_length=200, blank=True)
    tel2 = models.CharField(max_length=200, blank=True)
    tel3 = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    curriculo = models.TextField(blank=True)
    obs = models.TextField(blank=True)
    senha = models.CharField(max_length=200, blank=True)
    adm = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    sess = models.CharField(max_length=60, blank=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)
    confirmada = models.IntegerField(blank=True, null=True)
    bloqueada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curador'


class CuradorFilme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme_id = models.BigIntegerField(blank=True, null=True)
    curador = models.ForeignKey(Curador, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_atual = models.DateTimeField(blank=True, null=True)
    temas = models.TextField(blank=True)
    palavra_chave = models.TextField(blank=True)
    indicado = models.IntegerField(blank=True, null=True)
    justificativa = models.TextField(blank=True)
    obs = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'curador_filme'


class Diretor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    nome_artistico = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_atual = models.DateTimeField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True)
    uf = models.CharField(max_length=3, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    filmografia = models.TextField(blank=True)
    endereco = models.TextField(blank=True)
    cep = models.CharField(max_length=12, blank=True)
    tel1 = models.CharField(max_length=200, blank=True)
    tel2 = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    obs = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'diretor'


class Estado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    uf = models.CharField(max_length=3, blank=True)
    regiao = models.ForeignKey('Regiao')

    class Meta:
        managed = False
        db_table = 'estado'


class Evento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo_id = models.IntegerField()
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_atual = models.DateTimeField()
    website = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    exibir = models.CharField(max_length=1, blank=True)
    ponto_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class FaixaEtaria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'faixa_etaria'


class Filme(models.Model):
    id = models.BigIntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_alteracao = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True)
    titulo_en = models.CharField(max_length=255, blank=True)
    sinopse = models.TextField(blank=True)
    sinopse_editada = models.TextField(blank=True)
    sinopse_en = models.TextField(blank=True)
    uf = models.CharField(max_length=50, blank=True)
    estado_id = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True)
    municipio_id = models.IntegerField(blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True)
    janela_projecao_pelicula = models.IntegerField(blank=True, null=True)
    ano_captacao = models.TextField(blank=True)  # This field type is a guess.
    ano_lancamento = models.TextField(blank=True)  # This field type is a guess.
    idioma_id = models.IntegerField(blank=True, null=True)
    faixa_etaria_id = models.IntegerField(blank=True, null=True)
    som = models.IntegerField(blank=True, null=True)
    tema = models.TextField(blank=True)
    formato_som = models.IntegerField(blank=True, null=True)
    formato = models.IntegerField(blank=True, null=True)
    genero_id = models.IntegerField(blank=True, null=True)
    genero_sub_id = models.IntegerField(blank=True, null=True)
    formato_captacao_id = models.IntegerField(blank=True, null=True)
    suporte_captacao_outro = models.CharField(max_length=255, blank=True)
    cod_cor = models.IntegerField(blank=True, null=True)
    co_produtora = models.CharField(max_length=255, blank=True)
    produtora = models.CharField(max_length=255, blank=True)
    duracao = models.IntegerField(blank=True, null=True)
    elenco = models.TextField(blank=True)
    dir_fotografia = models.CharField(max_length=255, blank=True)
    montagem_edicao = models.CharField(max_length=255, blank=True)
    roteiro = models.CharField(max_length=255, blank=True)
    assistente_direcao = models.CharField(max_length=255, blank=True)
    operador_camera = models.CharField(max_length=255, blank=True)
    assistente_camera = models.CharField(max_length=255, blank=True)
    producao_executiva = models.CharField(max_length=255, blank=True)
    dir_atores = models.CharField(max_length=255, blank=True)
    dir_producao = models.CharField(max_length=255, blank=True)
    dir_arte = models.CharField(max_length=255, blank=True)
    cenografia = models.CharField(max_length=255, blank=True)
    figurino = models.CharField(max_length=255, blank=True)
    sound_designer = models.CharField(max_length=255, blank=True)
    tec_som = models.CharField(max_length=255, blank=True)
    trilha_desc = models.TextField(blank=True)
    festivais = models.TextField(blank=True)
    premios = models.TextField(blank=True)
    edital_minc = models.TextField(blank=True)
    cpb = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    obs = models.TextField(blank=True)
    duracao_segundo = models.IntegerField(blank=True, null=True)
    formato_projecao_id = models.IntegerField(blank=True, null=True)
    suporte_projecao_outro = models.CharField(max_length=255, blank=True)
    janela_projecao_video = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True)
    formato_telecine_id = models.IntegerField(blank=True, null=True)
    ano_telecine = models.IntegerField(blank=True, null=True)
    legendas_outras = models.CharField(max_length=255, blank=True)
    continuista = models.CharField(max_length=255, blank=True)
    representante_id = models.IntegerField(blank=True, null=True)
    producao = models.CharField(max_length=255, blank=True)
    coord_producao = models.CharField(max_length=255, blank=True)
    assistente_producao = models.CharField(max_length=255, blank=True)
    foquista = models.CharField(max_length=255, blank=True)
    iluminador = models.CharField(max_length=255, blank=True)
    assistente_iluminacao = models.CharField(max_length=255, blank=True)
    eletricista = models.CharField(max_length=255, blank=True)
    maquinista = models.CharField(max_length=255, blank=True)
    estudio_montagem_edicao = models.CharField(max_length=255, blank=True)
    producao_arte = models.CharField(max_length=255, blank=True)
    maquiagem = models.CharField(max_length=255, blank=True)
    cabeleireiro = models.CharField(max_length=255, blank=True)
    microfonista = models.CharField(max_length=255, blank=True)
    edicao_som = models.CharField(max_length=255, blank=True)
    mixagem = models.CharField(max_length=255, blank=True)
    estudio_som = models.CharField(max_length=255, blank=True)
    trilha_musical = models.IntegerField(blank=True, null=True)
    trilha_original = models.IntegerField(blank=True, null=True)
    trilha_adaptada = models.IntegerField(blank=True, null=True)
    narracao = models.CharField(max_length=255, blank=True)
    depoimentos = models.CharField(max_length=255, blank=True)
    foto_cena = models.IntegerField(blank=True, null=True)
    foto_cena_autor = models.CharField(max_length=255, blank=True)
    foto_cena_suporte_analogico = models.CharField(max_length=50, blank=True)
    foto_cena_suporte_digital = models.CharField(max_length=50, blank=True)
    ani_tecnica = models.CharField(max_length=255, blank=True)
    ani_design = models.CharField(max_length=255, blank=True)
    ani_estudio = models.CharField(max_length=255, blank=True)
    ani_software = models.CharField(max_length=255, blank=True)
    ani_bonecos = models.CharField(max_length=255, blank=True)
    ani_cenarios = models.CharField(max_length=255, blank=True)
    ani_moldes = models.CharField(max_length=255, blank=True)
    ani_construcao = models.CharField(max_length=255, blank=True)
    ani_usinagem = models.CharField(max_length=255, blank=True)
    ani_retoques = models.CharField(max_length=255, blank=True)
    ani_vozes = models.CharField(max_length=255, blank=True)
    material_outros = models.TextField(blank=True)
    data_lancamento = models.CharField(max_length=11, blank=True)
    local_lancamento = models.CharField(max_length=255, blank=True)
    dist_contrato = models.IntegerField(blank=True, null=True)
    dist_nome = models.CharField(max_length=255, blank=True)
    dist_data_contrato = models.CharField(max_length=11, blank=True)
    dist_exclusivo = models.IntegerField(blank=True, null=True)
    pat_minc = models.IntegerField(blank=True, null=True)
    pat_minc_edital = models.CharField(max_length=255, blank=True)
    pat_minc_contrato = models.CharField(max_length=255, blank=True)
    desc_classificacao = models.TextField(blank=True)
    autor_da_trilha = models.CharField(max_length=255, blank=True)
    animador = models.CharField(max_length=255, blank=True)
    dublagem = models.TextField(blank=True)
    inscrito_pb_id = models.IntegerField(blank=True, null=True)
    infanto_juvenil = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filme'


class FilmeComentario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(max_length=200, blank=True)
    comentario = models.TextField(blank=True)
    filme = models.ForeignKey(Filme, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    comentario_pai_id = models.IntegerField(blank=True, null=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filme_comentario'


class FilmeDiretor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme = models.ForeignKey(Filme, related_name='diretores')
    diretor = models.ForeignKey(Diretor)

    class Meta:
        managed = False
        db_table = 'filme_diretor'


class FilmeImagem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=255, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    filme = models.ForeignKey(Filme, blank=True, null=True, related_name='imagens')

    class Meta:
        managed = False
        db_table = 'filme_imagem'


class FilmeInscritoPb(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'filme_inscrito_pb'


class FilmeLegenda(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme = models.ForeignKey(Filme)
    idioma = models.ForeignKey('Idioma')

    class Meta:
        managed = False
        db_table = 'filme_legenda'


class FilmeMaterialSobreFilme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme_id = models.IntegerField()
    material_sobre_filme_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filme_material_sobre_filme'


class FilmeSerie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    serie_id = models.IntegerField(blank=True, null=True)
    filme_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filme_serie'


class FilmeSuporteDisponivel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme_id = models.IntegerField()
    formato_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filme_suporte_disponivel'


class FilmeTecnicaAnimacao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme_id = models.IntegerField()
    tecnica_animacao_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filme_tecnica_animacao'


class Formato(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'formato'


class Genero(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'genero'


class GeneroSub(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'genero_sub'


class Helpdesk(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cod_help = models.IntegerField(blank=True, null=True)
    associado_id = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    assunto = models.CharField(max_length=255, blank=True)
    texto = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'helpdesk'


class Idioma(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'idioma'


class LogSistema(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.IntegerField()
    desc = models.TextField()
    date = models.DateTimeField()
    ip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'log_sistema'


class MaterialSobreFilme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'material_sobre_filme'


class Modulo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    estado = models.ForeignKey(Estado, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    estado_0 = models.CharField(db_column='estado', max_length=70, blank=True)  # Field renamed because of name conflict.
    capital = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Newsletter(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=255)
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newsletter'


class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    data_expiracao = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    matricula = models.CharField(max_length=255, blank=True)
    nome_usuario = models.CharField(max_length=255, blank=True)
    nome_beneficiario = models.CharField(max_length=255, blank=True)
    desconto = models.IntegerField(blank=True, null=True)
    taxa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    endereco = models.TextField(blank=True)
    obs = models.TextField(blank=True)
    obs_geral = models.TextField(blank=True)
    tipo_envio = models.IntegerField(blank=True, null=True)
    valor_postagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tracker_envio = models.TextField(blank=True)
    quantidade = models.IntegerField(blank=True, null=True)
    detalhe_envio = models.TextField(blank=True)
    detalhe_recebimento = models.TextField(blank=True)
    recibo = models.CharField(max_length=255, blank=True)
    cupom = models.CharField(max_length=255, blank=True)
    pago = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoHistorico(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data = models.DateTimeField(blank=True, null=True)
    pedido = models.ForeignKey(Pedido, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    texto = models.TextField(blank=True)
    email_enviado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido_historico'


class PedidoPrograma(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    programa = models.ForeignKey('Programa', blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    pedido_id = models.IntegerField(blank=True, null=True)
    tipo_usuario = models.IntegerField(blank=True, null=True)
    tipo_pedido = models.IntegerField(blank=True, null=True)
    favorito = models.IntegerField(blank=True, null=True)
    extraviado = models.IntegerField(blank=True, null=True)
    renovado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido_programa'


class PedidoStatus(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    email = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'pedido_status'


class Produtor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=16, blank=True)
    endereco = models.TextField(blank=True)
    cep = models.CharField(max_length=12, blank=True)
    tel = models.CharField(max_length=255, blank=True)
    tel2 = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'produtor'


class Programa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data = models.DateTimeField(blank=True, null=True)
    data_atua = models.DateTimeField(blank=True, null=True)
    num_serie = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True)
    tema = models.TextField(blank=True)
    descricao = models.TextField(blank=True)
    faixa_etaria = models.ForeignKey(FaixaEtaria, blank=True, null=True)
    critica = models.TextField(blank=True)
    img = models.CharField(max_length=255, blank=True)
    convenio_id = models.IntegerField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    quantidade_total = models.IntegerField(blank=True, null=True)
    recursos = models.TextField(blank=True)
    ativo = models.IntegerField(blank=True, null=True)
    novo = models.IntegerField(blank=True, null=True)
    disponivel_aquisicao = models.IntegerField(blank=True, null=True)
    disponivel_renovacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa'


class ProgramaComentario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()
    programa_id = models.IntegerField()
    comantario_pai_id = models.IntegerField()
    data = models.DateTimeField()
    filmes = models.TextField(blank=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_comentario'


class ProgramaFilme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    filme_id = models.IntegerField(blank=True, null=True)
    programa = models.ForeignKey(Programa, blank=True, null=True, related_name='filmes')
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_filme'


class ProgramaImagem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=255, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    programa = models.ForeignKey(Programa, blank=True, null=True, related_name='imagens')

    class Meta:
        managed = False
        db_table = 'programa_imagem'


class ProgramaProducao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    programa = models.ForeignKey(Programa, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    obs = models.TextField(blank=True)
    convenio_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_producao'


class ProgramaSerie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    programa = models.ForeignKey(Programa, blank=True, null=True)
    serie = models.ForeignKey('Serie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_serie'


class Publicacao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=255)
    data = models.DateTimeField()
    data_atualizacao = models.DateTimeField()
    titulo = models.CharField(max_length=255)
    chamada = models.TextField()
    texto = models.TextField()
    classe_id = models.IntegerField()
    subclasse_id = models.IntegerField(blank=True, null=True)
    sessao_id = models.IntegerField()
    autor = models.CharField(max_length=255)
    imagem = models.CharField(max_length=255, blank=True)
    tags = models.TextField(blank=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacao'


class PublicacaoClasse(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacao_classe'


class PublicacaoComentario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()
    publicacao = models.ForeignKey(Publicacao)
    comentario_pai_id = models.IntegerField()
    data = models.DateTimeField()
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacao_comentario'


class PublicacaoSubclasse(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=100, blank=True)
    classe_id = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacao_subclasse'


class Regiao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'regiao'


class Representante(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data_atual = models.DateTimeField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=16, blank=True)
    endereco = models.TextField(blank=True)
    cep = models.CharField(max_length=12, blank=True)
    tel1 = models.CharField(max_length=150, blank=True)
    tel2 = models.CharField(max_length=150, blank=True)
    tel3 = models.CharField(max_length=150, blank=True)
    email = models.CharField(unique=True, max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    adm = models.IntegerField(blank=True, null=True)
    sess = models.CharField(max_length=50, blank=True)
    grupo_id = models.IntegerField(blank=True, null=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True)
    nome_contato = models.CharField(max_length=255, blank=True)
    bloqueada = models.IntegerField(blank=True, null=True)
    confirmada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representante'


class Serie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie'


class Sessao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.IntegerField()
    ponto = models.IntegerField(blank=True, null=True)
    programa_id = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_atu = models.DateTimeField()
    website = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    exibir = models.CharField(max_length=1, blank=True)
    rel_tipo_publico = models.IntegerField(blank=True, null=True)
    rel_espectadores = models.IntegerField(blank=True, null=True)
    rel_descricao = models.TextField(blank=True)
    rel_espectadores_debate = models.IntegerField(blank=True, null=True)
    rel_debate_gravado = models.IntegerField(blank=True, null=True)
    rel_temas_debatidos = models.TextField(blank=True)
    rel_debatedores = models.TextField(blank=True)
    rel_parcerias = models.TextField(blank=True)
    rel_exibir = models.IntegerField(blank=True, null=True)
    rel_debate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessao'


class SessaoComentario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()
    sessao = models.ForeignKey(Sessao)
    comentario_pai_id = models.IntegerField()
    data = models.DateTimeField()
    cod_filmes = models.TextField(blank=True)
    exibir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessao_comentario'


class SessaoFilme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sessao_id = models.IntegerField(blank=True, null=True)
    filme_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessao_filme'


class SessaoMidia(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sessao_id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    url_thumb = models.CharField(max_length=255, blank=True)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessao_midia'


class SessaoRelatorio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sessao_id = models.IntegerField(blank=True, null=True)
    tipo_publico = models.IntegerField(blank=True, null=True)
    espectadores = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    debate = models.CharField(max_length=3, blank=True)
    espectadores_debate = models.IntegerField(blank=True, null=True)
    debate_gravado = models.IntegerField(blank=True, null=True)
    temas_debatidos = models.TextField(blank=True)
    debatedores = models.TextField(blank=True)
    parcerias = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sessao_relatorio'


class Sistema(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    chave = models.CharField(max_length=255, blank=True)
    valor = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sistema'


class Tarefa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)
    onde = models.CharField(max_length=255, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    prioridade = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_atual = models.DateTimeField(blank=True, null=True)
    data_encerrado = models.DateTimeField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    usuario = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tarefa'


class TarefaPergunta(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tarefa_id = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    texto = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'tarefa_pergunta'


class TecnicaAnimacao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tecnica_animacao'


class TempQuemAdquiriu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    data = models.DateTimeField(blank=True, null=True)
    titulo_programa = models.CharField(max_length=255, blank=True)
    programa_id = models.IntegerField(blank=True, null=True)
    num_programa = models.IntegerField(blank=True, null=True)
    estado_id = models.IntegerField(blank=True, null=True)
    municipio_id = models.IntegerField(blank=True, null=True)
    nome_ponto = models.CharField(max_length=255, blank=True)
    associado_id = models.IntegerField(blank=True, null=True)
    ponto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_quem_adquiriu'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    login = models.CharField(unique=True, max_length=50)
    nome = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=100, blank=True)
    adm = models.IntegerField()
    grupo_id = models.IntegerField()
    sess = models.CharField(max_length=50, blank=True)
    ultimo_acesso = models.DateTimeField(blank=True, null=True)
    usurem = models.CharField(max_length=255, blank=True)
    bloqueado = models.CharField(max_length=3, blank=True)
    matricula = models.CharField(max_length=50, blank=True)
    endereco = models.TextField(blank=True)
    cep = models.CharField(max_length=11, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    uf = models.CharField(max_length=3, blank=True)
    tel = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    escolaridade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioPermissao(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    modulo = models.IntegerField(blank=True, null=True)
    poder = models.IntegerField(blank=True, null=True)
    cad = models.IntegerField(blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)
    rel = models.IntegerField(blank=True, null=True)
    exc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_permissao'


class ValorLote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantidade = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valor_lote'

class Estoque(models.Model):
    num_serie = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255, db_index=True)
    qtde_online = models.IntegerField(blank=True, null=True)
    aguardando_pgto = models.IntegerField(blank=True, null=True)
    pgto_efetuado = models.IntegerField(blank=True, null=True)
    enviado = models.IntegerField(blank=True, null=True)
    qtde_estoque = models.IntegerField(blank=True, null=True)
    disponivel_aquisicao = models.IntegerField(blank=True, null=True)
    programa_id = models.IntegerField(blank=True, null=True)
    qtde_adquirida_associados = models.IntegerField(blank=True, null=True)
    qtde_doada = models.IntegerField(blank=True, null=True)
    qtde_realizador = models.IntegerField(blank=True, null=True)
    qtde_outros = models.IntegerField(blank=True, null=True)
    pedidos_pgto_confirmado = models.CharField(max_length=2500, null=True)

    @property
    def disponivel(self):
        return 'SIM' if self.disponivel_aquisicao == 1 else 'NAO'

    @property
    def total_estoque(self):
        return self.qtde_online + self.qtde_estoque

    @property
    def total_geral(self):
        return self.total_estoque + self.aguardando_pgto + self.pgto_efetuado + self.enviado

    @property
    def total_adquirido(self):
        return self.qtde_adquirida_associados + self.qtde_doada + self.qtde_realizador + self.qtde_outros

    class Meta:
        managed = False
        db_table = 'estoque'

    def save(self, **kwargs):
        raise NotImplementedError

    def save(self, **kwargs):
        raise NotImplementedError

    def delete(self, **kwargs):
        raise NotImplementedError