from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view

from .models import  Associado, AssociadoCircuito, AssociadoHistorico, AssociadoPonto, Atendimento, Circuito, CircuitoAcesso, CircuitoGrupo, CircuitoSerie, Contrato, ContratoAssinatura, ContratoDeposito, Convenio, Cupom, Curador, CuradorFilme, Diretor, Estado, Evento, FaixaEtaria, Filme, FilmeComentario, FilmeDiretor, FilmeImagem, FilmeInscritoPb, FilmeLegenda, FilmeMaterialSobreFilme, FilmeSerie, FilmeSuporteDisponivel, FilmeTecnicaAnimacao, Formato, Genero, GeneroSub, Helpdesk, Idioma, LogSistema, MaterialSobreFilme, Modulo, Municipio, Newsletter, Pedido, PedidoHistorico, PedidoPrograma, PedidoStatus, Produtor, Programa, ProgramaComentario, ProgramaFilme, ProgramaImagem, ProgramaProducao, ProgramaSerie, Publicacao, PublicacaoClasse, PublicacaoComentario, PublicacaoSubclasse, Regiao, Representante, Serie, Sessao, SessaoComentario, SessaoFilme, SessaoMidia, SessaoRelatorio, Sistema, Tarefa, TarefaPergunta, TecnicaAnimacao, TempQuemAdquiriu, Usuario, UsuarioPermissao, ValorLote
from .serializers import  AssociadoSerializer, AssociadoCircuitoSerializer, AssociadoHistoricoSerializer, AssociadoPontoSerializer, AtendimentoSerializer, CircuitoSerializer, CircuitoAcessoSerializer, CircuitoGrupoSerializer, CircuitoSerieSerializer, ContratoSerializer, ContratoAssinaturaSerializer, ContratoDepositoSerializer, ConvenioSerializer, CupomSerializer, CuradorSerializer, CuradorFilmeSerializer, DiretorSerializer, EstadoSerializer, EventoSerializer, FaixaEtariaSerializer, FilmeSerializer, FilmeComentarioSerializer, FilmeDiretorSerializer, FilmeImagemSerializer, FilmeInscritoPbSerializer, FilmeLegendaSerializer, FilmeMaterialSobreFilmeSerializer, FilmeSerieSerializer, FilmeSuporteDisponivelSerializer, FilmeTecnicaAnimacaoSerializer, FormatoSerializer, GeneroSerializer, GeneroSubSerializer, HelpdeskSerializer, IdiomaSerializer, LogSistemaSerializer, MaterialSobreFilmeSerializer, ModuloSerializer, MunicipioSerializer, NewsletterSerializer, PedidoSerializer, PedidoHistoricoSerializer, PedidoProgramaSerializer, PedidoStatusSerializer, ProdutorSerializer, ProgramaSerializer, ProgramaComentarioSerializer, ProgramaFilmeSerializer, ProgramaImagemSerializer, ProgramaProducaoSerializer, ProgramaSerieSerializer, PublicacaoSerializer, PublicacaoClasseSerializer, PublicacaoComentarioSerializer, PublicacaoSubclasseSerializer, RegiaoSerializer, RepresentanteSerializer, SerieSerializer, SessaoSerializer, SessaoComentarioSerializer, SessaoFilmeSerializer, SessaoMidiaSerializer, SessaoRelatorioSerializer, SistemaSerializer, TarefaSerializer, TarefaPerguntaSerializer, TecnicaAnimacaoSerializer, TempQuemAdquiriuSerializer, UsuarioSerializer, UsuarioPermissaoSerializer, ValorLoteSerializer

class AssociadoViewSet(viewsets.ModelViewSet): 
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer
 
class AssociadoCircuitoViewSet(viewsets.ModelViewSet): 
    queryset = AssociadoCircuito.objects.all()
    serializer_class = AssociadoCircuitoSerializer
 
class AssociadoHistoricoViewSet(viewsets.ModelViewSet): 
    queryset = AssociadoHistorico.objects.all()
    serializer_class = AssociadoHistoricoSerializer
 
class AssociadoPontoViewSet(viewsets.ModelViewSet): 
    queryset = AssociadoPonto.objects.all()
    serializer_class = AssociadoPontoSerializer
 
class AtendimentoViewSet(viewsets.ModelViewSet): 
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer
 
class CircuitoViewSet(viewsets.ModelViewSet): 
    queryset = Circuito.objects.all()
    serializer_class = CircuitoSerializer
 
class CircuitoAcessoViewSet(viewsets.ModelViewSet): 
    queryset = CircuitoAcesso.objects.all()
    serializer_class = CircuitoAcessoSerializer
 
