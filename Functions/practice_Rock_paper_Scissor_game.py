"""
Write a small function to depict rock_paper_scissors game
Your function should take two inputs and should give us the winner based on a certain condition
"""
print("What do u want to choose> rock, or paper or scissors?")
p1 = input()
print("What do u want to choose> rock, or paper or scissors?")
p2 = input()


def game(a, b):
    if a == b:
        return "Tie"
    elif a == "rock":
        if b == "scissor":
            return "rock beats scissor"
        else:
            return "paper beats rock"
    elif a == "scissor":
        if b == "paper":
            return "scissor beats scissor"
        else:
            return "rock beats rock"
    elif a == "paper":
        if b == "rock":
            return "paper beats scissor"
        else:
            return "scissor beats rock"
    else:
        return "Invalid input"


print(game(p1, p2))
