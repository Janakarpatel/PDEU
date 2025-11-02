import sys

class node:
    def __init__(self,name,utility,children=[]):
        self.name = name
        self.utility = utility
        self.children = children

    def terminal(self):
        return not self.children



def alphabeta(node,maxi,alpha,beta,visited=[]):
    if node.terminal():
        return node.utility,visited
    
    if maxi:
        best_val = -sys.maxsize
        for child in node.children:
            val,list1 = alphabeta(child,False,alpha,beta,visited)
            best_val = max(best_val,val)
            alpha = max(alpha , best_val)
            visited.append(child.name)

            if beta<=alpha:
                break
        return best_val,visited
    else:
        best_val = sys.maxsize
        for child in node.children:
            val,list1 = alphabeta(child,True,alpha,beta,visited)
            best_val = min(best_val,val)
            beta = min(beta , best_val)
            visited.append(child.name)

            if beta<=alpha:
                break
        return best_val,visited


if __name__=='__main__':
    
    j = node('J',5)
    k = node('K',2)
    l = node('L',6)
    m = node('M',9)
    n = node('N',10)
    o = node('O',4)
    p = node('P',2)
    q = node('Q',0)
    r = node('R',0)
    d = node('D',-1)
    h = node('H',0,[q,r])
    e = node('E',0,[j,k])
    f = node('F',0,[l,m,n])
    g = node('G',0,[o,p])
    b = node('B',0,[d,e,f])
    c = node('C',0,[g,h])
    a = node('A',0,[b,c])

    mini = -sys.maxsize
    maxi = sys.maxsize
    result,val = alphabeta(a, True, mini, maxi,visited=[])
    print(result)

    print(val)

    # h =[]
    # t=int(input("Enter total no of node: "))
    # l=int(input("Enter total no of terminal node: "))
    # p=t-l

    # for i in range(l):
    #     tem1 = input('Enter Terminal Node Name: ')
    #     tem2 = int(input('Enter Value: '))
    #     h.insert(i,node(tem1,tem2))
    
    # for w in range(0,l):
    #         print(w,h[w].name)

    # print(" %%%% Terminal nodes finished %%%% ")

    # for i in range(l,t):
    #     tem1 = input('Enter New Node Name : ')
    #     tem2 = int(input('Enter Value : '))
    #     ncn=int(input("Enter no of child nodes : "))
        
    #     for w in range(0,i):
    #         print(w,h[w].name)
    #     listt=[]

    #     for tob in range(ncn):
    #         t = int(input("Enter "+str(tob)+ " th child number from list: "))
    #         listt.append(h[t])

    #     h.insert(i,node(tem1,tem2,listt))
   

    # for w in range(0,(t+2)):
    #         print(w,h[w].name)
    # k = int(input("Enter index of node you want to search: "))
    # mm=bool(int(input("Do yo want Max search: ")))

    # mini = -sys.maxsize
    # maxi = sys.maxsize
    # result,val = alphabeta(h[k],mm,mini,maxi,visited=[])
    # print("Root Node Value : ")
    # print(result)
    # print("Total Visited Nodes : ")
    # print(val,len(val))