class CircuitoGrupoViewSet(viewsets.ModelViewSet): 
    queryset = CircuitoGrupo.objects.all()
    serializer_class = CircuitoGrupoSerializer
 
class CircuitoSerieViewSet(viewsets.ModelViewSet): 
    queryset = CircuitoSerie.objects.all()
    serializer_class = CircuitoSerieSerializer
 
class ContratoViewSet(viewsets.ModelViewSet): 
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
 
class ContratoAssinaturaViewSet(viewsets.ModelViewSet): 
    queryset = ContratoAssinatura.objects.all()
    serializer_class = ContratoAssinaturaSerializer
 
class ContratoDepositoViewSet(viewsets.ModelViewSet): 
    queryset = ContratoDeposito.objects.all()
    serializer_class = ContratoDepositoSerializer
 
class ConvenioViewSet(viewsets.ModelViewSet): 
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
 
class CupomViewSet(viewsets.ModelViewSet): 
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer
 
class CuradorViewSet(viewsets.ModelViewSet): 
    queryset = Curador.objects.all()
    serializer_class = CuradorSerializer
 
class CuradorFilmeViewSet(viewsets.ModelViewSet): 
    queryset = CuradorFilme.objects.all()
    serializer_class = CuradorFilmeSerializer
 
class DiretorViewSet(viewsets.ModelViewSet): 
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer
 
class EstadoViewSet(viewsets.ModelViewSet): 
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
 
class EventoViewSet(viewsets.ModelViewSet): 
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
 
class FaixaEtariaViewSet(viewsets.ModelViewSet): 
    queryset = FaixaEtaria.objects.all()
    serializer_class = FaixaEtariaSerializer
 
class FilmeViewSet(viewsets.ModelViewSet): 
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
 
class FilmeComentarioViewSet(viewsets.ModelViewSet): 
    queryset = FilmeComentario.objects.all()
    serializer_class = FilmeComentarioSerializer
 
class FilmeDiretorViewSet(viewsets.ModelViewSet): 
    queryset = FilmeDiretor.objects.all()
    serializer_class = FilmeDiretorSerializer
 
class FilmeImagemViewSet(viewsets.ModelViewSet): 
    queryset = FilmeImagem.objects.all()
    serializer_class = FilmeImagemSerializer
 
class FilmeInscritoPbViewSet(viewsets.ModelViewSet): 
    queryset = FilmeInscritoPb.objects.all()
    serializer_class = FilmeInscritoPbSerializer
 
class FilmeLegendaViewSet(viewsets.ModelViewSet): 
    queryset = FilmeLegenda.objects.all()
    serializer_class = FilmeLegendaSerializer
 
class FilmeMaterialSobreFilmeViewSet(viewsets.ModelViewSet): 
    queryset = FilmeMaterialSobreFilme.objects.all()
    serializer_class = FilmeMaterialSobreFilmeSerializer
 
class FilmeSerieViewSet(viewsets.ModelViewSet): 
    queryset = FilmeSerie.objects.all()
    serializer_class = FilmeSerieSerializer
 
class FilmeSuporteDisponivelViewSet(viewsets.ModelViewSet): 
    queryset = FilmeSuporteDisponivel.objects.all()
    serializer_class = FilmeSuporteDisponivelSerializer
 
class FilmeTecnicaAnimacaoViewSet(viewsets.ModelViewSet): 
    queryset = FilmeTecnicaAnimacao.objects.all()
    serializer_class = FilmeTecnicaAnimacaoSerializer
 
class FormatoViewSet(viewsets.ModelViewSet): 
    queryset = Formato.objects.all()
    serializer_class = FormatoSerializer
 
class GeneroViewSet(viewsets.ModelViewSet): 
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
 
class GeneroSubViewSet(viewsets.ModelViewSet): 
    queryset = GeneroSub.objects.all()
    serializer_class = GeneroSubSerializer
 
class HelpdeskViewSet(viewsets.ModelViewSet): 
    queryset = Helpdesk.objects.all()
    serializer_class = HelpdeskSerializer
 
class IdiomaViewSet(viewsets.ModelViewSet): 
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
 
class LogSistemaViewSet(viewsets.ModelViewSet): 
    queryset = LogSistema.objects.all()
    serializer_class = LogSistemaSerializer
 
class MaterialSobreFilmeViewSet(viewsets.ModelViewSet): 
    queryset = MaterialSobreFilme.objects.all()
    serializer_class = MaterialSobreFilmeSerializer
 
class ModuloViewSet(viewsets.ModelViewSet): 
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
 
