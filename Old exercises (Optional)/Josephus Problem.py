
def get_winning_seat(num_players):
    seats = [i for i in range(1,num_players)]
    while len(seats) > 1:
        seats = seats[1::2]
    return seats[0] + 1

num_players = int(input("Please enter the number of players: "))
winning_seat = get_winning_seat(num_players)
print(f"The winning seat is {winning_seat}")
