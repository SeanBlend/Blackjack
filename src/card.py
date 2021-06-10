class Card:
    width = 19
    height = 11

    empty = "|" + " "*(width-2) + "|"
    top = " " + "_"*(width-2)
    bottom = "|" + top[1:] + "|"
    letter1 = "|  {}              |"
    letter2 = "|              {}  |"

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def as_string(self):
        s = ""
        s += self.top + "\n"
        s += self.empty + "\n"
        s += self.letter1.format(str(self.num)) + "\n"
        for _ in range(8):
            s += self.empty + "\n"
        s += self.letter2.format(str(self.num)) + "\n"
        s += self.bottom + "\n"

        return s


SPADE = r"""
  /\
 /  \
/_/\_\
  /\
"""

HEART = r"""
/^\/^\
\    /
 \  /
  \/
"""

CLUBS = r"""
   _
 _|_|_
|_|||_|
  /_\
"""

DIAMOND = r"""
   /\
  /  \
  \  /
   \/
"""