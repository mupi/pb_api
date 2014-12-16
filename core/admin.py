from django.contrib import admin

from core.models import Associado, AssociadoCircuito, AssociadoHistorico, AssociadoPonto, Atendimento, Circuito, CircuitoAcesso, CircuitoGrupo, CircuitoSerie, Contrato, ContratoAssinatura, ContratoDeposito, Convenio, Cupom, Curador, CuradorFilme, Diretor, Estado, Evento, FaixaEtaria, Filme, FilmeComentario, FilmeDiretor, FilmeImagem, FilmeInscritoPb, FilmeLegenda, FilmeMaterialSobreFilme, FilmeSerie, FilmeSuporteDisponivel, FilmeTecnicaAnimacao, Formato, Genero, GeneroSub, Helpdesk, Idioma, LogSistema, MaterialSobreFilme, Modulo, Municipio, Newsletter, Pedido, PedidoHistorico, PedidoPrograma, PedidoStatus, Produtor, Programa, ProgramaComentario, ProgramaFilme, ProgramaImagem, ProgramaProducao, ProgramaSerie, Publicacao, PublicacaoClasse, PublicacaoComentario, PublicacaoSubclasse, Regiao, Representante, Serie, Sessao, SessaoComentario, SessaoFilme, SessaoMidia, SessaoRelatorio, Sistema, Tarefa, TarefaPergunta, TecnicaAnimacao, TempQuemAdquiriu, Usuario, UsuarioPermissao, ValorLote

models = [Associado, AssociadoCircuito, AssociadoHistorico, AssociadoPonto, Atendimento, Circuito, 
		  CircuitoAcesso, CircuitoGrupo, CircuitoSerie, Contrato, ContratoAssinatura, ContratoDeposito, 
   		  Convenio, Cupom, Curador, CuradorFilme, Diretor, Estado, Evento, FaixaEtaria, Filme, FilmeComentario, 
   		  FilmeDiretor, FilmeImagem, FilmeInscritoPb, FilmeLegenda, FilmeMaterialSobreFilme, FilmeSerie, 
 		  FilmeSuporteDisponivel, FilmeTecnicaAnimacao, Formato, Genero, GeneroSub, Helpdesk, Idioma, 
 		  LogSistema, MaterialSobreFilme, Modulo, Municipio, Newsletter, Pedido, PedidoHistorico, PedidoPrograma, 
 		  PedidoStatus, Produtor, Programa, ProgramaComentario, ProgramaFilme, ProgramaImagem, ProgramaProducao, 
 		  ProgramaSerie, Publicacao, PublicacaoClasse, PublicacaoComentario, PublicacaoSubclasse, Regiao, Representante, 
 		  Serie, Sessao, SessaoComentario, SessaoFilme, SessaoMidia, SessaoRelatorio, Sistema, Tarefa, TarefaPergunta, 
 		  TecnicaAnimacao, TempQuemAdquiriu, Usuario, UsuarioPermissao, ValorLote]

admin.site.register(models)
