import re

# string data given
string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

# using regular expression patterns and grouping into name groups.
players = re.compile(r'''           
    ^(?P<last_name>[\w\s]+),\s
    (?P<first_name>[\w\s]+):\s
    (?P<score>[\d]+)$
''', re.X | re.M)


class Players:

    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score

    def learn(self):
        return f"{self.first_name} is learning to code!"


# looping over regular expression pattern name groups dictionary and intializing each player
for player in players.finditer(string):
    p = Players(player["last_name"], player["first_name"], player["score"])
    print(p.learn())

