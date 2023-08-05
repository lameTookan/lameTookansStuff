class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    reset = "\u001b[0m"

    def rgb(r, g, b):
        return f"\u001b[38;2;{r};{g};{b}m"


class bg:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"

    def rgb(r, g, b):
        return f"\u001b[48;2;{r};{g};{b}m"


colors_fg = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "rgb": lambda r, g, b: f"\u001b[38;2;{r};{g};{b}m",
}

colors_bg = {
    "black": "\u001b[40m",
    "red": "\u001b[41m",
    "green": "\u001b[42m",
    "yellow": "\u001b[43m",
    "blue": "\u001b[44m",
    "magenta": "\u001b[45m",
    "cyan": "\u001b[46m",
    "white": "\u001b[47m",
}


def yellow(text):
    return f"{fg.yellow}{text}{fg.reset}"


def red(text):
    return f"{fg.red}{text}{fg.reset}"


def green(text):
    return f"{fg.green}{text}{fg.reset}"


def blue(text):
    return f"{fg.blue}{text}{fg.reset}"


def magenta(text):
    return f"{fg.magenta}{text}{fg.reset}"


def cyan(text):
    return f"{fg.cyan}{text}{fg.reset}"


def white(text):
    return f"{fg.white}{text}{fg.reset}"


def underline(text):
    return f"\u001b[4m{text}{fg.reset}"


def bold(text):
    return f"\u001b[1m{text}{fg.reset}"


def italic(text):
    return f"\u001b[3m{text}{fg.reset}"


def print_colors(text):
    for color in colors_fg:
        print(f"{colors_fg[color]}{text}{fg.reset}")
        
RED = "\u001b[31m"
BLUE = "\u001b[34m"
CYAN = "\u001b[36m"
MAGENTA = "\u001b[35m"
YELLOW = "\u001b[33m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"
BOLD = "\u001b[1m"
UNDERLINE = "\u001b[4m"
ITALIC = "\u001b[3m"
GREEN = "\u001b[32m"

ON_WHITE = "\u001b[47m"
ON_BLACK = "\u001b[40m"
ON_BLUE = "\u001b[44m"
ON_YELLOW = "\u001b[43m"
ON_MAGENTA = "\u001b[45m"
ON_CYAN = "\u001b[46m"
ON_RED = "\u001b[41m"

class Colors:
    RED = "\u001b[31m"
    BLUE = "\u001b[34m"
    CYAN = "\u001b[36m"
    MAGENTA = "\u001b[35m"
    YELLOW = "\u001b[33m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"
    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"
    ITALIC = "\u001b[3m"
    GREEN = "\u001b[32m"

    ON_WHITE = "\u001b[47m"
    ON_BLACK = "\u001b[40m"
    ON_BLUE = "\u001b[44m"
    ON_YELLOW = "\u001b[43m"
    ON_MAGENTA = "\u001b[45m"
    ON_CYAN = "\u001b[46m"
    ON_RED = "\u001b[41m"
    def color_text(self, text, color):
        return f"{color}{text}{self.RESET}"
COLORS_BAG = Colors()

RED = "\u001b[31m"
GREEN = "\u001b[32m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
BLUE = "\u001b[34m"
YELLOW = "\u001b[33m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"
BOLD = "\u001b[1m"
ITALIC = "\u001b[3m"
UNDERLINE = "\u001b[4m"

ON_WHITE = "\u001b[47m"
ON_BLACK = "\u001b[40m"
ON_BLUE = "\u001b[44m"
ON_YELLOW = "\u001b[43m"
ON_MAGENTA = "\u001b[45m"
ON_CYAN = "\u001b[46m"
ON_RED = "\u001b[41m"