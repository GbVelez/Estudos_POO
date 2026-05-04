#Classe Pai
class Servico():
    def __init__(self, descricao, valor_hora):
        #Encapsulamento para proteção de dados
        self._descricao = descricao
        self._valor_hora = valor_hora
#Metodo para calculo total de horas vezes o valor da hora
    def calcular_total(self, horas):
        return horas * self._valor_hora
#Classe Filha Manutenção Industrial que herda de serviço
class ManutencaoIndustrial(Servico):
    def __init__(self, descricao, valor_hora,horas):
        super().__init__(descricao, valor_hora)
        #Informando que o horas utilizado em calculo total precisa receber a informação horas para que possa ser informada as horas
        self.horas = horas
        #Informando a taxa fixa de deslocamento
        self._taxa_deslocamento = 150
#Metodo para calcular o valor total que seria o calculo total mais o 150 da taxa de serviço que é fixo
    def valor_total(self):
        total = self.calcular_total(self.horas)
        return total + self._taxa_deslocamento
#Polimorfismo utilizado para que cada recibo tenha sua identidade
    def gerar_recibo(self):
        print(f'RECIBO INDUSTRIAL')
        print(f'O Serviço Solicitado foi:{self._descricao}')
        print(f'O valor por hora é:{self._valor_hora}')
        print(f'A quantidade de horas é de {self.horas}')
        print(f'O valor total é de {self.valor_total()}')

class ManutencaoLeve(Servico):
    def __init__(self, descricao, valor_hora,horas):
        super().__init__(descricao, valor_hora)
        self.horas = horas

# Metodo para calcular o valor total que seria o calculo total menos cinco porcento caso o serviço tenha mais de 10 horas de duração
    def valor_total(self, horas):
        total = self.calcular_total(self.horas)
        if self.horas > 10:
            return self.calcular_total(self.horas) * 0.95
        else:
            return self.calcular_total(self.horas)
#Utilizando Novamente Polimorfismo
    def gerar_recibo(self):
        print(f'RECIBO LEVE')
        print(f'O Serviço Solicitado foi:{self._descricao}')
        print(f'O valor por hora é:{self._valor_hora}')
        print(f'A quantidade de horas é de {self.horas}')
        print(f'O valor total é de {self.valor_total(self.horas)}')

#Exibindo resultados
ind1 = ManutencaoIndustrial('Ponte Qubrada',1000,10)
ind1.gerar_recibo()
lev1 = ManutencaoLeve('Torno Qubrado',150,5)
lev1.gerar_recibo()



