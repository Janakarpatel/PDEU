
class node:
    def __init__(self,name,utility,children=[]):
        self.name = name
        self.utility = utility
        self.children = children

    def terminal(self):
        return not self.children

def minmax(node,maxi,value={}):
    if node.terminal():
        return node.utility,value

    if maxi:
        maxeva = float('-inf')
        for item in node.children:
            eva,v = minmax(item,False,value)
            maxeva = max(maxeva,eva)
            value.update({str(node.name):int(maxeva)})
            #print(str(node.name),int(maxeva))
        return maxeva,value
    else:
        mineva = float('inf')
        for item in node.children:
            eva,v = minmax(item,True,value)
            mineva = min(mineva,eva)
            value.update({str(node.name):int(mineva)})
            #print(str(node.name),int(mineva))
        return mineva,value


if __name__=='__main__':
    h=[]
    t=int(input("Enter total no of node: "))
    l=int(input("Enter total no of terminal node: "))
    p=t-l

    for i in range(l):
        tem1 = input('Enter Terminal Node Name: ')
        tem2 = int(input('Enter Value: '))
        h.insert(i,node(tem1,tem2))
    for w in range(0,l):
            print(w,h[w].name)

    print(" %%%% Terminal nodes finished %%%% ")

    for i in range(l,t):
        tem1 = input('Enter New Node Name : ')
        tem2 = int(input('Enter Value : '))
        ncn=int(input("Enter no of child nodes : "))
        
        for w in range(0,i):
            print(w,h[w].name)
        listt=[]

        for tob in range(ncn):
            t = int(input("Enter "+str(tob)+ " th child number from list: "))
            listt.append(h[t])

        h.insert(i,node(tem1,tem2,listt))
   

    for w in range(0,(t+1)):
            print(w,h[w].name)
    k = int(input("Enter index of node you want to search: "))
    mm=bool(int(input("Do yo want Max search: ")))
    result,val = minmax(h[k],mm,value={})
    print(val)
    print(result)
