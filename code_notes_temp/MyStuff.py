	

import os 
import shutil
from enum import Enum
from collections import namedtuple
terminal_size = os.get_terminal_size()
terminal_cols = terminal_size.columns
#===============================================================================

#..............................(COLORS).............................

#===============================================================================

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

#===============================================================================


#..............................(DIVIDERS)..............................


#===============================================================================
dividers_basic = {
    "dash": "-" * 50,
    "dot": "." * 50,
    "tilda": "~" * 50,
    "underscore": "_" * 50,
    "*": "*" * 50,
    "equal": "=" * 50,
    "hash": "#" * 50,
    "pipe": "|" * 50,
    "plus": "+" * 50,
    "minus": "-" * 50,
}
dividers_neat = {
    "night": "•☽───────────────────✧˖°˖☆˖°˖✧───────────────────☾•",
    "star": "──────────────────────── ⋆⋅☆⋅⋆ ────────────────────────",
    "cat": "=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=",
    "geo": "nunununununununununununununununununununununununununununununun",
    "oOo": ".oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.",
    "basic": "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+",
    "smiley": "☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻",
    "line": "──────────────────────────────────────────────────────────────────",
    "twinkle": "✦•〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰•★•〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰•✦",
    "diamond": "--:::------::------------------->◇<--------------------::------:::---",
    "temple": "╬╬════════════════════════════════════════════════════════════════╬╬",
    "wave": "▂ ▃ ▄ ▅ ▆ ▇ █ █ ▇ ▆ ▅ ▄ ▃ ▂",
    "big_wave": "▂▂ ▃▃ ▄▄ ▅▅ ▆▆ ▇▇ ██ ██ ▇▇ ▆▆ ▅▅ ▄▄ ▃▃ ▂▂",
    "skull": "☠◉☠◉☠◉☠◉☠☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻◉☠☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻☹☻",
    "fancy": "▅▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▅",
    "double": "════════════════════════════════════════════════════════════════════",
    "chain": "⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘",
    "tilda_line": "≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃≃",
    
}
dividers = {}
dividers.update(dividers_basic)
dividers.update(dividers_neat)


def print_all_dividers():
    for divider in dividers:
        print(dividers[divider])


def print_divider(divider_name="basic"):
    text: str  = dividers.get(divider_name, dividers["basic"])
    print(text.center(terminal_cols))


def get_divider(divider_name="basic"):
    text: str  = dividers.get(divider_name, dividers["basic"])
    return text.center(terminal_cols)

DividerChar = namedtuple("DividerChar", ["name", "char"])
class Divider_Chars(Enum):
    LINE = DividerChar("line", "─")
    DASH = DividerChar("dash", "-")
    DOT = DividerChar("dot", ".")
    DOUBLE = DividerChar("double", "═")
    BOTTOM = DividerChar("bottom", "▁")
    CHAIN = DividerChar("chain", "⫘")
    SQUIGGLE = DividerChar("squiggle", "〰")
    TRIPLE = DividerChar("triple", "☰")
    ABOUT_EQUAL = DividerChar("about-equal", "≈")
    TILDA_LINE = DividerChar("tilda-line", "≃")
    STABLE = DividerChar("stable", "⎍")
    POINT_DOWN = DividerChar("point-down", "☟")
    ARROW_DOWN = DividerChar("arrow-down", "↓")
    NEG_INF = DividerChar("neg-inf", "⧞")
    SCRIBBLE = DividerChar("scrible", "෴")
    TRI_DIAMOND =  DividerChar("tri-diamond", "ᚒ")
    OR = DividerChar("or", "ᚖ")
    MOUNTAIN = DividerChar("mountain", "ᨏ")
    
class MakeDivider:
    def __init__(self):
        self.divider_chars = Divider_Chars
        self.all_dividers = {e.name: e.value.char for e in self.divider_chars}
    def find_divider(self, name: str) -> DividerChar:
        name = name.upper()
        if name not in self.all_dividers:
            return self.divider_chars.LINE.value
        else:
            return self.divider_chars[name.upper()].value
    def make_divider(self, name: str = "line", length: int = terminal_cols):
        divider = self.find_divider(name)
        return divider.char * length
    
def test_make_divider():
    make_divider = MakeDivider()
    print(make_divider.make_divider("line"))
    print(make_divider.make_divider("dash"))
    print(make_divider.all_dividers)
    
divider_maker = MakeDivider()
class DividerCharNames:
    LINE = "line"
    DASH = "dash"
    DOT = "dot"
    DOUBLE = "double"
    CHAIN = "chain"
    BOTTOM = "bottom"
    SQUIGGLE = "squiggle"
    TRIPLE = "triple"
    "☰"
    
DIVIDER_CHARS = DividerCharNames()
def make_full_divider_special(name: str = "line" ) -> str:
    chars = {
        DIVIDER_CHARS.LINE: "─",
        DIVIDER_CHARS.DASH: "-",
        DIVIDER_CHARS.DOT: ".",
        DIVIDER_CHARS.DOUBLE: "═",
        DIVIDER_CHARS.BOTTOM: "▁",
        DIVIDER_CHARS.CHAIN: "⫘",
        DIVIDER_CHARS.SQUIGGLE: "〰",
        DIVIDER_CHARS.TRIPLE: "☰",

        
    }
    if name not in chars:
        c = chars["line"]
    else:
        c = chars[name]
    return c * terminal_cols
auto_double_cyan = cyan("══"*int(terminal_cols//2))
auto_center_stars = get_divider("star").center(terminal_cols, " ")

#===============================================================================

#..............................(NOTES).............................

#===============================================================================

def print_intro(*args,):
	for arg in args:
		print(yellow(arg), "\n")
def print_section(section: int,*args ,  divider = True):
	print("\n\n")
	if divider:
		print(magenta(dividers["basic"] ))
	print()
	print (magenta(f"===== ({str(section)}) ===== \n"))
	
	for arg in args:
			print(blue(arg))
			print()
		

def print_sub(section: str, *args):
	template = magenta("\n> {} <").format(section)
	print(template)
	if args:
		for arg in args:
			print(cyan(arg))

def print_code(code: str, section = None):
	if section != None:
		print(blue(
			f" ~ ({str(section)}) ~ "
		))
	print(green(code))
 
def print_object_info(obj) -> None:
     print("Type: ", type(obj))
     print("Dir: ", dir(obj))


	



def print_super_section(name: str, *args):
    print("\n\n")
    divider = dividers["double"] 
    print(magenta(dividers["double"] ))
    print()
    print (magenta(f"===== {name} ===== \n").center(len(dividers["double"] )))
    print(magenta(dividers["double"] ))
    print("Sections: ")
    for arg in args:
            print("\n")
            print(green(blue("> "+ arg)))
            print()
    print("\n\n")
    
	