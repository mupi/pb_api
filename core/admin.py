from django.contrib import admin

from core.models import *

class AssociadoAdmin(admin.ModelAdmin):
    model = Associado
    list_display = ('id', 'matricula')

admin.site.register(Associado, AssociadoAdmin)

class AssociadoCircuitoAdmin(admin.ModelAdmin):
    model = AssociadoCircuito
    list_display = ('id', 'circuito_id', 'associado_id')

admin.site.register(AssociadoCircuito, AssociadoCircuitoAdmin)

class AssociadoHistoricoAdmin(admin.ModelAdmin):
    model = AssociadoHistorico
    list_display = ('id', 'associado_id')

admin.site.register(AssociadoHistorico, AssociadoHistoricoAdmin)

class AssociadoPontoAdmin(admin.ModelAdmin):
    model = AssociadoPonto
    list_display = ('id', 'nome')

admin.site.register(AssociadoPonto, AssociadoPontoAdmin)

class AtendimentoAdmin(admin.ModelAdmin):
    model = Atendimento
    list_display = ('id', 'usr_nome')

admin.site.register(Atendimento, AtendimentoAdmin)

class CircuitoAdmin(admin.ModelAdmin):
    model = Circuito
    list_display = ('id', 'nome')

admin.site.register(Circuito, CircuitoAdmin)

class CircuitoAcessoAdmin(admin.ModelAdmin):
    model = CircuitoAcesso
    list_display = ('id', 'nome')

admin.site.register(CircuitoAcesso, CircuitoAcessoAdmin)

class CircuitoGrupoAdmin(admin.ModelAdmin):
    model = CircuitoGrupo
    list_display = ('id', 'nome')

admin.site.register(CircuitoGrupo, CircuitoGrupoAdmin)

class CircuitoSerieAdmin(admin.ModelAdmin):
    model = CircuitoSerie
    list_display = ('id', 'circuito_id', 'serie_id')

admin.site.register(CircuitoSerie, CircuitoSerieAdmin)

class ContratoAdmin(admin.ModelAdmin):
    model = Contrato
    list_display = ('id', 'filme_id')

admin.site.register(Contrato, ContratoAdmin)

class ContratoAssinaturaAdmin(admin.ModelAdmin):
    model = ContratoAssinatura
    list_display = ('id', 'contrato_id', 'numero')

admin.site.register(ContratoAssinatura, ContratoAssinaturaAdmin)


class ContratoDepositoAdmin(admin.ModelAdmin):
    model = ContratoDeposito
    list_display = ('id', 'contrato', 'nome')

admin.site.register(ContratoDeposito, ContratoDepositoAdmin)

class ConvenioAdmin(admin.ModelAdmin):
    model = Convenio
    list_display = ('id', 'nome')

admin.site.register(Convenio, ConvenioAdmin)

class CupomAdmin(admin.ModelAdmin):
    model = Cupom
    list_display = ('id', 'cupom')

admin.site.register(Cupom, CupomAdmin)

class CuradorAdmin(admin.ModelAdmin):
    model = Curador
    list_display = ('id', 'nome', 'nome_artistico')

admin.site.register(Curador, CuradorAdmin)

class CuradorFilmeAdmin(admin.ModelAdmin):
    model = CuradorFilme
    list_display = ('id', 'filme_id', 'curador')

admin.site.register(CuradorFilme, CuradorFilmeAdmin)

class DiretorAdmin(admin.ModelAdmin):
    model = Diretor
    list_display = ('id', 'nome', 'nome_artistico')

admin.site.register(Diretor, DiretorAdmin)

class EstadoAdmin(admin.ModelAdmin):
    model = Estado
    list_display = ('id', 'uf')

admin.site.register(Estado, EstadoAdmin)

class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = ('id', 'titulo')

admin.site.register(Evento, EventoAdmin)

class FaixaEtariaAdmin(admin.ModelAdmin):
    model = FaixaEtaria
    list_display = ('id', 'nome')

admin.site.register(FaixaEtaria, FaixaEtariaAdmin)

class FilmeAdmin(admin.ModelAdmin):
    model = Filme
    list_display = ('id', 'titulo')

admin.site.register(Filme, FilmeAdmin)

class FilmeComentarioAdmin(admin.ModelAdmin):
    model = FilmeComentario
    list_display = ('id', 'titulo', 'filme')

admin.site.register(FilmeComentario, FilmeComentarioAdmin)

class FilmeDiretorAdmin(admin.ModelAdmin):
    model = FilmeDiretor
    list_display = ('id', 'filme', 'diretor')

admin.site.register(FilmeDiretor, FilmeDiretorAdmin)

class FilmeImagemAdmin(admin.ModelAdmin):
    model = FilmeImagem
    list_display = ('id', 'filme', 'tipo')

admin.site.register(FilmeImagem, FilmeImagemAdmin)

class FilmeInscritoPbAdmin(admin.ModelAdmin):
    model = FilmeInscritoPb
    list_display = ('id', 'nome')

