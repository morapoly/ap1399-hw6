from copy import copy

class Match:
    def __init__(self, input_string):
        self.input_string = input_string.split() # making string list from input
        self.home = self.input_string[0]
        self.home_goals = self.input_string[1]
        self.away = self.input_string[4]
        self.away_goals = self.input_string[3]
       
    def data(self):
        t0 = 1
        t1 = int(int(self.home_goals) > int(self.away_goals))
        t2 = int(int(self.home_goals) == int(self.away_goals))
        t3 = int(int(self.home_goals) < int(self.away_goals))
        t4 = int(self.home_goals)
        t5 = int(self.away_goals)
        t6 = int(self.home_goals) - int(self.away_goals)
        t7 = int(int(self.home_goals) == int(self.away_goals))* 1 + int(int(self.home_goals) > int(self.away_goals))* 3
        homeTuple = (t0, t1, t2, t3, t4, t5, t6, t7)
        awaytuple = (
            1, homeTuple[3], homeTuple[2], homeTuple[1], homeTuple[5], homeTuple[4], homeTuple[6] * -1,
            1 if homeTuple[7] == 1 else 3 - homeTuple[7],
        )
        return homeTuple, awaytuple
    
    def __str__(self):
        return f"{self.home} {self.home_goals}  -  {self.away_goals} {self.away}"

    def __repr__(self):
        return f"{self.home} {self.home_goals}  -  {self.away_goals} {self.away}"
    
class Weeks:
    def __init__(self, weeks, matches=[]):
        self.weeks = weeks
        self.matches = matches.copy()

    def add_match(self, match):
        for m in self.matches:
            if (m.home == match.home or m.home == match.away or m.away == match.home or m.away == match.away):
                break
        else:
            self.matches.append(match)
    
    def __str__(self):
        s = ""
        for m in self.matches:
            s += f"{m}\n"
        return s[:len(s)-1]

    def __repr__(self):
        s = ""
        for m in self.matches:
            s += f"{m}\n"
        return s[:len(s)-1]
    
class Team:
    all_teams = 0

    def __init__(self, teamName):
        Team.all_teams += 1
        self.name = teamName
        self.rank = Team.all_teams
        self.matches = []
        self.mp = 0
        self.l = 0
        self.d = 0
        self.w = 0
        self.ga = 0
        self.gd = 0
        self.gf = 0
        self.pts = 0

    def add_match(self, match):
        if match.home == self.name:
            i = 0
        elif match.away == self.name:
            i = 1
        else:
            return
        self.matches.append(match)
        self.w += match.data()[i][1]
        self.d += match.data()[i][2]
        self.l += match.data()[i][3]
        self.gf += match.data()[i][4]
        self.ga += match.data()[i][5]
        self.gd += match.data()[i][6]
        self.pts += match.data()[i][7]
        self.mp += 1

    def __del__(self):
        Team.all_teams -= 1

    def __str__(self):
        print_str = f"{self.rank} {self.name} {self.mp} {self.w} {self.d} {self.l} {self.gf} {self.ga} {self.gd} {self.pts}"
        return print_str

    def __repr__(self):
        print_str = f"{self.rank} {self.name} {self.mp} {self.w} {self.d} {self.l} {self.gf} {self.ga} {self.gd} {self.pts}"
        return print_str

class League:
    def __init__(self, teams, year):
        self.all_weeks = []
        self.year = year
        self.standing = teams.copy()
        self.standing.sort(key=lambda input: input.rank)
        l = []
        for i in range(len(self.standing)):
            l.append(copy(self.standing[i]))
        self.all_standing = []
        self.all_standing.append(l.copy())

    def __add_match__(self, match): # using __ to make add_match in private manner 
        for sl in self.standing:
            sl.add_match(match)

    def add_week(self, week):
        self.all_weeks.append(week)
        for wm in week.matches:
            self.__add_match__(wm)
        self.standing.sort(reverse=True, key=lambda input: (input.pts, input.gd, input.gf, input.w, [-ord(l) for l in input.name],),)
        for i in range(len(self.standing)):
            self.standing[i].rank = i + 1
        l = []
        for i in range(len(self.standing)):
            l.append(copy(self.standing[i]))
        self.all_standing.append(l.copy())

    def __str__(self):
        temp_str = "team"
        print_str = f"#  {temp_str} mp  w   d   l   gf  ga  gd  pts\n"
        for m in self.standing:
            print_str += f"{m}\n"
        return print_str[: len(print_str) - 1]
    
    def __repr__(self):
        temp_str = "team"
        print_str = f"#  {temp_str} mp  w   d   l   gf  ga  gd  pts\n"
        for m in self.standing:
            print_str += f"{m}\n"
        return print_str[: len(print_str) - 1]