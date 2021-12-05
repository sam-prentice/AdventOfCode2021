file_in = open("input.txt", "r")
called_numbers = file_in.readline()
games = file_in.read().splitlines()
file_in.close()
games.pop(0)

def check_for_five(values):
    score_count = 0
    for value in values:
        if value == 'X':
            score_count += 1

    if score_count == 5:
        return True
    else: 
        return False

def check_for_winner(game_card):
    grid_size = 5
    for row in game_card:
        if check_for_five(row):
            return game_card

    for row in game_card:
        for column_index in range(grid_size):
            values = []
            for row_index in range(grid_size):
                values.append(game_card[row_index][column_index])
            if check_for_five(values):
                return game_card
    return False

def calculate_score(winning_board, winning_number):
    sum = 0
    for row in winning_board:
        for column in row:
            if column != 'X':
                sum += int(column)  
    return sum * int(winning_number)


games_by_rows_and_columns = []
game_cards = []
game_card = []
winning_boards = []

for row in games:
    row_by_colums = row.split()
    games_by_rows_and_columns.append(row_by_colums)


for row in games_by_rows_and_columns:
    if len(row) == 0:
        game_cards.append(game_card)
        game_card = []
    else:
        game_card.append(row)


for called_number in called_numbers.split(','):
    for game_index, game_card in enumerate(game_cards):
        for row_index, row in enumerate(game_card):
            for column_index, column in enumerate(row):
                if column == called_number:
                    game_card[row_index][column_index] = 'X'
        if check_for_winner(game_card):
            print("Score: " + str(calculate_score(check_for_winner(game_card), called_number)))
            winning_boards.append(game_card)
            game_cards.pop(game_index)