admin.site.register(FilmeInscritoPb, FilmeInscritoPbAdmin)

class FilmeLegendaAdmin(admin.ModelAdmin):
    model = FilmeLegenda
    list_display = ('id', 'filme', 'idioma')

admin.site.register(FilmeLegenda, FilmeLegendaAdmin)

class FilmeMaterialSobreFilmeAdmin(admin.ModelAdmin):
    model = FilmeMaterialSobreFilme
    list_display = ('id', 'filme_id', 'material_sobre_filme_id')

admin.site.register(FilmeMaterialSobreFilme, FilmeMaterialSobreFilmeAdmin)

class FilmeSerieAdmin(admin.ModelAdmin):
    model = FilmeSerie
    list_display = ('id', 'filme_id', 'serie_id')

admin.site.register(FilmeSerie, FilmeSerieAdmin)

class FilmeSuporteDisponivelAdmin(admin.ModelAdmin):
    model = FilmeSuporteDisponivel
    list_display = ('id', 'filme_id', 'formato_id')

admin.site.register(FilmeSuporteDisponivel, FilmeSuporteDisponivelAdmin)

class FilmeTecnicaAnimacaoAdmin(admin.ModelAdmin):
    model = FilmeTecnicaAnimacao
    list_display = ('id', 'filme_id', 'tecnica_animacao_id')

admin.site.register(FilmeTecnicaAnimacao, FilmeTecnicaAnimacaoAdmin)

class FormatoAdmin(admin.ModelAdmin):
    model = Formato
    list_display = ('id', 'nome', 'descricao')

admin.site.register(Formato, FormatoAdmin)

class GeneroAdmin(admin.ModelAdmin):
    model = Genero
    list_display = ('id', 'nome', 'descricao')

admin.site.register(Genero, GeneroAdmin)

class GeneroSubAdmin(admin.ModelAdmin):
    model = GeneroSub
    list_display = ('id', 'nome', 'descricao')

admin.site.register(GeneroSub, GeneroSubAdmin)

class HelpdeskAdmin(admin.ModelAdmin):
    model = Helpdesk
    list_display = ('id', 'associado_id', 'data')

admin.site.register(Helpdesk, HelpdeskAdmin)

class IdiomaAdmin(admin.ModelAdmin):
    model = Helpdesk
    list_display = ('id', 'nome')

admin.site.register(Idioma, IdiomaAdmin)

class LogSistemaAdmin(admin.ModelAdmin):
    model = LogSistema
    list_display = ('id', 'status', 'date')

admin.site.register(LogSistema, LogSistemaAdmin)

class MaterialSobreFilmeAdmin(admin.ModelAdmin):
    model = MaterialSobreFilme
    list_display = ('id', 'nome')

admin.site.register(MaterialSobreFilme, MaterialSobreFilmeAdmin)

class ModuloAdmin(admin.ModelAdmin):
    model = MaterialSobreFilme
    list_display = ('id', 'nome')

admin.site.register(Modulo, ModuloAdmin)

class MunicipioAdmin(admin.ModelAdmin):
    model = Municipio
    list_display = ('id', 'nome', 'estado')

