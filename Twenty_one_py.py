import random

class TwentyOneGame:
    """
    The main class for the card game Tjugoett (Twenty-One) for Edvin against a dealer.

    """

    def __init__(self):
        """
        Initialize the TwentyOneGame class with a deck of cards and both the player/dealer hands.

        I am using a tuple for cards as they shoudn't be changed, EVER

        Deck is a list of tuples.
        """
    
        self.deck: list[tuple[str, int]] = [
            (suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            for value in range(2, 15)  # Assigning the different card values. 
        ]

        
        random.shuffle(self.deck)
        
        self.player_hand: list[tuple[str, int]] = []
        self.dealer_hand: list[tuple[str, int]] = []    

    def deal_card(self) -> tuple[str, int]:
        """ This method deals a card from the deck, but if the deck is empty it reshuffles card

        returns: 
        tuple[int, str] The dealt card from the deck 
        """
        if len(self.deck) > 0:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card
        else:
            print("God Edvin you have been playing for a while :o...")
            print("the deck is empty... ")
            print("reshuffling the deck...")
            self.deck = self.player_hand + self.dealer_hand
            self.player_hand.clear()
            self.dealer_hand.clear()
            random.shuffle(self.deck)

        return self.deck.pop()  # This removes and returns last card to deck 
            

    def display_hand(self, hands:  list[tuple[str, int]]) -> str: 
        """
        Creating a simple method to handle cards are displayed, and creates a dict

        Return: (str) Returns how cards are displayed as a str
        """
        card_names: dict [int, str] = {
        11: "Jack", 
        12: "Queen", 
        13: "King", 
        14: "Ace"
        }

        return ', '.join([f"{card_names.get(card[1], card[1])} of {card[0]}" for card in hands])


    def score_calculation(self, hand: list[tuple[str, int]]) -> int:
        """
        Calculates the score of both hands, handling Aces as both 14 and or 1. 
        The program chooses Ace value in the favor of the User.

        Returns:
            int: The score calculation. 

        Thought Note:
            Thought about letting the player choose Ace value themselves, decided against it 
        """
        score: int = 0
        ace_count: int = 0
    
        for card in hand:
            if card[1] == 14:  
                ace_count += 1
            else:
                score += (card[1])
        # Handling both Aces values
        for _ in range(ace_count):
            if score + 14 <= 21:
                score += 14
            else:
                score += 1
          
        return score

    def player_turn(self) -> bool:
        """
        Handles the player's turn, here they can decide "to hit or not to hit" 
       
         Returns:
            boolean: Only returns true if player did'nt lose during their turn, 
            otherwise it returns false and ends game.
        """
        while True:
            print(f"\nYour hand: {self.display_hand(self.player_hand)}")
            print(f"Your current score: {self.score_calculation(self.player_hand)}")

            choice: str = input("Does Edvin want to hit or stand? (h/s): ").lower()

            if choice == "h":
                new_card: tuple[str, int] = self.deal_card()
                self.player_hand.append(new_card)
                print(f"Edvin drew: {new_card}!")
                
                # Checking for bust after each card
                if self.score_calculation(self.player_hand) > 21:
                    print("Oh Edvin just busted :( Better luck next time.")
                    return False
            elif choice == "s":
                return True
            else:
                print("Invalid input. Please enter 'h' for hit or 's' for stand.")

    def dealer_turn(self) -> None:
        """
        Handles the dealer's turn,makes sure that dealer hit until dealer has 17 .

        Returns:
        None
        """
        print("\nDealer's turn:")
        
        while self.score_calculation(self.dealer_hand) < 17:
            new_card: tuple[str, int] = self.deal_card()
            self.dealer_hand.append(new_card)
            # Had to convert new card to a list containing a singe value
            print(f"Dealer drew: {self.display_hand([new_card])}")


    def play_game(self) -> None:
        """
        This method manages the main game loop, and handles both player and dealer turns.

        My method also checks for ties and calculates the winner
        based on the rules of the game 
        """
      
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card()]
        
        if self.score_calculation(self.player_hand) > 21:
            print(f"Edvin's hand: {self.display_hand(self.player_hand)}")
            print(f"Edvin's score: {self.score_calculation(self.player_hand)}") 
            print("Oh Bust! You went over 21 with your initial hand Edvin, that's very unlucky...")
            print("Edvin sadly, you lost this one!")
            return
        # Checking if you lost 
        if not self.player_turn():
            print("You lost this one Edvin :( I wish you better luck next time! )")
            return

        self.dealer_turn()

        player_score: int = self.score_calculation(self.player_hand)
        dealer_score: int = self.score_calculation(self.dealer_hand)
        
        print(f"\nYour final hand: {self.display_hand(self.player_hand)}")
        print(f"Your final score: {player_score}")
        print(f"Dealer's final hand: {self.display_hand(self.dealer_hand)}")
        print(f"Dealer's final score: {dealer_score}")

        # Note: Dealer wins all ties
        if dealer_score > 21:
            print("Dealer busts! Edvin won this one!:D ")
        elif dealer_score >= player_score:
            print("Sorry, dealer wins this one Edvin! :( ")
        else:
            print("Edvin won this one! :)")

def main() -> None:
    """
    Main function to start the game.
    """
    game: TwentyOneGame = TwentyOneGame()
    game.play_game()

    while True:
        try:
            play_again: str = input("Does Edvin want to play again?  (y/n): ").lower()
            if play_again == "y":
                game = TwentyOneGame()
                game.play_game()
            elif play_again == "n":
                print("Thanks for playing Edvin! I hope you had fun :)")
                break
            else:
                raise ValueError("Invalid input Edvin... Please enter 'y' for yes or 'n' for no.")
        except ValueError as ve:
            print(f"An error in the form of: {ve}")
        except TypeError as te:
            print(f"An error in the form of: {te}")
        except Exception as e: 
            print(f"An error in the form of: {e} ")

if __name__ == "__main__":
    main()

"""
Tried making the game a bit more personalized for you, I realised the value of a more informal experience 
after Alexeis presentation. I sincerly hope you enjoyed it :-). I have a more formal one without your name
everywhere, please do tell if you're interested in that one aswell. 
"""
