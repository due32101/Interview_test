# Connected_Graph

*2019.9.12* from interview of Deep Force

There is a map of several cities, the city connected to the city by road, but some of the cities won't be connected to the other cities.
Please write an function to return an **boolean** to show if you can arrive all the cities on the map no matter where you are.

Example:

![image](https://github.com/due32101/Interview_test/blob/master/connected_graph/images/example.png)

In Figure(a), A, B, C, D are connected to each other, but E,F aren't connected to other cities, so in this case, you should return **False**; In Figure(b), A, B, C, D, E, F are connected to each other, so you should return **True**

The input data will be an matix, the matrix of Figure(a) is shown as:
```
[[1,1,1,0,0,0],
 [1,1,0,1,0,0],
 [1,0,1,0,0,0],
 [0,1,0,1,0,0],
 [0,0,0,0,1,1],
 [0,0,0,0,1,1]]
```
The matrix of Figure(b) is shown as
```
[[1,1,1,0,0,0],
 [1,1,0,1,0,0],
 [1,0,1,0,1,0],
 [0,1,0,1,0,0],
 [0,0,1,0,1,1],
 [0,0,0,0,1,1]]
```



※The test case contain 6 graphs:

![image](https://github.com/due32101/Interview_test/blob/master/connected_graph/images/connect_test.png)
