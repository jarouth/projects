import random

USER_FAILURE = print("please enter a number") #used to check users numbers

MAX_LINE = 3 #Max lines to bet on

MAX_BET = 1000 #Max Bet

MIN_BET = 1 #Min Bet

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else: 
                winnings += values[symbol] * bet

    return winnings

def check_winning_lines(columns, lines):
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else: 
                winning_lines.append(lines + 1)

    return winning_lines


def get_slot_machine_spin(rows, cols, symbol): 
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) -1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount =  input("Please input the amount that you would like to deposit today! $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount enterted must be greater than 0")
        else: 
            print(USER_FAILURE)

    return amount 

def get_lines():
    while True:
        lines = input("Enter the number of lines that you would like to bet on (1-" + str(MAX_LINE) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE: 
                break
            else: 
                print("Enter A valid number between (1-" + str(MAX_LINE) + ")?")
        else: print(USER_FAILURE)

    return lines

def get_bet():
    while True:
        bet= input("Enter the amount that you would like to bet on each line (1-" + str(MAX_BET) + ")?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <=bet <= MAX_BET: 
                break
            else: 
                print(f"Enter A valid number between ${MIN_BET} - ${MAX_BET}.")
        else: print(USER_FAILURE)

    return bet 


def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        
        if total_bet > balance:
            print(f"You have exceeded your current balance, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    winning_lines = check_winning_lines(slots, lines )
    print(f"You won ${winnings}")
    print(f"you won on lines:", *winning_lines)
main()
