from rest_framework import serializers

from .models import  *

class AssociadoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Associado
 
class AssociadoCircuitoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AssociadoCircuito
 
class AssociadoHistoricoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AssociadoHistorico
 
class AssociadoPontoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AssociadoPonto
 
class AtendimentoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Atendimento
 
class CircuitoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Circuito
 
class CircuitoAcessoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CircuitoAcesso
 
class CircuitoGrupoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CircuitoGrupo
 
class CircuitoSerieSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CircuitoSerie
 
class ContratoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contrato
 
class ContratoAssinaturaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ContratoAssinatura
 
class ContratoDepositoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ContratoDeposito
 
class ConvenioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Convenio
 
class CupomSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cupom
 
class CuradorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Curador
 
class CuradorFilmeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CuradorFilme
 
class DiretorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Diretor
 
class EstadoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Estado
 
class EventoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Evento
 
class FaixaEtariaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FaixaEtaria
 

class FilmeComentarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeComentario
 
class FilmeDiretorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeDiretor
 
class FilmeImagemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeImagem
 
class FilmeInscritoPbSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeInscritoPb
 
class FilmeLegendaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeLegenda
 
class FilmeMaterialSobreFilmeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeMaterialSobreFilme
 
class FilmeSerieSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeSerie
 
class FilmeSuporteDisponivelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeSuporteDisponivel
 
class FilmeTecnicaAnimacaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FilmeTecnicaAnimacao

class FilmeSerializer(serializers.ModelSerializer): 
    imagens = FilmeImagemSerializer(many=True, read_only=True)
    diretores = FilmeDiretorSerializer(many=True, read_only=True)
    class Meta:
        model = Filme

class FormatoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Formato
 
class GeneroSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genero
 
class GeneroSubSerializer(serializers.ModelSerializer): 
    class Meta:
        model = GeneroSub
 
class HelpdeskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Helpdesk
 
class IdiomaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Idioma
 
class LogSistemaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = LogSistema
 
class MaterialSobreFilmeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MaterialSobreFilme
 
class ModuloSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Modulo
 
class MunicipioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Municipio
 
class NewsletterSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Newsletter
 
class PedidoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Pedido
 
class PedidoHistoricoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PedidoHistorico
 
class PedidoProgramaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PedidoPrograma
 
class PedidoStatusSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PedidoStatus
 
class ProdutorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Produtor
 
class ProgramaComentarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProgramaComentario
 
class ProgramaFilmeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProgramaFilme
 
class ProgramaImagemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProgramaImagem
 
class ProgramaSerializer(serializers.ModelSerializer): 
    filmes = ProgramaFilmeSerializer(many=True, read_only=True)
    imagens = ProgramaImagemSerializer(many=True, read_only=True)
    class Meta:
        model = Programa

class ProgramaProducaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProgramaProducao
 
class ProgramaSerieSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProgramaSerie
 
class PublicacaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Publicacao
 
class PublicacaoClasseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PublicacaoClasse
 
class PublicacaoComentarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PublicacaoComentario
 
class PublicacaoSubclasseSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PublicacaoSubclasse
 
class RegiaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Regiao
 
class RepresentanteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Representante
 
class SerieSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Serie
 
class SessaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Sessao
 
class SessaoComentarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SessaoComentario
 
class SessaoFilmeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SessaoFilme
 
class SessaoMidiaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SessaoMidia
 
class SessaoRelatorioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SessaoRelatorio
 
class SistemaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Sistema
 
class TarefaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tarefa
 
class TarefaPerguntaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TarefaPergunta
 
class TecnicaAnimacaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TecnicaAnimacao
 
class TempQuemAdquiriuSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TempQuemAdquiriu
 
class UsuarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Usuario
 
class UsuarioPermissaoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UsuarioPermissao
 
class ValorLoteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ValorLote
 

