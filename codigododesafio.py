import csv

with open('listadeplayers.csv', newline='') as arquivo:
    dados = csv.reader(arquivo)
    primeira_tabela = [linha for linha in dados]

sugestoes_por_estilo = {
    'fps': 'sugerir jogos como CS GO e Call of Duty',
    'corrida': 'sugerir jogos como Trackmania e Need for Speed',
    'rpg': 'sugerir jogos como Orna e Dungeons & Dragons',
}

tabela_transformada = []
for dado in primeira_tabela:
    estilo = dado[3]
    sugestao = sugestoes_por_estilo.get(estilo, 'sugerir')
    dado.append(sugestao)
    tabela_transformada.append(dado)

with open('sugerirjogo.csv', 'w', newline='') as novo_arquivo:
    sugerirjogo = csv.writer(novo_arquivo, delimiter=',')
    sugerirjogo.writerows(tabela_transformada)

print("Tabela transformada gerada com sucesso!")

def gerar_segunda_tabela(primeira_tabela, sugestoes):
    segunda_tabela = []
    for jogador in primeira_tabela:
        jogador_id, jogador_nome, jogador_idade, jogador_estilo = jogador
        sugestao = sugestoes.get(jogador_estilo, 'sugerir')
        segunda_tabela.append([jogador_id, jogador_nome, jogador_idade, jogador_estilo, sugestao])
    return segunda_tabela

segunda_tabela = gerar_segunda_tabela(primeira_tabela, sugestoes_por_estilo)

with open('segundatabela.csv', 'w', newline='') as segundo_arquivo:
    segunda_jogo = csv.writer(segundo_arquivo, delimiter=',')
    segunda_jogo.writerows(segunda_tabela)

print("Segunda tabela gerada com base nas sugestões.")
