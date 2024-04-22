import sys

comands = dict() # игрок: его команда
totalgoalsfor = dict() # количество голов забитое командой
totalgoalsby = dict() # кол-во голов забитое игроком
goalsonminute = dict() # голы игроков по минутам
gamecnt = dict() # количество игр сыгранных командами
scoreopensc = dict() # сколько раз команда первая забивала
scoreopensp = dict() # сколько раз игрок открывал счёт

g1 = g2 = 0
firstgoal1 = True
firstgoal2 = True

for line in sys.stdin:
    line = line.strip()

    if g1 > 0:
        line = line[:len(line) - 1]
        time = int(line[len(line) - 2:].strip())
        name = line[:len(line) - 2].strip()
        if name not in comands:
            comands[name] = com1
        
        if name not in totalgoalsby:
            totalgoalsby[name] = 0
        totalgoalsby[name] += 1

        if name not in goalsonminute:
            goalsonminute[name] = dict()
        if time not in goalsonminute[name]:
            goalsonminute[name][time] = 0
        goalsonminute[name][time] += 1

        if firstgoal1:
            timetimefirstgoal = time
            namefirstgoal = name
            firstgoal1 = False
            if g2 <= 0:
                if com1 not in scoreopensc:
                    scoreopensc[com1] = 0
                scoreopensc[com1] += 1
                if name not in scoreopensp:
                    scoreopensp[name] = 0
                scoreopensp[name] += 1

        g1 -= 1

    elif g1 <= 0 and g2 > 0:
        line = line[:len(line) - 1]
        time = int(line[len(line) - 2:].strip())
        name = line[:len(line) - 2].strip()
        if name not in comands:
            comands[name] = com2
        
        if name not in totalgoalsby:
            totalgoalsby[name] = 0
        totalgoalsby[name] += 1

        if name not in goalsonminute:
            goalsonminute[name] = dict()
        if time not in goalsonminute[name]:
            goalsonminute[name][time] = 0
        goalsonminute[name][time] += 1

        if firstgoal2:
            firstgoal2 = False
            if time < timetimefirstgoal or firstgoal1:
                if com2 not in scoreopensc:
                    scoreopensc[com2] = 0
                scoreopensc[com2] += 1
                if name not in scoreopensp:
                    scoreopensp[name] = 0
                scoreopensp[name] += 1
            else:
                if com1 not in scoreopensc:
                    scoreopensc[com1] = 0
                scoreopensc[com1] += 1
                if namefirstgoal not in scoreopensp:
                    scoreopensp[namefirstgoal] = 0
                scoreopensp[namefirstgoal] += 1

        g2 -= 1

    elif line[0] == '"':
        com1, _, com2, score = line[1:].split('"')
        g1, g2 = map(int, score.strip().split(':'))
        firstgoal1 = firstgoal2 = True
        timetimefirstgoal = 100
        
        if com1 not in totalgoalsfor:
            totalgoalsfor[com1] = 0
        totalgoalsfor[com1] += g1
        if com2 not in totalgoalsfor:
            totalgoalsfor[com2] = 0
        totalgoalsfor[com2] += g2

        if com1 not in gamecnt:
            gamecnt[com1] = 0
        gamecnt[com1] += 1
        if com2 not in gamecnt:
            gamecnt[com2] = 0
        gamecnt[com2] += 1

    elif line[:len('Total goals for')] == 'Total goals for':
        com = line[len('Total goals for'):].strip().strip('"')
        try:
            print(totalgoalsfor[com])
        except:
            print(0)
    
    elif line[:len('Mean goals per game for')] == 'Mean goals per game for':
        com = line[len('Mean goals per game for'):].strip().strip('"')
        try:
            print(totalgoalsfor[com] / gamecnt[com])
        except:
            print(0)

    elif line[:len('Total goals by')] == 'Total goals by':
        plr = line[len('Total goals by'):].strip()
        try:
            print(totalgoalsby[plr])
        except:
            print(0)

    elif line[:len('Mean goals per game by')] == 'Mean goals per game by':
        plr = line[len('Mean goals per game by'):].strip()
        try:
            print(totalgoalsby[plr] / gamecnt[comands[plr]])
        except:
            print(0)

    elif line[:len('Goals on minute')] == 'Goals on minute':
        time = line[len('Goals on minute '):2 + len('Goals on minute ')].strip()
        plr = line[len('Goals on minute ## by'):].strip()
        time = int(time.strip())
        try:
            print(goalsonminute[plr][time])
        except:
            print(0)

    elif line[:len('Goals on first')] == 'Goals on first':
        time = line[len('Goals on first '):2 + len('Goals on first ')].strip()
        plr = line[len('Goals on first ## minutes by'):].strip()
        time = int(time.strip())
        cnt = 0

        if plr in goalsonminute:
            for i in range(time + 1):
                try:
                    cnt += goalsonminute[plr][i]
                except:
                    None
        
        print(cnt)

    elif line[:len('Goals on last')] == 'Goals on last':
        time = line[len('Goals on last '):2 + len('Goals on last ')].strip()
        plr = line[len('Goals on last ## minutes by'):].strip()
        time = int(time.strip())
        cnt = 0

        if plr in goalsonminute:
            for i in range(91 - time, 91):
                try:
                    cnt += goalsonminute[plr][i]
                except:
                    None
        
        print(cnt)

    elif line[:len('Score opens by')] == 'Score opens by':
        name = line[len('Score opens by'):].strip()
        if name[0] == '"':
            com = name.strip('"')
            try:
                print(scoreopensc[com])
            except:
                print(0)
        else:
            try:
                print(scoreopensp[name])
            except:
                print(0)