admin.site.register(Municipio, MunicipioAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    model = Municipio
    list_display = ('id', 'email', 'tipo')

admin.site.register(Newsletter, NewsletterAdmin)

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    list_display = ('id', 'status', 'tipo', 'usuario_id', 'matricula', 'nome_usuario')

admin.site.register(Pedido, PedidoAdmin)

class PedidoHistoricoAdmin(admin.ModelAdmin):
    model = PedidoHistorico
    list_display = ('id', 'data', 'pedido', 'status')

admin.site.register(PedidoHistorico, PedidoHistoricoAdmin)

class PedidoProgramaAdmin(admin.ModelAdmin):
    model = PedidoPrograma
    list_display = ('id', 'programa', 'usuario_id', 'pedido_id')

admin.site.register(PedidoPrograma, PedidoProgramaAdmin)

class PedidoStatusAdmin(admin.ModelAdmin):
    model = PedidoStatus
    list_display = ('id', 'nome', 'descricao')

admin.site.register(PedidoStatus, PedidoStatusAdmin)

class ProdutorAdmin(admin.ModelAdmin):
    model = Produtor
    list_display = ('id', 'nome', 'email')

admin.site.register(Produtor, ProdutorAdmin)

class ProgramaAdmin(admin.ModelAdmin):
    model = Programa
    list_display = ('id', 'data', 'titulo')

admin.site.register(Programa, ProgramaAdmin)

class ProgramaComentarioAdmin(admin.ModelAdmin):
    model = ProgramaComentario
    list_display = ('id', 'programa_id', 'titulo')

admin.site.register(ProgramaComentario, ProgramaComentarioAdmin)

class ProgramaFilmeAdmin(admin.ModelAdmin):
    model = ProgramaFilme
    list_display = ('id', 'filme_id', 'programa')

admin.site.register(ProgramaFilme, ProgramaFilmeAdmin)

class ProgramaImagemAdmin(admin.ModelAdmin):
    model = ProgramaImagem
    list_display = ('id', 'tipo', 'programa')

admin.site.register(ProgramaImagem, ProgramaImagemAdmin)

class ProgramaProducaoAdmin(admin.ModelAdmin):
    model = ProgramaProducao
    list_display = ('id', 'convenio_id', 'programa')

admin.site.register(ProgramaProducao, ProgramaProducaoAdmin)

class ProgramaSerieAdmin(admin.ModelAdmin):
    model = ProgramaSerie
    list_display = ('id', 'serie', 'programa')

admin.site.register(ProgramaSerie, ProgramaSerieAdmin)

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    list_display = ('id', 'data', 'titulo')

admin.site.register(Publicacao, PublicacaoAdmin)


class PublicacaoClasseAdmin(admin.ModelAdmin):
    model = PublicacaoClasse
    list_display = ('id', 'nome')

admin.site.register(PublicacaoClasse, PublicacaoClasseAdmin)

class PublicacaoComentarioAdmin(admin.ModelAdmin):
    model = PublicacaoComentario
    list_display = ('id', 'titulo')

admin.site.register(PublicacaoComentario, PublicacaoComentarioAdmin)

class PublicacaoSubclasseAdmin(admin.ModelAdmin):
    model = PublicacaoSubclasse
    list_display = ('id', 'nome', 'classe_id')

admin.site.register(PublicacaoSubclasse, PublicacaoSubclasseAdmin)

class RegiaoAdmin(admin.ModelAdmin):
    model = Regiao
    list_display = ('id', 'nome')

admin.site.register(Regiao, RegiaoAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    model = Representante
    list_display = ('id', 'nome')

admin.site.register(Representante, RepresentanteAdmin)

class SerieAdmin(admin.ModelAdmin):
    model = Serie
    list_display = ('id', 'nome')

admin.site.register(Serie, SerieAdmin)

class SessaoAdmin(admin.ModelAdmin):
    model = Sessao
    list_display = ('id', 'titulo')

admin.site.register(Sessao, SessaoAdmin)

class SessaoComentarioAdmin(admin.ModelAdmin):
    model = SessaoComentario
    list_display = ('id', 'titulo', 'sessao', 'comentario')

admin.site.register(SessaoComentario, SessaoComentarioAdmin)

class SessaoFilmeAdmin(admin.ModelAdmin):
    model = SessaoFilme
    list_display = ('id', 'sessao_id', 'filme_id')

admin.site.register(SessaoFilme, SessaoFilmeAdmin)

class SessaoMidiaAdmin(admin.ModelAdmin):
    model = SessaoMidia
    list_display = ('id', 'sessao_id', 'url')

admin.site.register(SessaoMidia, SessaoMidiaAdmin)

class SessaoRelatorioAdmin(admin.ModelAdmin):
    model = SessaoRelatorio
    list_display = ('id', 'sessao_id')

admin.site.register(SessaoRelatorio, SessaoRelatorioAdmin)


class SistemaAdmin(admin.ModelAdmin):
    model = Sistema
    list_display = ('id', 'chave', 'valor')

admin.site.register(Sistema, SistemaAdmin)

class TarefaAdmin(admin.ModelAdmin):
    model = Tarefa
    list_display = ('id', 'nome', 'usuario')

admin.site.register(Tarefa, TarefaAdmin)

class TarefaPerguntaAdmin(admin.ModelAdmin):
    model = TarefaPergunta
    list_display = ('id', 'tarefa_id', 'data')

admin.site.register(TarefaPergunta, TarefaPerguntaAdmin)

class TecnicaAnimacaoAdmin(admin.ModelAdmin):
    model = TecnicaAnimacao
    list_display = ('id', 'nome')

admin.site.register(TecnicaAnimacao, TecnicaAnimacaoAdmin)


class TempQuemAdquiriuAdmin(admin.ModelAdmin):
    model = TempQuemAdquiriu    
    list_display = ('id', 'associado_id')

admin.site.register(TempQuemAdquiriu, TempQuemAdquiriuAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario    
    list_display = ('id', 'login', 'nome')

admin.site.register(Usuario, UsuarioAdmin)


class UsuarioPermissaoAdmin(admin.ModelAdmin):
    model = UsuarioPermissao    
    list_display = ('id', 'usuario', 'modulo')

admin.site.register(UsuarioPermissao, UsuarioPermissaoAdmin)


class ValorLoteAdmin(admin.ModelAdmin):
    model = ValorLote    
    list_display = ('id', 'quantidade', 'valor')

admin.site.register(ValorLote, ValorLoteAdmin)

class EstoqueAdmin(admin.ModelAdmin):
    name = "Estoque"
    list_display = ('disponivel', 'num_serie', 'titulo', 'qtde_online', 'aguardando_pagamento', 'pagamento_efetuado', 'enviado', 'quantidade_estoque', 'total', 'total_geral')
    ordering = ('num_serie',)

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Estoque, EstoqueAdmin)