from random import randint

"""list for history of player moves"""
history = []

"""generate array with 4 ships in random places"""


def generate_arr():
    arr = []
    for j in range(0, 5):
        arr.append([0 for i in range(0, 5)])

    for i in range(4):
        ri = randint(0, 4)
        ci = randint(0, 4)
        while arr[ri][ci] == 1:
            ri = randint(0, 4)
            ci = randint(0, 4)

        arr[ri][ci] = 1

    return arr


"""print the board on the screen function"""


def display_arr(arr, hide):
    for r in arr:
        rs = ""
        for el in r:
            if hide or el == 0:
                rs += ". "
            else:
                rs += "@ "
        print(rs)


"""hit opponents board function"""


def hit(arr, ri, ci):
    if arr[ri][ci] == 1:
        arr[ri][ci] = 0
        return 1
    else:
        return 0


"""check if board contains only zeros function"""


def empty(arr):
    return sum([sum(row) for row in arr]) == 0
    """check if coordinates are valid and they
are not in history already function"""


def check_coords(ri, ci):
    if ri < 0 or ri > 4 or ci < 0 or ci > 4:
        print("insert values in range from 0 to 4")
        return False

    if len(history) > 0 and (ri, ci) in history:
        print("this coordinates were already hit")
        return False

    return True


"""players points vars"""


player_points = 0
computer_points = 0

print("Please enter your name:")
name = input()

"""generate and display players board"""
player_arr = generate_arr()
print(name + "'s board:")
display_arr(player_arr, False)

"""generate and display computer board"""
computer_arr = generate_arr()
print("Computers board:")
display_arr(computer_arr, True)

"""variable determining the main loop of the game"""
game = True

"""if game is True repeat rounds"""
while game:
    ri = -1
    ci = -1

    """player inserting coordinates till they are valid"""
    while not check_coords(ri, ci):
        print("Guess a row:")
        ri = int(input())
        print("Guess a column:")
        ci = int(input())

    """players hit"""
    print("Player guessed:(", ri, ",", ci, ")")
    points = hit(computer_arr, ri, ci)
    """add coordinates to history"""
    history.append((ri, ci))

    """display result of hit"""
    if points == 1:
        print("Player hit the ship")
    else:
        print("Player missed")

    """add points"""
    player_points += points

    """random computers move"""
    ri = randint(0, 4)
    ci = randint(0, 4)
    print("Computer guessed:(", ri, ", ", ci, ")")

    """computers hit"""
    points = hit(player_arr, ri, ci)

    """display result of hit"""
    if points == 1:
        print("Computer hit the ship")
    else:
        print("Computer missed")

    """add points"""
    computer_points += points

    """display summary of the round"""
    print("---------------------------------")
    print("After this round, the scores are")
    print(name, ":", player_points, ". Computer", computer_points)
    """player decide to play or stop the game"""
    print("Press any key to continue or 'no' to quit")
    command = input()
    if command == "no":
        game = False
    print("---------------------------------")

    """check if someone won the game and end the game"""
    if empty(player_arr):
        print("Computer won the game!")
        game = False
    elif empty(computer_arr):
        print("Player won the game!")
        game = False
