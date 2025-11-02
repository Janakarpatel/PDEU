#  8 puzzle problem.
#  A * algorithm to find path between initial node to goal node 
#  state will be [[1,2,3],
#                 [4,5,6],
#                 [7,8,_]] like this 

goal = [[1,2,3],[4,5,6],[7,8,'-']]
start = [[1,2,3],[4,5,6],[7,'-',8]]


def copy(item):
    temp = []
    for i in item:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp 

def heuristic(item,depth):
    temp = 0
    for i in range(3):
        for j in range(3):
            if item[i][j] != goal[i][j]:
                temp+=1
    
    return temp+depth 

# print(heuristic(start))
# print(heuristic(goal))

def findpos(item):
    for i in range(3):
        for j in range(3):
            if item[i][j] == '-':
                return i,j


def swap(item,i,j):
    m,n = findpos(item)
    temp = item[m][n]
    item[m][n] = item[i][j]
    item[i][j] = temp
    return item


def dekhadTaro(item):
    for i in range(3):
        print(item[i])
    print()


def generatechild(item):
    child=[]
    m,n = findpos(item)

    possible_list = []
    if(m>=1):#for up move
        possible_list.append([m-1,n])
    if(m<=1):#for down move
        possible_list.append([m+1,n])
    if(n>=1):#for left move
        possible_list.append([m,n-1])
    if(n<=1):#for right move
        possible_list.append([m,n+1])


    for i in possible_list:
        tempo = copy(item)
        tmp = swap(tempo,i[0],i[1])
        child.append(tmp)

    return child


# result = generatechild(start,child=[])
# print(result)

def dfs(sta,goal,visited=[]):
    if sta == goal:
        return visited
    else:
        lst = generatechild(sta)
        for i in lst:
            if i not in visited:
                temp = copy(i)
                visited.append(temp)
                return dfs(i,goal,visited)


result = dfs(start,goal,visited=[])

print(result)



#A star algorithm
def astar(sta,open=[],closed=[]):
    
   open.append(sta)
   while True:
       cur = open[0]

       print("")
       print("  | ")
       print("  | ")
       print(" \\\'/ \n")
       for i in cur:
            for j in i:
               print(j,end=" ")
            print("")

       if (heuristic(cur)==0):
           break
 
       for i in generatechild(cur):
           open.append(i)
       
       closed.append(cur)
       del open[0]

       open.sort(key = lambda x:heuristic(x),reverse=False)


# astar(start,open=[],closed=[])