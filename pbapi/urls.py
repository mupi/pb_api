from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import  AssociadoViewSet, AssociadoCircuitoViewSet, AssociadoHistoricoViewSet, AssociadoPontoViewSet, AtendimentoViewSet, CircuitoViewSet, CircuitoAcessoViewSet, CircuitoGrupoViewSet, CircuitoSerieViewSet, ContratoViewSet, ContratoAssinaturaViewSet, ContratoDepositoViewSet, ConvenioViewSet, CupomViewSet, CuradorViewSet, CuradorFilmeViewSet, DiretorViewSet, EstadoViewSet, EventoViewSet, FaixaEtariaViewSet, FilmeViewSet, FilmeComentarioViewSet, FilmeDiretorViewSet, FilmeImagemViewSet, FilmeInscritoPbViewSet, FilmeLegendaViewSet, FilmeMaterialSobreFilmeViewSet, FilmeSerieViewSet, FilmeSuporteDisponivelViewSet, FilmeTecnicaAnimacaoViewSet, FormatoViewSet, GeneroViewSet, GeneroSubViewSet, HelpdeskViewSet, IdiomaViewSet, LogSistemaViewSet, MaterialSobreFilmeViewSet, ModuloViewSet, MunicipioViewSet, NewsletterViewSet, PedidoViewSet, PedidoHistoricoViewSet, PedidoProgramaViewSet, PedidoStatusViewSet, ProdutorViewSet, ProgramaViewSet, ProgramaComentarioViewSet, ProgramaFilmeViewSet, ProgramaImagemViewSet, ProgramaProducaoViewSet, ProgramaSerieViewSet, PublicacaoViewSet, PublicacaoClasseViewSet, PublicacaoComentarioViewSet, PublicacaoSubclasseViewSet, RegiaoViewSet, RepresentanteViewSet, SerieViewSet, SessaoViewSet, SessaoComentarioViewSet, SessaoFilmeViewSet, SessaoMidiaViewSet, SessaoRelatorioViewSet, SistemaViewSet, TarefaViewSet, TarefaPerguntaViewSet, TecnicaAnimacaoViewSet, TempQuemAdquiriuViewSet, UsuarioViewSet, UsuarioPermissaoViewSet, ValorLoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'associado',  AssociadoViewSet, 'AssociadoList')
router.register(r'associadocircuito',  AssociadoCircuitoViewSet, 'AssociadoCircuitoList')
router.register(r'associadohistorico',  AssociadoHistoricoViewSet, 'AssociadoHistoricoList')
router.register(r'associadoponto',  AssociadoPontoViewSet, 'AssociadoPontoList')
router.register(r'atendimento',  AtendimentoViewSet, 'AtendimentoList')
router.register(r'circuito',  CircuitoViewSet, 'CircuitoList')
router.register(r'circuitoacesso',  CircuitoAcessoViewSet, 'CircuitoAcessoList')
router.register(r'circuitogrupo',  CircuitoGrupoViewSet, 'CircuitoGrupoList')
router.register(r'circuitoserie',  CircuitoSerieViewSet, 'CircuitoSerieList')
router.register(r'contrato',  ContratoViewSet, 'ContratoList')
router.register(r'contratoassinatura',  ContratoAssinaturaViewSet, 'ContratoAssinaturaList')
router.register(r'contratodeposito',  ContratoDepositoViewSet, 'ContratoDepositoList')
router.register(r'convenio',  ConvenioViewSet, 'ConvenioList')
router.register(r'cupom',  CupomViewSet, 'CupomList')
router.register(r'curador',  CuradorViewSet, 'CuradorList')
router.register(r'curadorfilme',  CuradorFilmeViewSet, 'CuradorFilmeList')
router.register(r'diretor',  DiretorViewSet, 'DiretorList')
router.register(r'estado',  EstadoViewSet, 'EstadoList')
router.register(r'evento',  EventoViewSet, 'EventoList')
router.register(r'faixaetaria',  FaixaEtariaViewSet, 'FaixaEtariaList')
router.register(r'filme',  FilmeViewSet, 'FilmeList')
router.register(r'filmecomentario',  FilmeComentarioViewSet, 'FilmeComentarioList')
router.register(r'filmediretor',  FilmeDiretorViewSet, 'FilmeDiretorList')
router.register(r'filmeimagem',  FilmeImagemViewSet, 'FilmeImagemList')
router.register(r'filmeinscritopb',  FilmeInscritoPbViewSet, 'FilmeInscritoPbList')
router.register(r'filmelegenda',  FilmeLegendaViewSet, 'FilmeLegendaList')
router.register(r'filmematerialsobrefilme',  FilmeMaterialSobreFilmeViewSet, 'FilmeMaterialSobreFilmeList')
router.register(r'filmeserie',  FilmeSerieViewSet, 'FilmeSerieList')
router.register(r'filmesuportedisponivel',  FilmeSuporteDisponivelViewSet, 'FilmeSuporteDisponivelList')
router.register(r'filmetecnicaanimacao',  FilmeTecnicaAnimacaoViewSet, 'FilmeTecnicaAnimacaoList')
router.register(r'formato',  FormatoViewSet, 'FormatoList')
router.register(r'genero',  GeneroViewSet, 'GeneroList')
router.register(r'generosub',  GeneroSubViewSet, 'GeneroSubList')
router.register(r'helpdesk',  HelpdeskViewSet, 'HelpdeskList')
router.register(r'idioma',  IdiomaViewSet, 'IdiomaList')
router.register(r'logsistema',  LogSistemaViewSet, 'LogSistemaList')
router.register(r'materialsobrefilme',  MaterialSobreFilmeViewSet, 'MaterialSobreFilmeList')
router.register(r'modulo',  ModuloViewSet, 'ModuloList')
router.register(r'municipio',  MunicipioViewSet, 'MunicipioList')
router.register(r'newsletter',  NewsletterViewSet, 'NewsletterList')
router.register(r'pedido',  PedidoViewSet, 'PedidoList')
router.register(r'pedidohistorico',  PedidoHistoricoViewSet, 'PedidoHistoricoList')
router.register(r'pedidoprograma',  PedidoProgramaViewSet, 'PedidoProgramaList')
router.register(r'pedidostatus',  PedidoStatusViewSet, 'PedidoStatusList')
router.register(r'produtor',  ProdutorViewSet, 'ProdutorList')
router.register(r'programa',  ProgramaViewSet, 'ProgramaList')
router.register(r'programacomentario',  ProgramaComentarioViewSet, 'ProgramaComentarioList')
router.register(r'programafilme',  ProgramaFilmeViewSet, 'ProgramaFilmeList')
router.register(r'programaimagem',  ProgramaImagemViewSet, 'ProgramaImagemList')
router.register(r'programaproducao',  ProgramaProducaoViewSet, 'ProgramaProducaoList')
router.register(r'programaserie',  ProgramaSerieViewSet, 'ProgramaSerieList')
router.register(r'publicacao',  PublicacaoViewSet, 'PublicacaoList')
router.register(r'publicacaoclasse',  PublicacaoClasseViewSet, 'PublicacaoClasseList')
router.register(r'publicacaocomentario',  PublicacaoComentarioViewSet, 'PublicacaoComentarioList')
router.register(r'publicacaosubclasse',  PublicacaoSubclasseViewSet, 'PublicacaoSubclasseList')
router.register(r'regiao',  RegiaoViewSet, 'RegiaoList')
router.register(r'representante',  RepresentanteViewSet, 'RepresentanteList')
router.register(r'serie',  SerieViewSet, 'SerieList')
router.register(r'sessao',  SessaoViewSet, 'SessaoList')
router.register(r'sessaocomentario',  SessaoComentarioViewSet, 'SessaoComentarioList')
router.register(r'sessaofilme',  SessaoFilmeViewSet, 'SessaoFilmeList')
router.register(r'sessaomidia',  SessaoMidiaViewSet, 'SessaoMidiaList')
router.register(r'sessaorelatorio',  SessaoRelatorioViewSet, 'SessaoRelatorioList')
router.register(r'sistema',  SistemaViewSet, 'SistemaList')
router.register(r'tarefa',  TarefaViewSet, 'TarefaList')
router.register(r'tarefapergunta',  TarefaPerguntaViewSet, 'TarefaPerguntaList')
router.register(r'tecnicaanimacao',  TecnicaAnimacaoViewSet, 'TecnicaAnimacaoList')
router.register(r'tempquemadquiriu',  TempQuemAdquiriuViewSet, 'TempQuemAdquiriuList')
router.register(r'usuario',  UsuarioViewSet, 'UsuarioList')
router.register(r'usuariopermissao',  UsuarioPermissaoViewSet, 'UsuarioPermissaoList')
router.register(r'valorlote',  ValorLoteViewSet, 'ValorLoteList')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += router.urls

admin.autodiscover()
