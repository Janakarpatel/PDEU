class DFS:
    def _init_(self):
        self.states = [[0,1],[1,0],[1,1],[0,2],[2,0]]
        self.visited = set()
        self.q = [[3,3,0]]
        self.start = [3,3,0]
        self.check = Problem()
        self.parent = {}

    def dfs(self, node = [3,3,0]):
        self.visited.add(str(node)) 

        if self.check.isfinal(node):
            ans = []
            temp = str(node)
            while temp!= str(self.start):
                ans.append(temp)
                temp = self.parent.get(temp)
            ans.append(self.start)
            return [ans, True]

        children = self.generate(node)
        for child in children:
            if str(child) not in self.visited:
                x, y = self.dfs(child)
                if y == True:
                    return [x, True]
        return [[], False]


    def generate(self, node):
        valid = []
        for state in self.states:
                if node[2] == 0:
                    nex = [node[0]-state[0],node[1]-state[1],1]
                    if self.check.isValid(nex):
                        if str(nex) not in self.visited:
                            self.parent.update({str(nex):str(node)})
                            valid.append(nex)
                else:
                    nex = [node[0]+state[0],node[1]+state[1],0]
                    if self.check.isValid(nex):
                        if str(nex) not in self.visited:
                            self.parent.update({str(nex):str(node)})
                            valid.append(nex)
        return valid