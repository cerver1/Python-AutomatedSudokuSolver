def request_difficulty_level():
    difficulty_scale = '\n1 = Easy\n2 = Medium\n3 = Hard\n4 = Evil\n\n'
    difficulty = input("{}Please enter a number that corresponds to a difficulty level: ".format(difficulty_scale))

    if int(difficulty) not in range(1, 5):
        request_difficulty_level()
    else:
        return continue_prompt(difficulty)


def continue_prompt(difficulty):
    when = {
        1: 'easy',
        2: 'medium',
        3: 'hard',
        4: 'evil'
    }

    confirm = str(raw_input("\nYou selected: {}, do you want to continue? (Y\N): ".format(when.get(difficulty))))
    if confirm.upper() == "Y":
        return when.get(difficulty)
    elif confirm.upper() == "N":
        request_difficulty_level()
    else:
        continue_prompt(difficulty)


def selected_url():
    url = "https://www.livesudoku.com/en/sudoku/{}/".format(request_difficulty_level())
    return url