class MunicipioViewSet(viewsets.ModelViewSet): 
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
 
class NewsletterViewSet(viewsets.ModelViewSet): 
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
 
class PedidoViewSet(viewsets.ModelViewSet): 
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
 
class PedidoHistoricoViewSet(viewsets.ModelViewSet): 
    queryset = PedidoHistorico.objects.all()
    serializer_class = PedidoHistoricoSerializer
 
class PedidoProgramaViewSet(viewsets.ModelViewSet): 
    queryset = PedidoPrograma.objects.all()
    serializer_class = PedidoProgramaSerializer
 
class PedidoStatusViewSet(viewsets.ModelViewSet): 
    queryset = PedidoStatus.objects.all()
    serializer_class = PedidoStatusSerializer
 
class ProdutorViewSet(viewsets.ModelViewSet): 
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
 
class ProgramaViewSet(viewsets.ModelViewSet): 
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
 
class ProgramaComentarioViewSet(viewsets.ModelViewSet): 
    queryset = ProgramaComentario.objects.all()
    serializer_class = ProgramaComentarioSerializer
 
class ProgramaFilmeViewSet(viewsets.ModelViewSet): 
    queryset = ProgramaFilme.objects.all()
    serializer_class = ProgramaFilmeSerializer
 
class ProgramaImagemViewSet(viewsets.ModelViewSet): 
    queryset = ProgramaImagem.objects.all()
    serializer_class = ProgramaImagemSerializer
 
class ProgramaProducaoViewSet(viewsets.ModelViewSet): 
    queryset = ProgramaProducao.objects.all()
    serializer_class = ProgramaProducaoSerializer
 
class ProgramaSerieViewSet(viewsets.ModelViewSet): 
    queryset = ProgramaSerie.objects.all()
    serializer_class = ProgramaSerieSerializer
 
class PublicacaoViewSet(viewsets.ModelViewSet): 
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
 
class PublicacaoClasseViewSet(viewsets.ModelViewSet): 
    queryset = PublicacaoClasse.objects.all()
    serializer_class = PublicacaoClasseSerializer
 
class PublicacaoComentarioViewSet(viewsets.ModelViewSet): 
    queryset = PublicacaoComentario.objects.all()
    serializer_class = PublicacaoComentarioSerializer
 
class PublicacaoSubclasseViewSet(viewsets.ModelViewSet): 
    queryset = PublicacaoSubclasse.objects.all()
    serializer_class = PublicacaoSubclasseSerializer
 
class RegiaoViewSet(viewsets.ModelViewSet): 
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
 
class RepresentanteViewSet(viewsets.ModelViewSet): 
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer
 
class SerieViewSet(viewsets.ModelViewSet): 
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
 
class SessaoViewSet(viewsets.ModelViewSet): 
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
 
class SessaoComentarioViewSet(viewsets.ModelViewSet): 
    queryset = SessaoComentario.objects.all()
    serializer_class = SessaoComentarioSerializer
 
class SessaoFilmeViewSet(viewsets.ModelViewSet): 
    queryset = SessaoFilme.objects.all()
    serializer_class = SessaoFilmeSerializer
 
class SessaoMidiaViewSet(viewsets.ModelViewSet): 
    queryset = SessaoMidia.objects.all()
    serializer_class = SessaoMidiaSerializer
 
class SessaoRelatorioViewSet(viewsets.ModelViewSet): 
    queryset = SessaoRelatorio.objects.all()
    serializer_class = SessaoRelatorioSerializer
 
class SistemaViewSet(viewsets.ModelViewSet): 
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer
 
class TarefaViewSet(viewsets.ModelViewSet): 
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
 
class TarefaPerguntaViewSet(viewsets.ModelViewSet): 
    queryset = TarefaPergunta.objects.all()
    serializer_class = TarefaPerguntaSerializer
 
class TecnicaAnimacaoViewSet(viewsets.ModelViewSet): 
    queryset = TecnicaAnimacao.objects.all()
    serializer_class = TecnicaAnimacaoSerializer
 
class TempQuemAdquiriuViewSet(viewsets.ModelViewSet): 
    queryset = TempQuemAdquiriu.objects.all()
    serializer_class = TempQuemAdquiriuSerializer
 
class UsuarioViewSet(viewsets.ModelViewSet): 
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
 
class UsuarioPermissaoViewSet(viewsets.ModelViewSet): 
    queryset = UsuarioPermissao.objects.all()
    serializer_class = UsuarioPermissaoSerializer
 
class ValorLoteViewSet(viewsets.ModelViewSet): 
    queryset = ValorLote.objects.all()
    serializer_class = ValorLoteSerializer
