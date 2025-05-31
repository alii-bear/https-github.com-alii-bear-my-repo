def play_rps():
    choices = ["rock", "paper", "scissors"]

    rounds = input("How many rounds? (odd number): ")
    while not rounds.isdigit() or int(rounds) % 2 == 0:
        rounds = input("Please enter an odd number: ")
    rounds = int(rounds)

    p1_score = 0
    p2_score = 0

    def beats(p1, p2):
        return (p1 == "rock" and p2 == "scissors") or \
               (p1 == "scissors" and p2 == "paper") or \
               (p1 == "paper" and p2 == "rock")

    for r in range(1, rounds + 1):
        print(f"\nRound {r}")
        p1 = input("P1, choose (rock, paper, scissors): ").lower().strip()
        while p1 not in choices:
            p1 = input("Invalid. P1, try again: ").lower().strip()

        p2 = input("P2, choose (rock, paper, scissors): ").lower().strip()
        while p2 not in choices:
            p2 = input("Invalid. P2, try again: ").lower().strip()

        print(f"P1 chose: {p1}")
        print(f"P2 chose: {p2}")

        if p1 == p2:
            print("It's a tie!")
        elif beats(p1, p2):
            print("P1 wins!")
            p1_score += 1
        else:
            print("P2 wins!")
            p2_score += 1

    print("\nGame Over!")
    if p1_score > p2_score:
        print("Congrats P1, you won!")
    elif p2_score > p1_score:
        print("Congrats P2, you won!")
    else:
        print("It's a tie!")

play_rps()