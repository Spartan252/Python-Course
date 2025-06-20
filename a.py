data = [
  { 'name': 'Instagram', 'follower_count': 691, 'description': 'Social media platform', 'country': 'United States' },
  { 'name': 'Cristiano Ronaldo', 'follower_count': 658, 'description': 'Footballer', 'country': 'Portugal' },
  { 'name': 'Lionel Messi', 'follower_count': 505, 'description': 'Footballer', 'country': 'Argentina' },
  { 'name': 'Selena Gomez', 'follower_count': 419, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Kylie Jenner', 'follower_count': 393, 'description': 'Media personality', 'country': 'United States' },
  { 'name': 'Dwayne Johnson', 'follower_count': 393, 'description': 'Actor and wrestler', 'country': 'United States' },
  { 'name': 'Ariana Grande', 'follower_count': 375, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Kim Kardashian West', 'follower_count': 356, 'description': 'Media personality', 'country': 'United States' },
  { 'name': 'Beyoncé', 'follower_count': 311, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Khloé Kardashian', 'follower_count': 302, 'description': 'Media personality', 'country': 'United States' },
  { 'name': 'Justin Bieber', 'follower_count': 294, 'description': 'Musician', 'country': 'Canada' },
  { 'name': 'Kendall Jenner', 'follower_count': 287, 'description': 'Media personality', 'country': 'United States' },
  { 'name': 'Taylor Swift', 'follower_count': 281, 'description': 'Musician', 'country': 'United States' },
  { 'name': 'National Geographic', 'follower_count': 278, 'description': 'Magazine', 'country': 'United States' },
  { 'name': 'Virat Kohli', 'follower_count': 273, 'description': 'Cricketer', 'country': 'India' },
  { 'name': 'Jennifer Lopez', 'follower_count': 248, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Neymar', 'follower_count': 229, 'description': 'Footballer', 'country': 'Brazil' },
  { 'name': 'Nicki Minaj', 'follower_count': 225, 'description': 'Musician', 'country': 'Trinidad and Tobago' },
  { 'name': 'Kourtney Kardashian', 'follower_count': 218, 'description': 'Media personality', 'country': 'United States' },
  { 'name': 'Miley Cyrus', 'follower_count': 212, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Katy Perry', 'follower_count': 204, 'description': 'Musician', 'country': 'United States' },
  { 'name': 'Zendaya', 'follower_count': 178, 'description': 'Actress and singer', 'country': 'United States' },
  { 'name': 'Kevin Hart', 'follower_count': 177, 'description': 'Comedian and actor', 'country': 'United States' },
  { 'name': 'Real Madrid CF', 'follower_count': 176, 'description': 'Football club', 'country': 'Spain' },
  { 'name': 'Cardi B', 'follower_count': 163, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'LeBron James', 'follower_count': 159, 'description': 'Basketball player', 'country': 'United States' },
  { 'name': 'Demi Lovato', 'follower_count': 153, 'description': 'Musician and actress', 'country': 'United States' },
  { 'name': 'Rihanna', 'follower_count': 149, 'description': 'Musician', 'country': 'Barbados' },
  { 'name': 'Chris Brown', 'follower_count': 144, 'description': 'Musician', 'country': 'United States' },
  { 'name': 'Drake', 'follower_count': 142, 'description': 'Musician', 'country': 'Canada' },
  { 'name': 'FC Barcelona', 'follower_count': 141, 'description': 'Football club', 'country': 'Spain' },
  { 'name': 'Ellen DeGeneres', 'follower_count': 136, 'description': 'Comedian and television host', 'country': 'United States' },
  { 'name': 'Billie Eilish', 'follower_count': 124, 'description': 'Musician', 'country': 'United States' }
]






import  random

import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

  

def logo():
    print("""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      
        """)
    

def verify(person_a, person_b, choice, score):
    if choice == "a" and (person_a['follower_count'] > person_b['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
        data.remove(person_b)
        return person_a, score, False
    elif choice == "b" and (person_b['follower_count'] > person_a['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
        data.remove(person_a)
        return person_b, score, False
    else:
        lost(score)
        return person_a, score, True


def lost(score):
    clear_terminal()
    logo()
    print(f"Sorry, that's wrong. Final score: {score}")

    
def compare():
    score = 0
    person_a = random.choice(data)
    lost_flag = False

    while not lost_flag:
        person_b = random.choice(data)
        while person_b == person_a:
            person_b = random.choice(data)

        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print("""
        _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)    
        """)
        print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        person_a, score, lost_flag = verify(person_a, person_b, choice, score)
        clear_terminal()

    lost(score)


compare()   #Start