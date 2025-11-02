#s[0,1,2] =  m ,c, b

def is_legal(s):

    if s[0]<0 or s[0]>3 or s[1]<0 or s[1]>3:
        return False
    if s[0]>0 and s[0]<s[1]:
        return False
    if (3-s[0])<0 or (3-s[0])>3 or (3-s[1])<0 or (3-s[1])>3:
        return False
    if (3-s[0])>0 and (3-s[0])<(3-s[1]):
        return False
    
    return True


def is_goal(s):
    if s == [0,0,1]:
        return True
    return False

def is_possible(s):
    q=[]
    state = [[1,0],[0,1],[1,1],[2,0],[0,2]]
    for item in state:
        if s[2]==0:
            curr=[s[0]-item[0],s[1]-item[1],1]
            if is_legal(curr):
                q.append(curr)
        else:
            curr = [s[0]+item[0],s[1]+item[1],0]
            if is_legal(curr):
                q.append(curr)
    
    return q


def bfs(s,states,q=[[3,3,0]],visited=set(),parent={}):
    for item in q:
        source = str(item)
        if is_goal(item):
            ans = []
            temp = source
            while temp!= str(s):
                ans.append(temp)
                temp = parent.get(temp)
            return ans,visited
        
        for state in states:
            if item[2]==0:
                next = [item[0]-state[0],item[1]-state[1],1]
                if is_legal(next):
                    if str(next) not in visited:
                        visited.add(str(next))
                        q.append(next)
                        parent.update({str(next):source})
            else:
                next = [item[0]+state[0],item[1]+state[1],0]
                if is_legal(next):
                    if str(next) not in visited:
                        visited.add(str(next))
                        q.append(next)
                        parent.update({str(next):source})


def dfs(s,start,visited=[]):
    visited.append(str(s))

    if is_goal(s):
        return [visited,True]
    
    child = is_possible(s)
    for c in child:
        if str(c) not in visited:
            x, y = dfs(c,start,visited)
            if y == True:
                return [x,True]
            visited.remove(str(c))
    return [[], False]



print("==== DFS ====")
possible_states = [[1,0],[0,1],[1,1],[2,0],[0,2]]
s = [3,3,0]
path1,v = dfs(s,s,visited=[])
print("Total Visited States",len(path1)-1)
for x,y in enumerate(path1):
     print(f"Step {x}: {y}")

print("==== BFS ====")
path,visit=bfs(s,possible_states,q=[[3,3,0]],visited=set(),parent={})
print("Total Visited States",len(visit)-1)
path.append(s)
path.reverse()
for x,y in enumerate(path):
    print(f"Step {x}: {y}")