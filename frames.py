from abc import ABC, abstractmethod
from dataclasses import dataclass
"""Make a frame around text using unicode characters. Can use any single character as a frame element."""
@dataclass
class FrameElements:
    top_left: str
    top_right: str
    bottom_left: str
    bottom_right: str
    top: str
    bottom: str
    left: str
    right: str


asterisk_frame = FrameElements(
    top_left="⁎",
    top_right="⁎",
    top="⁎",
    bottom_left="⁎",
    bottom_right="⁎",
    bottom="⁎",
    left = "⁑",
    right = "⁑"
)
light_box_frame = FrameElements("┌", "┐", "└", "┘", "─", "─", "│", "│")
rounded_box_frame = FrameElements("╭", "╮", "╰", "╯", "─", "─", "│", "│")
super_heavy_frame = FrameElements(bottom_left="▙", bottom_right="▟", top_left="▛", top_right="▜", top="▀", bottom="▄", left="▌", right="▐")
wavy_frame = FrameElements(left="│",right = "│", top="~", bottom="~", top_left="╭", top_right="╮", bottom_left="╰", bottom_right="╯" )
dot_frame = FrameElements(
    top_left = ".",
    top_right=".",
    bottom_left=".",
    bottom_right=".",
    right="┋",
    left = "┋",
    bottom=".",
    top="."
)


box_frame = FrameElements("╔", "╗", "╚", "╝", "═", "═", "║", "║")
frames = {
    "asterisk": asterisk_frame,
    "light_box": light_box_frame,
    "rounded_box": rounded_box_frame,
    "super_heavy": super_heavy_frame,
    "wavy": wavy_frame,
    "box": box_frame,
    "dot": dot_frame
}

def frame_text(text: str, *args, frame_elements: FrameElements = box_frame, padding = (4, 4)) -> str:
    """Creates a frame around text.
    :param text:int  The text to frame.
    :args:int  Additional text to frame.(arg per line)
    :param frame_elements:FrameElements  The frame elements to use.
    :param padding:tuple  The padding to use. (horizontal, vertical)
    
    
    
    """
    if not isinstance(frame_elements, FrameElements):
        raise TypeError("frame_elements must be an instance of AbstractFrameElements")
    padding_horizontal, padding_vertical = padding
    lines = text.split("\n")
    lines.extend(args)
    max_len = max([len(line) for line in lines])
    # find max length of line
   
    
    
    width = max_len + padding_vertical #add padding to width to get the total width of frame
   
    top_row = f"{frame_elements.top_left}{frame_elements.top * width}{frame_elements.top_right}"
    bottom_row = f"{frame_elements.bottom_left}{frame_elements.bottom * width}{frame_elements.bottom_right}"
    horizontal_padding = [f"{frame_elements.left}{(' ' * width)}{frame_elements.right}" for _ in range((padding_horizontal//2) )] 
    rows = [top_row, *horizontal_padding]
    
    #make the padding rows(added before and after text)

    # now add the text
    for line in lines:
        line = line.center(width, " ") #center the text in the frame
        line = f"{frame_elements.left}{line}{frame_elements.right}" #add the left and right frame elements
        rows.append(line)
    # now add the bottom rows
    
    rows.extend(horizontal_padding)
    # make the bottom row
    rows.append( bottom_row)
    return "\n".join(rows)
@dataclass
class FrameElementsDimensions:
        top: int 
        bottom: int
        left: int
        right: int
        top_left: int
        bottom_left: int
        top_right: int
        bottom_right: int

         
    
def main():
    frame_list = []
    for key, value in frames.items():
        text = [
            "Hello", 
            "This is the ", 
            f"{key} frame",
            "It is very cool"
        ]
        frame_list.append(frame_text(frame_elements=value, *text))
    print("\n\n".join(frame_list))
    with open("frames.txt", "w") as f:
        f.write("\n\n".join(frame_list))
if __name__ == "__main__":
    main()