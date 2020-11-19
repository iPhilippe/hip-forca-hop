# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.guessed_letters = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word  not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word not in self.wrong_letters:
            self.wrong_letters.append(letter)
            
    # Método para não mostrar a letra no board
    def hide_word(self):
        showWord = ''
        for character in self.word:
            if character not in self.guessed_letters:
                showWord += '_'
            else:
                showWord += character
        return showWord


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        tentatives = len(self.wrong_letters)
        print(board[tentatives])
        print(self.hide_word())
        print('Letras descartadas: %s' %list(self.wrong_letters))


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.wrong_letters) == 6 or self.hide_word().strip() == self.word.strip():
            return True
        else:
            return False


    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.hide_word() == self.word:
            return True
        else:
            return False

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("cantores.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        game.guess(input("Digite uma letra para adivinhar o cantor: "))


    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
