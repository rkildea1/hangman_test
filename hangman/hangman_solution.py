
from os import lseek
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



    def check_letter(self, letter):
        for x,y in enumerate(self.word): # x = the index of the string, y = the corresponding letter of the hangmanword
            if letter == y: #if the guess is equal to a letter in the hangmanword
                for a,b in enumerate(self.word_guessed):# a = the index of the list, b = the corresponding underscore of the blankword [_ _ _ _]
                    if a == x: # where the index of the underscore list is equal to the index of the letter in the hangman word..
                        self.word_guessed[x] = (letter) #replace the underscore of the 
        print(self.word_guessed)

        

             

    def ask_letter(self):
            # TODO This condition should be inside the "play_game" function.
            # TODO That way, this method only asks once for an input, which is what the name of the method suggests
            while self.num_lives>0 and '_' in self.word_guessed:
                print(f'you have {self.num_lives} lives left')
                letter = input('Please enter a letter: ')
                letter = letter.lower()
                if len(letter) !=1:
                        # TODO If the letter is not valid, you don't need to decrease the n_lives
                        # TODO (You can if you want to make the game harder)
                        self.num_lives -= 1
                        print("Please, enter just one character")
                else:    
                    if letter in self.list_letters:
                        print(f'"{letter} was already tried"')
                    else: 
                        if letter in self.word:
                            self.list_letters.append(letter)
                            print(f'So far you have guessed the following letters: {self.list_letters}') 
                            self.check_letter(letter) 
                        else:
                            self.num_lives -= 1
                            self.list_letters.append(letter)
                            print(f'Hard luck! You guessed {letter} which is not a correct letter.') 
                            print(self.word_guessed)


            else:
                if self.num_lives<1:
                    print(f'You ran out of lives. The word was {self.word}')
                else:
                    print('Congratulations, you won!')

        
        


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    # TODO As mentioned in line 40, the while loop should be here
    # TODO Something like: 
    # TODO while game.num_lives > 0 and '_' in game.word_guessed:
    # TODO      game.ask_letter()
    game.ask_letter()
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

