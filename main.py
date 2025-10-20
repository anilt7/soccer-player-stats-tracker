import matplotlib.pyplot as plt


def input_player_stats():
    players = []
    num_players = int(input("Enter number of players to track: "))

    for i in range(num_players):
        print(f"\nEnter details for Player {i + 1}:")
        name = input("Player Name: ")

        while True:
            try:
                goals = int(input("Goals Scored: "))
                assists = int(input("Assists: "))
                pass_accuracy = float(input("Pass Accuracy (%): "))
                minutes = int(input("Minutes Played: "))

                if goals < 0 or assists < 0 or not (0 <= pass_accuracy <= 100) or minutes <= 0:
                    print("❌ Invalid input. Please enter valid positive numbers.")
                    continue

                players.append({
                    "name": name,
                    "goals": goals,
                    "assists": assists,
                    "pass_accuracy": pass_accuracy,
                    "minutes": minutes
                })
                break

            except ValueError:
                print("⚠️ Please enter numeric values only.")

    return players



def check_performance(player):
    print(f"\n📊 Performance for {player['name']}:")

    if player["goals"] >= 2:
        print("✅ Great goal performance!")
    else:
        print("⚠️ Could improve goal-scoring.")

    if player["assists"] >= 1:
        print("✅ Good team support (assists).")
    else:
        print("⚠️ Needs more assists.")

    if player["pass_accuracy"] >= 80:
        print("✅ Excellent passing accuracy.")
    else:
        print("⚠️ Passing accuracy below standard.")

    if player["minutes"] >= 60:
        print("✅ Maintained strong playtime.")
    else:
        print("⚠️ Consider improving stamina.")
       
def visualize_stats(players):
    names = [p["name"] for p in players]
    goals = [p["goals"] for p in players]
    assists = [p["assists"] for p in players]
    accuracy = [p["pass_accuracy"] for p in players]

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1)
    plt.bar(names, goals)
    plt.title("Goals Scored")

    plt.subplot(1, 3, 2)
    plt.bar(names, assists)
    plt.title("Assists")

    plt.subplot(1, 3, 3)
    plt.bar(names, accuracy)
    plt.title("Pass Accuracy (%)")

    plt.tight_layout()
    plt.show()



def main():
    print("⚽ Welcome to Soccer Player Stats Tracker ⚽")
    players = input_player_stats()

    for p in players:
        check_performance(p)

    visualize_stats(players)
    print("\n✅ Analysis complete!")



if __name__ == "__main__":
    main()