import random
from collections import deque

def hot_potato_game(players, max_passes):
    queue = deque(players)  # Representing the circle of players
    
    while len(queue) > 1:  # Continue until only one player remains
        passes = random.randint(1, max_passes)  # Random number of passes
        # Simulate the passing
        queue.rotate(-passes)  # Move players around the queue
        # Remove the player holding the hot potato
        queue.popleft()  # The player is eliminated
    
    return queue[0]  # Return the winner

# Example usage
players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
max_passes = 4
winner = hot_potato_game(players, max_passes)
winner
import random
from collections import deque

def hot_potato_game(players, max_passes):
    queue = deque(players)  # Representing the circle of players
    print(f"Jugadores iniciales: {list(queue)}")
    
    round_number = 1
    while len(queue) > 1:  # Continue until only one player remains
        passes = random.randint(1, max_passes)  # Random number of passes
        print(f"\nRonda {round_number}: La papa se pasa {passes} veces")
        
        # Simulate the passing
        queue.rotate(-passes)  # Move players around the queue
        
        # Remove the player holding the hot potato
        eliminated = queue.popleft()  # The player is eliminated
        print(f"¡{eliminated} ha sido eliminado!")
        print(f"Jugadores restantes: {list(queue)}")
        
        round_number += 1
    
    return queue[0]  # Return the winner

# Example usage
players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
max_passes = 4

print("Iniciando el juego de la Papa Caliente...\n")
winner = hot_potato_game(players, max_passes)
print(f"\n¡{winner} es el ganador del juego de la Papa Caliente!")