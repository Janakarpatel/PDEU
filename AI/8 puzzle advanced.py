class Node:

    def __init__(self,state,level,fval):
        self.state = state
        self.level=level
        self.fval=fval
    
    def findpos(self,item):
        for i in range(3):
            for j in range(3):
                if item[i][j] == 0:
                    return i,j
                
    def swap(self,item,i,j):
        m,n = self.findpos(item)
        temp = item[m][n]
        item[m][n] = item[i][j]
        item[i][j] = temp
        return item
    
    def copy(self,item):
        temp = []
        for i in item:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp 
    
    def generatechild(self):

        m,n = self.findpos(self.state)

        possible_list = []
        if(m>=1):#for up move
            possible_list.append([m-1,n])
        if(m<=1):#for down move
            possible_list.append([m+1,n])
        if(n>=1):#for left move
            possible_list.append([m,n-1])
        if(n<=1):#for right move
            possible_list.append([m,n+1])

        child=[]
        for i in possible_list:
            tempo = self.copy(self.state)
            tmp = self.swap(tempo,i[0],i[1])
            chi = Node(tmp,self.level+1,0)
            child.append(chi)

        return child


class enviroment:

    def heuristic(self,item,goal):
        temp = 0
        for i in range(3):
            for j in range(3):
                if item[i][j] != goal[i][j] and item[i][j]!=0:
                    temp+=1
        return temp 

    def function(self,item,goal):
        return self.heuristic(item.state,goal)+item.level
    
    def solv(self,item):
        invcount = 0
        sample=[]
        for i in range(3):
            for j in range(3):
                sample.append(item[i][j])

        for i in range(0,9):
            for j in range(j,i):
                if sample[j]!=0 and sample[i]!=0 and sample[i]>sample[j]:
                    invcount+=1

        return invcount
    
    def astar(self):
        print(" - - - Intial State - - - ")
        print('\n')
        sta = [[2,5,3],[1,0,6],[4,7,8]]
        goal = [[1,2,3],[4,5,6],[7,8,0]]
        open=[]
        closed=[]
        visited=[]

        start = Node(sta,0,0)
        start.fval = self.function(start,goal)
        open.append(start)
        visited.append(start)

        for i in start.state:
            for j in i:
                print(j,end=" ")
            print("")

        # count = self.solv(start.state)+1
        # if (count % 2 == 0):
        #     solv = True
        # else:
        #     solv =  False
        #     print('---Unsolvalbe Problem---')

        count = 1
        while True:
            cur = open[0]
            print("")
            print(" \\\/ \n")
            count+=1
            for i in cur.state:
                for j in i:
                    print(j,end=" ")
                print("")

            if(self.heuristic(cur.state,goal)==0):
                break

            for i in cur.generatechild():
                if i not in visited:
                    visited.append(i)
                    i.fval=self.function(i,goal)
                    open.append(i)
            closed.append(cur)

            del open[0]
            open.sort(key = lambda x:x.fval,reverse=False)
        
        print('\n')
        print(" - - - Final State - - - ")
        
        print('--------------------------------------------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------------------------------------------------')

        print('\n')
        print(" - - - - -  Details - - - - - -")
        print('\n')

        print('=== Total Visited States ===  :',len(visited))
        print('\n')
        print('=== Required steps to solved problem ===  :',(count-1))
        print('\n')




# goal = [[1,2,3],[4,5,6],[7,8,0]]
# p = Node(goal,7,3)
# n = p.generatechild()
# print(n)
# # print(p.state)
# q = enviroment()
# print(q.function(p,p))

print('--------------------------------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------------------------------')
print(' ___    _____ _____ _____ _____ __    _____    _____ _____ _____ _____ __    _____ _____ ')
print('| . |  |  _  |  |  |__   |__   |  |  |   __|  |  _  | __  |     | __  |  |  |   __|     |')
print('| . |  |   __|  |  |   __|   __|  |__|   __|  |   __|    -|  |  | __ -|  |__|   __| | | |')
print('|___|  |__|  |_____|_____|_____|_____|_____|  |__|  |__|__|_____|_____|_____|_____|_|_|_|')
print('                                                                                                                   ')
print('--------------------------------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------------------------------')
print('\n')

# main code 
p = enviroment()
p.astar()