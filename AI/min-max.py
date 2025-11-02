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



def display(node,level=0):
    if node.children is None:
        return
    print("|"+"-"*level+node.name)
    for child in node.children:
        display(child,level+1) 


if __name__=='__main__':
    
    h = node('H',-1,[])
    i = node('I',4)
    j = node('J',2)
    k = node('K',6)
    l = node('L',-3)
    m = node('M',-5)
    n = node('N',0)
    o = node('O',7)

    d = node('D',0,[h,i])
    g = node('G',0,[n,o])
    f = node('F',0,[l,m])
    e = node('E',0,[j,k])
    d = node('D',0,[h,i])
    c = node('C',0,[f,g])
    b = node('B',0,[d,e])
    a = node('A',0,[b,c])


    # nam,val,child = input("enter").split()
    # print(child)
    

    # n = input("Enter The Number of Nodes")
    # for i in range(int(n)):
    #     print("If leaf node:0  or node:1")
    #     p = int(input("enter choice"))
    #     if p==0:
    #         nam = input("Enter name of node in capital letter : ")
    #         val = input("Enter the utility value : ")
    #         nam = node(str(nam),val)
    #     elif p==1:
    #         nam = input("Enter name of node in capital letter : ")
    #         child = list(input('Enter the children of node ; '))
    #         nam = node(str(nam),0,child)
    #     else:
    #         print("not valid")

    # display(a)
    result,val = minmax(a,True,value={})
    print(val)
    print(result)
    # # show(a)
    
