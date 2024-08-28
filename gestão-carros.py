from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class GestaoVeiculosApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista = []  # Lista para armazenar os carros

    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')

        # Layout para os campos de entrada e labels
        grid = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        
        # Labels e TextInputs para as propriedades do veículo
        grid.add_widget(Label(text='Marca:', size_hint_x=0.3))
        self.marca = TextInput(multiline=False)
        grid.add_widget(self.marca)

        grid.add_widget(Label(text='Modelo:', size_hint_x=0.3))
        self.modelo = TextInput(multiline=False)
        grid.add_widget(self.modelo)

        grid.add_widget(Label(text='Ano:', size_hint_x=0.3))
        self.ano = TextInput(multiline=False)
        grid.add_widget(self.ano)

        grid.add_widget(Label(text='Placa:', size_hint_x=0.3))
        self.placa = TextInput(multiline=False)
        grid.add_widget(self.placa)

        # Adiciona o grid ao layout principal
        layout.add_widget(grid)

        # Layout para os botões
        botoes = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)

        # Botão Gravar
        btn_gravar = Button(text='Gravar')
        btn_gravar.bind(on_release=self.gravar_veiculo)
        botoes.add_widget(btn_gravar)

        # Botão Pesquisar
        btn_pesquisar = Button(text='Pesquisar')
        btn_pesquisar.bind(on_release=self.pesquisar_veiculo)
        botoes.add_widget(btn_pesquisar)

        # Adiciona os botões ao layout principal
        layout.add_widget(botoes)

        return layout

    def gravar_veiculo(self, instance):
        # Cria um dicionário com os dados do veículo
        veiculo = {
            'placa': self.placa.text,
            'modelo': self.modelo.text,
            'marca': self.marca.text,
            'ano': self.ano.text
        }
        # Adiciona o dicionário à lista
        self.lista.append(veiculo)
        # Limpa os TextInputs
        self.placa.text = ''
        self.modelo.text = ''
        self.marca.text = ''
        self.ano.text = ''
        print(f"Veículo gravado: {veiculo}")

    def pesquisar_veiculo(self, instance):
        # Procura o veículo pela placa
        placa_pesquisada = self.placa.text
        for veiculo in self.lista:
            if veiculo['placa'] == placa_pesquisada:
                # Se encontrar, preenche os TextInputs
                self.modelo.text = veiculo['modelo']
                self.marca.text = veiculo['marca']
                self.ano.text = veiculo['ano']
                print(f"Veículo encontrado: {veiculo}")
                return
        print("Veículo não encontrado.")

if __name__ == '__main__':
    GestaoVeiculosApp().run()
