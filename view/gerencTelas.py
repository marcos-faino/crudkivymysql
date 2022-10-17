from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

# from view.telaAluno import ViewAluno
from view.telaTurma import ViewTurma


class TelaInicial(Screen):
    pass


class CadastroTurma(Screen):
    pass


class ListarTurmas(Screen):
    inputid = ObjectProperty(None)
    colid = ObjectProperty(None)
    colnome = ObjectProperty(None)
    colturno = ObjectProperty(None)
    colatual = ObjectProperty(None)
    colexcluir = ObjectProperty(None)
    gridlistar = ObjectProperty(None)


class CadastroAluno(Screen):
    pass


class ListarAlunos(Screen):
    pass


class GerenciaTelas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._telaTurma = ViewTurma(self)
        # self._telaAluno = ViewAluno(self)

    def telaInicial(self):
        self.current = "TelaInicial"

    def telaCadastroTurma(self):
        self.current = 'CadastroTurma'

    def telaListarTurmas(self):
        self.current = "ListarTurmas"
    """
    def telaCadastroAluno(self):
        self.current = "CadastroAluno"

    def telaListarAlunos(self):
        self._telaAluno.alternarPesq("id")
        self.current = "ListarAlunos"
    """
    def cadastrarAtualizar(self):
        self._telaTurma.cadAtualTurma()
    """
    def cadastrarAtualizarAluno(self):
        self._telaAluno.cadAtualAluno()
    """
    def buscarTurmas(self):
        self._telaTurma.buscaTurmas()
    """
    def buscarAlunos(self):
        self._telaAluno.buscaAlunos()

    def buscarAlunosNome(self, nome):
        self._telaAluno.buscaAlunos(nome)
    """