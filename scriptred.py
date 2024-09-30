from random import randint 

name = 'sample4'

def moveTo(l , v , Pirate):
    position = Pirate.getPosition()
    if position[0] == l and position[1] == v:
        return 0
    if position[0] == l:
        return (position[1] < v) * 2 + 1
    if position[1] == v:
        return (position[0] > l) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > l) * 2 + 2
    else:
        return (position[1] < v) * 2 + 1
    
def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    o = pirate.getTeamSignal()
    print(type(y))
    s = pirate.trackPlayers()
    i = pirate.getID()
    i = i + "1"
    ce = "0"
    if(i!="1"):
        ce = (int(i)-1)/10
    t = pirate.getCurrentFrame()
    r = int(t/20.0)
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(up[-1]==1):
                s = up[-1] + str(x) + "," + str(y-1) + "/" + str(x) + "|" + str(y-1) + "/" + "2" + "/" + "2" 
            elif(sw[-1]==2):
                s = up[-1] + str(x) + "," + str(y-1) + "/" + "2" + "/" + str(x) + "|" + str(y-1) + "/" + "2"
            else:
                s = up[-1] + str(x) + "," + str(y-1) + "/" + "2" + "/" + "2" + "/" + str(x) + "|" + str(y-1)
        else:
            m = j.split("/")
            m[0] = up[-1] + str(x) + "," + str(y-1)
            if(up[-1]==1):
                m[1]=  str(x) + "|" + str(y-1)
            elif(up[-1]==2):
                m[2]=  str(x) + "|" + str(y-1)
            else:
                m[3]=  str(x) + "|" + str(y-1)
            s = "/".join(m)
        pirate.setTeamSignal(s)


    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(down[-1]==1):
                s = down[-1] + str(x) + "," + str(y+1) + "/" + str(x) + "|" + str(y+1) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = down[-1] + str(x) + "," + str(y+1) + "/" + "2" + "/" + str(x) + "|" + str(y+1) + "/" + "2"
            else:
                s = down[-1] + str(x) + "," + str(y+1) + "/" + "2" + "/" + "2" + "/" + str(x) + "|" + str(y+1)
        else:
            m = j.split("/")
            m[0] = down[-1] + str(x) + "," + str(y+1)
            if(down[-1]==1):
                m[1]=  str(x) + "|" + str(y+1)
            elif(down[-1]==2):
                m[2]=  str(x) + "|" + str(y+1)
            else:
                m[3]=  str(x) + "|" + str(y+1)
            s = "/".join(m)
        pirate.setTeamSignal(s)


    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(left[-1]==1):
                s = left[-1] + str(x-1) + "," + str(y) + "/" + str(x-1) + "|" + str(y) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = left[-1] + str(x-1) + "," + str(y) + "/" + "2" + "/" + str(x-1) + "|" + str(y) + "/" + "2"
            else:
                s = left[-1] + str(x-1) + "," + str(y) + "/" + "2" + "/" + "2" + "/" + str(x-1) + "|" + str(y)
        else:
            m = j.split("/")
            m[0] = left[-1] + str(x-1) + "," + str(y)
            if(left[-1]==1):
                m[1]=  str(x-1) + "|" + str(y)
            elif(left[-1]==2):
                m[2]=  str(x-1) + "|" + str(y)
            else:
                m[3]=  str(x-1) + "|" + str(y)
            s = "/".join(m)
        pirate.setTeamSignal(s)


    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(right[-1]==1):
                s = right[-1] + str(x+1) + "," + str(y) + "/" + str(x+1) + "|" + str(y) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = right[-1] + str(x+1) + "," + str(y) + "/" + "2" + "/" + str(x+1) + "|" + str(y) + "/" + "2"
            else:
                s = right[-1] + str(x+1) + "," + str(y) + "/" + "2" + "/" + "2" + "/" + str(x+1) + "|" + str(y)
        else:
            m = j.split("/")
            m[0] = right[-1] + str(x+1) + "," + str(y)
            if(right[-1]==1):
                m[1]=  str(x+1) + "|" + str(y)
            elif(right[-1]==2):
                m[2]=  str(x+1) + "|" + str(y)
            else:
                m[3]=  str(x+1) + "|" + str(y)
            s = "/".join(m)
        pirate.setTeamSignal(s)

        
    if (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(nw[-1]==1):
                s = nw[-1] + str(x-1) + "," + str(y-1) + "/" + str(x-1) + "|" + str(y-1) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = nw[-1] + str(x-1) + "," + str(y-1) + "/" + "2" + "/" + str(x-1) + "|" + str(y-1) + "/" + "2"
            else:
                s = nw[-1] + str(x-1) + "," + str(y-1) + "/" + "2" + "/" + "2" + "/" + str(x-1) + "|" + str(y-1)
        else:
            m = j.split("/")
            m[0] = nw[-1] + str(x-1) + "," + str(y-1)
            if(nw[-1]==1):
                m[1]=  str(x-1) + "|" + str(y-1)
            elif(nw[-1]==2):
                m[2]=  str(x-1) + "|" + str(y-1)
            else:
                m[3]=  str(x-1) + "|" + str(y-1)
            s = "/".join(m)
        pirate.setTeamSignal(s)

        
    if (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
            h = pirate.getTeamSignal() + "1"
            j = pirate.getTeamSignal()
            if(h=="1"):
                if(ne[-1]==1):
                    s = ne[-1] + str(x+1) + "," + str(y-1) + "/" + str(x+1) + "|" + str(y-1) + "/" + "2" + "/" + "2"
                elif(sw[-1]==2):
                    s = ne[-1] + str(x+1) + "," + str(y-1) + "/" + "2" + "/" + str(x+1) + "|" + str(y-1) + "/" + "2"
                else:
                    s = ne[-1] + str(x+1) + "," + str(y-1) + "/" + "2" + "/" + "2" + "/" + str(x+1) + "|" + str(y-1)
            else:
                m = j.split("/")
                m[0] = ne[-1] + str(x+1) + "," + str(y-1)
                if(ne[-1]==1):
                    m[1]=  str(x+1) + "|" + str(y-1)
                elif(ne[-1]==2):
                    m[2]=  str(x+1) + "|" + str(y-1)
                else:
                    m[3]=  str(x+1) + "|" + str(y-1)
                s = "/".join(m)
            pirate.setTeamSignal(s)

        
        
    if (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(se[-1]==1):
                s = se[-1] + str(x+1) + "," + str(y+1) + "/" + str(x+1) + "|" + str(y+1) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = se[-1] + str(x+1) + "," + str(y+1) + "/" + "2" + "/" + str(x+1) + "|" + str(y+1) + "/" + "2"
            else:
                s = se[-1] + str(x+1) + "," + str(y+1) + "/" + "2" + "/" + "2" + "/" + str(x+1) + "|" + str(y+1)
        else:
            m = j.split("/")
            m[0] = se[-1] + str(x+1) + "," + str(y+1)
            if(se[-1]==1):
                m[1]=  str(x+1) + "|" + str(y+1)
            elif(se[-1]==2):
                m[2]=  str(x+1) + "|" + str(y+1)
            else:
                m[3]=  str(x+1) + "|" + str(y+1)
            s = "/".join(m)
                
            

        pirate.setTeamSignal(s)
    if (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        h = pirate.getTeamSignal() + "1"
        j = pirate.getTeamSignal()
        if(h=="1"):
            if(sw[-1]==1):
                s = sw[-1] + str(x-1) + "," + str(y+1) + "/" + str(x-1) + "|" + str(y+1) + "/" + "2" + "/" + "2"
            elif(sw[-1]==2):
                s = sw[-1] + str(x-1) + "," + str(y+1) + "/" + "2" + "/" + str(x-1) + "|" + str(y+1) + "/" + "2"
            else:
                s = sw[-1] + str(x-1) + "," + str(y+1) + "/" + "2" + "/" + "2" + "/" + str(x-1) + "|" + str(y+1)
        else:
            m = j.split("/")
            m[0] = sw[-1] + str(x-1) + "," + str(y+1)
            if(sw[-1]==1):
                m[1]=  str(x-1) + "|" + str(y+1)
            elif(sw[-1]==2):
                m[2]=  str(x-1) + "|" + str(y+1)
            else:
                m[3]=  str(x-1) + "|" + str(y+1)
            s = "/".join(m)
                
            

        pirate.setTeamSignal(s)

    g = pirate.getTeamSignal()
    w = g.split("/")
    if (w[0] != "2" and g !="" and int(ce)%4==0):
        lo = w[0]
        l = lo.split(",")
        ad = int(l[0][1:])
        af = int(l[1])
    
        return moveTo(ad, af, pirate)

    else:
        if(g==""):
            if(int(ce)%4==1 and r<=5):
                q = randint(30,39)
                v = randint(1,20)
                return moveTo(q,v,pirate)
            elif(int(ce)%4==2 and r<=5):
                q = randint(1,10)
                v = randint(20,39)
                return moveTo(q,v,pirate)
            elif((int(ce)%4==3) and r<=5):
                q = randint(30,39)
                v = randint(30,39)
                return moveTo(q,v,pirate)
            else:
                return spread(pirate)
        else:
            u = g.split("/")
            if((int(ce)%4==1 or int(ce)%4==2 or int(ce)%4==3) and r>15):
                if((s[3]=="oppCaptured" or s[3]=="oppCapturing") and u[1] !="2" ):
                    fo = u[1].split("|")
                    kl = fo[0]
                    si = fo[1]
                    return moveTo(int(kl),int(si),pirate)
                elif((s[4]=="oppCaptured" or s[4]=="oppCapturing") and u[2] !="2" ):
                    fo = u[2].split("|")
                    kl = fo[0]
                    si = fo[1]
                    return moveTo(int(kl),int(si),pirate)
                elif((s[3]=="oppCaptured" or s[3]=="oppCapturing") and u[3] !="2" ):
                    fo = u[3].split("|")
                    kl = fo[0]
                    si = fo[1]
                    return moveTo(int(kl),int(si),pirate)
                else:
                    return spread(pirate)
            elif(int(ce)%4==1 and r<=15):
                q = randint(30,39)
                v = randint(1,20)
                return moveTo(q,v,pirate)
            elif(int(ce)%4==2 and r<=15):
                q = randint(1,10)
                v = randint(20,39)
                return moveTo(q,v,pirate)
            elif((int(ce)%4==3) and r<=15):
                q = randint(30,39)
                v = randint(30,39)
                return moveTo(q,v,pirate)
            else:
                return spread(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    h = s.split("/")


    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(h[0][0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            k = "2" + "/"+h[1]+"/"+h[2]+"/"+h[3]

            team.setTeamSignal(k)