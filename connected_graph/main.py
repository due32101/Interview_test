import numpy as np
import string
import pandas as pd

#define city name
city_name = list(string.ascii_uppercase)
#define connect graph(A-B, A-C, B-D, E)
graph = np.array([[1,1,1,0,0],
                  [1,1,0,1,0],
                  [1,0,1,0,0],
                  [0,1,0,1,0],
                  [0,0,0,0,1]])

def check_connect(graph):
    #define connect or not
    connect = False
    #calculate the length of city
    l = len(graph)
    #turn graph into dataframe
    graph_pd = pd.DataFrame(graph, columns = city_name[:l], index = city_name[:l])
    for k in city_name[:l]:
        #set a city array
        city = [k]
        #initailize start city i
        i = 0
        #check if city is connected to the other city
        while(i < len(city)):
            c = city[i] #pick the city in list
            connect_city = graph_pd.loc[graph_pd[c] == 1, c] #pick the connected city
            connect_city = connect_city.index.tolist()
            # if the city is not in the list, insert it
            for j in connect_city: 
                if j not in city:
                    city.append(j)
            i += 1
        #if the list's length same as the graph's length, then all the city connect
        if (len(city) == l):
            connect = True
            break
    return connect

#load test data
test = np.load('test.npy')
for t in test:
    print(check_connect(t))


