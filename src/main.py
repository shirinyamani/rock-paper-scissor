import random


class Game:
    def __init__(self):
        self.choices = ['r', 'p', 's']

    def get_user_choice(self):
        user_input = input(f'Please your choice from:{self.choices}.')
        if user_input.lower() in self.choices:
            return user_input.lower()
        print(f"Invalid input, choose from: {self.choices}:")
        return self.get_user_choice()


    def get_computer_choice(self):
         return random.choice(self.choices)
         

    def winner(self, com_choice, user_input):
        if com_choice == user_input:
            return "It's a Tie!"
        win_combo = [('r','s'), ('s', 'p'), ('p', 'r')]
        for combo in win_combo:
            if (com_choice == combo[0]) & (user_input == combo[1]):
                return 'COmputer won!'
        return "Congrats! Yoy won!"
        
    
    def play(self):
        user_input = self.get_user_choice()
        com_choice = self.get_computer_choice()
        print(self.winner(com_choice, user_input))


if __name__ == "__main__":
    game = Game()

    while True:
        game.play()

        continue_game = input("You wanna play more? q/yes")
        if continue_game.lower() == "q":
            break
