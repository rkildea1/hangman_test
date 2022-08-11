
import random

class Hangman:

   
    def __init__(self, word_list, num_lives=5):
                            
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) #pick a word from the list
        self.num_letters = int()
        self.list_letters = []
        self.word_guessed = ['_'] * len(self.word)

        print(f"The mystery word has {len(self.word)} characters") #print how long the word is
        print(f'{self.word_guessed}') #print the word in underscores eg, ['_ _ _ _']
        pass


    def check_letter(self, letter):

        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        alphabetList = []
        for x,y in enumerate(self.word): # x = the index of the string, y = the corresponding letter of the hangmanword
            if letter == y: #if the guess is equal to a letter in the hangmanword
                for a,b in enumerate(self.word_guessed):# a = the index of the list, b = the corresponding underscore of the blankword [_ _ _ _]
                    if a == x: # where the index of the underscore list is equal to the index of the letter in the hangman word..
                        self.word_guessed[x] = (letter) #replace the underscore of the 
        print(self.word_guessed)
        
             

    def ask_letter(self):

        while self.num_lives>0:
            letter = input('Please enter a letter: ')
            letter = letter.lower()
            if len(letter) !=1:
                    self.num_lives -= 1
                    print("Please, enter just one character")
            else:    
                if letter in self.list_letters:
                    print(f'"{letter} was already tried"')
                else: 
                    if letter in self.word:
                        self.list_letters.append(letter)
                        print(f'Great job, you guessed the letter {letter} which is a correct guess.') 
                        print(f'So far you have guessed the following letters: {self.list_letters}') 
                        self.check_letter(letter) 
                    else:
                        self.num_lives -= 1
                        self.list_letters.append(letter)
                        print(f'Hard luck! You guessed {letter} which is not a correct letter.') 
                        print(f'So far you have guessed the following letters: {self.list_letters}') 
                        print(f'you have {self.num_lives} lives left')
                        print(self.word_guessed)
        else:
            print(f'You ran out of lives. The word was {self.word}')
        pass
        


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%

# %%

