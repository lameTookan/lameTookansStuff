from collections import namedtuple
import os 

from enum import Enum
import colors as c 
terminal_size = os.get_terminal_size()
terminal_cols = terminal_size.columns

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
    "fancy": "▅▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▅",
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

auto_double_cyan = c.cyan("══"*int(terminal_cols//2))
auto_center_stars = get_divider("star").center(terminal_cols, " ")

basic = get_divider("basic")
double = get_divider("double")
