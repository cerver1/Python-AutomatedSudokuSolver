from time import sleep


def request_difficulty_level():
    difficulty_scale = '\n1 = Easy\n2 = Medium\n3 = Hard\n4 = Evil\n\n'
    difficulty = input("{}Please enter a number that corresponds to a difficulty level: ".format(difficulty_scale))

    if int(difficulty) not in range(1, 5):
        request_difficulty_level()
    else:
        return continue_prompt(int(difficulty))


def when_statement(level):
    when = {
        1: 'easy',
        2: 'medium',
        3: 'hard',
        4: 'evil'
    }
    return when.get(level, "something went wrong")


def continue_prompt(difficulty):
    confirm = str(input("\nYou selected: {}, do you want to continue? (Y/N): ".format(when_statement(difficulty))))
    if confirm.upper() == "Y":
        return when_statement(difficulty)
    elif confirm.upper() == "N":
        request_difficulty_level()
    else:
        continue_prompt(difficulty)


def selected_url():
    url = "https://www.livesudoku.com/en/sudoku/{}/".format(request_difficulty_level())
    sleep(1.5)
    return url
