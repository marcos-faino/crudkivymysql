import kivy
from kivy.app import App
from view.gerencTelas import GerenciaTelas
from view.telaTurma import ViewTurma

kivy.require('2.1.0')

__version__ = '0.1'


class exemploCrud(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root


if __name__ == '__main__':
    exemploCrud().run()