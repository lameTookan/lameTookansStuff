import dividers as d
import colors as c

class Notes:
    def __init__(self):
        pass

    def print_intro(self, *args):
        for arg in args:
            print(c.yellow(arg), "\n")

    def print_section(self, section: int, *args, divider = True):
        print("\n\n")
        if divider:
            print(c.magenta(d.basic))
        print()
        print (c.magenta(f"===== ({str(section)}) ===== \n"))
        
        for arg in args:
                print(c.blue(arg))
                print()

    def print_sub(self, section: str, *args):
        template = c.magenta("\n> {} <").format(section)
        print(template)
        if args:
            for arg in args:
                print(c.cyan(arg))

    def print_code(self, code: str, section = None):
        if section != None:
            print(c.blue(
                f" ~ ({str(section)}) ~ "
            ))
        print(c.green(code))

    def print_object_info(self, obj) -> None:
        print("Type: ", type(obj))
        print("Dir: ", dir(obj))

    def print_super_section(self, name: str, table_of_contents: dict,  *args):
        """Super section(Collection Of Sections))"""
        print("\n\n")
        double = c.magenta("═" *120)
        basic = c.cyan("+-" * 60)
        print(c.magenta(double))
        print()
        print (c.magenta(f"|-------->{name}<--------|").center(len(double)))
        print()
        print(c.magenta(double))
        indents = " " * 4
        
        print()
        for section in table_of_contents:
            print(c.magenta(f"{indents}{str(section)} -> ") +  table_of_contents[section])
            
        print()
                
        for arg in args:
                
                print(c.green(c.blue(" "+ arg)))
              
        print("\n\n")

notes = Notes()
def main():
    """Test the PrintUtils class"""
    print("Test Print Super Section")
    table_of_contents = {
        "1": "Section 1",
        "2": "Section 2",
        "3": "Section 3",
        "4": "Section 4",
    }
    notes.print_super_section("Test Super Section", table_of_contents, "Test 1", "Test 2", "Test 3")
    
if __name__ == "__main__":
    main()