
START = 'abc-xyz'
GOAL  = 'abc-xyz'
RR = 'abc'
LR = 'xyz'

def swap_positions(s,i,j):
    assert i < j  #if i < j is TRUE then run the program otherwise stop execution
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

def apply_move(s,f):
    i = s.index(f)
    if f in RR: # go right
        if i+1 < len(s) and s[i+1] == '-':
            return swap_positions(s,i,i+1)
        if i+2 < len(s) and s[i+1] != '-' and s[i+2] == '-':
            return swap_positions(s,i,i+2)
    if f in LR: # go left
        if i-1 >= 0 and s[i-1] == '-':
            return swap_positions(s,i-1,i)
        if i-2 >= 0 and s[i-1] != '-' and s[i-2] == '-':
            return swap_positions(s,i-2,i)

def show_state(s):
    print (s)

def next_moves(s):
    i = s.index('-')
    ms = []
    # in from the left
    if i-1 >= 0 and s[i-1] in RR:
        ms.append(s[i-1])
    if i-2 >= 0 and s[i-2] in RR:
        ms.append(s[i-2])
    # in from the right
    if i+1 < len(s) and s[i+1] in LR:
        ms.append(s[i+1])
    if i+2 < len(s) and s[i+2] in LR:
        ms.append(s[i+2])
    return ms

def possible(s):
    i = s.index('-')
    if i==0:
        if s[i+2] in RR:
            return False
        else:
            return True
    elif i==len(s):
        if s[i-2] in LR:
            return False
        else:
            return True
    else:
        return True

def search(s):
    work = set([("",s)])
    states = 0
    while work:
        path, cur = work.pop()
        states += 1
        show_state(cur)
        for k in next_moves(cur):
            succ = apply_move(cur, k)
            work.add((path+k, succ))
            print ("  ", path+k, " --> ",)
            show_state(succ)
            if succ == GOAL:
                print ("           !!! GOAL in", len(path)+1, " moves.")
    print ("Visited", states, "states.")

print("===== BFS =====")
search(START)

def dfs2(s,visited=[],path=[]):

    if s==GOAL:
        #print(visited,count,len(visited))
        print ("           !!! GOAL in", len(path), " moves.")
        # [print(item) for item in visited]
        result = ''.join(str(item) for item in path)
        print(result)
        print ("\nVisited", len(visited), "states.")
        quit()
    else:
        for x in next_moves(s):
            po = possible(apply_move(s,x))
            if po==False:
                continue
            
            if apply_move(s,x) not in visited:
                print ("  ", path, " --> ",)
                print(apply_move(s,x))
                #print(visited)
                path.append(x)
                visited.append(apply_move(s,x))
                dfs2(apply_move(s,x),visited,path)
                path.pop()
                
print("====== DFS ======")
dfs2(START,visited=[],path=[])