
print('Estou modificando a minha Branch conteudo')

class Conteudo:
    def comandoLista(self):

        lista = []
        for recebe in range(2):
            nome = input('Nome: ')
            idade = int(input('idade: '))
            profissao = input('prof: ')
            lista.append(nome)
            lista.append(idade)
            lista.append(profissao)
        print(lista)

