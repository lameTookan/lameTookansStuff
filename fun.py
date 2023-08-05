from colors import COLORS_BAG
import dividers as div

class DecorateText:
    """A quick little class to decorate text with dividers and colors
    Dependencies: colors.py, dividers.py
    Methods:
        double_cyan_m(text: str) -> str Double cyan divider with magenta text
        temple_div(text: str) -> str Yellow temple divider with magenta text
    """
    divider_temple = "╬╬════════════════════════════════════════════════════════════════════════════╬╬"
    def double_cyan_m(self, text):
        divider = f"{COLORS_BAG.CYAN}{'═'*100}{COLORS_BAG.RESET}"
        result = [
            divider,
            "\n",
            f"{COLORS_BAG.MAGENTA}|---------->{text}<----------|{COLORS_BAG.RESET}".center(len(divider)),
            "\n",
            divider
        ]
        return "\n".join(result)
    def temple_div(self, text) -> str:
     
        divider = f"{COLORS_BAG.YELLOW}{self.divider_temple}{COLORS_BAG.RESET}"
        temple_length = len(divider)
        result = [ 
           divider,
           "\n",
           f"{COLORS_BAG.YELLOW}|---------->{text}<----------|{COLORS_BAG.RESET}".center(temple_length),
           "\n",
           divider, 
        ]
        return "\n".join(result)
text_decorator = DecorateText()
def test_double_cyan_m():
    print(DecorateText().double_cyan_m("Hello World!"))
    print(DecorateText().temple_div("Hello World!"))

if __name__ == "__main__":
    test_double_cyan_m()
   