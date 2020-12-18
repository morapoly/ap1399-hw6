from league import Team, Match, Weeks, League

def read_data(file_name, year):
    teams = []
    wm = []
    with open(file_name, "r") as fs:
        for line in fs.readlines():
            if line.find("table") > -1 and line.find(":") > -1:
                str_list = line[line.find("[") + 1 : line.find("]")]
                for words in str_list.split():
                    words = words.strip(",")
                    if words.find('"') >= 0:
                        teams.append(Team(words.strip('"')))
                    elif words.find("'") >= 0:
                        teams.append(Team(words.strip("'")))

            if line.find("week") >= 0 and line.find(":") >= 0:
                wm.append([line[:line.find(":")].strip("week").split()[0], line[line.find(":") + 1 :].strip("\n"),])

    weeks_list = []
    for i in range(int(len(teams) * (len(teams) - 1) / 2)):
        weeks_list.append(Weeks(i))
    for ob in wm:
        weeks_list[int(ob[0]) - 1].add_match(Match(ob[1]))
    lo = League(teams, year)
    for week in weeks_list:
        lo.add_week(week)
    return lo