

class ANSI:
    """
    background: allows background formatting. Accepts ANSI codes between 40 and 47, 100 and 107
style_text: corresponds to formatting the style of the text. Accepts ANSI code between 0 and 8
color_text:  Corresponds to the text of the color. Accepts ANSI code between 30 and 37, 90 and 97

    """
    def background(code):
        """
        Allows background formatting. Accepts ANSI codes between 40 and 47.
            
            * 40  -> black
            * 41  -> red
            * 42  -> green
            * 43  -> yellow
            * 44  -> orange
            * 45  -> purple
            * 46  -> blue
            * 47  -> white

        """
        return "\33[{code}m".format(code=code)
    
    def style(code):
        """
        Corresponds to formatting style of the text. Accepts ANSI code between
        0 and 8.
        """
        return "\33[{code}m".format(code=code)
 
    def color(code):
        """
        Corresponds to the text of the color. Accepts ANSI code between 30 and
        37.
            
            * 30  -> black
            * 31  -> red
            * 32  -> green
            * 33  -> yellow
            * 33  -> orange
            * 35  -> purple
            * 36  -> blue
            * 37  -> white

        """
        return "\33[{code}m".format(code=code)