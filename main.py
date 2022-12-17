import game_data
import random



def higher_lower():
    data=game_data.data

    score=0
    lose=0
    while lose==0:
        choice1 = random.choice(data)
        choice2 = random.choice(data)
        print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
        print(f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
        guess=input("Who has more followers?")
        if guess=="A" and choice1['follower_count']>choice2['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}")
        elif guess=="B" and choice2['follower_count']>choice1['follower_count']:
            score+=1
            print(f"You're right! Current score: {score}")
        else:
            lose+=1
            print(f"You're wrong! Final score:{score}")


higher_lower()

