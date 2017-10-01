import random
import math
    
visited = []
h = 0

#generates adjacency matrix based on n (number of nodes) and p (probability each edge exists)
def gengraph( n, p ):
    matrix = [[0 for i in range(n)] for j in range(n)];
    for i in range(n):
        for j in range(n):
            q = random.random()
            if(q<p):
                matrix[i][j] = 1
                matrix[j][i] = 1
    return(matrix)
#deoth first search algorithm
def Explore(G, v): 
    visited.append(v)
    for n in range(len(G[v])):
        if(G[v][n] == 1 and n not in visited):
            Explore(G, n)
        
        

if __name__ == "__main__":
    #this generates test cases based on different prbabilities
    n = 40
    #clist initialized, will be used to calculate probabilities for gengraph function
    clist = [0.2*i for i in range(15)]
    for i in range(15):
        c = clist[i]
        count = 0
        #probability calculated
        p = c/n
        for j in range(500):
            h = 0
            #graph generated
            temp = gengraph(n, p)
            #this part checks to see if there exists a connected component in the graph larger than 30
            visited = []
            while(len(visited) < len(temp[0])):
                for i in range(len(temp[0])):
                    if i not in visited:
                        Explore(temp, i)
                        break
                break
            #if there exists such component, count++
            if(len(visited) > 30):
                count += 1
        #output percent of graphs with a connected component larger than 30
        answer = 100*(count/500)
        print("percentage where t > 30 = %.8f" % answer)