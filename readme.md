# Voronoi Games and Epsilon Nets
This is a compilation of code I have written for my undergraduate honours project done at the University of Manitoaba. The research is in computational geometry and very math heavy, so this code is primarily for doing initial testing of various algorithms and creating diagrams. The product of this research will eventually be a paper compiling out results, though this is still in the process of being created. Thank you to my advisor Dr. Jimmy Zhu and also Dr. Stephane Durocher for working with me and guiding me through this project.

My research question is as follows:

"In the (3,1) instance of the one round discrete Voronoi game, can the first player always win at least 1/2 of the points? Currently the bounds on the fraction of points that the first player can win is 7/15."

What this means is far from clear, so I've made an effort to explain it as best I can.

## Discrete Voronoi Games

Imagine two companies that are competing for customers, eg. Tim Hortons and Starbucks, in this example the companies are Red and Blue. There are a certain number of customers around the city and each company's goal is to open their stores closer to customers than the other.

![The customers](example_1.png)

The game proceeds as follows: first, Red opens up _r_ store(s).

![Red's stores](example_2.png)

The red lines represent the Voroni cells defined by each red store. Each store's Voronoi cell represents the regions on the map that are closest to it rather than other stores.

Next, Blue opens up _b_ store(s).

![Blue's stores](example_3.png)

Notice that the lines defining the Voronoi cells are re-drawn now and some of the customers that used to be closer to Red's stores are now closer to Blue's store.

The game is now over and each company "wins" customers in the Voronoi cells around their stores, in this case Blue wins 2 customers and Red wins 9.

An instance of the game is denoted (_r_, _b_), where _r_ and _b_ are the numbers of stores placed by Red and Blue respectively.

This is practical example of the game, in general, the customers will be a set of points in a plane, and the stores will be corresponding points placed by 2 theoretical players which each take one turn to place their points. Going forward I will keep refering to the game in terms of companies and stores though.

## Research into the Game
There are a number of areas of research relating to the game:
- What is the best strategy for Red to place it's stores?
    - Finding this in general is NP-Hard
- What is the optimal strategy for Blue to place it's stores?
    - This is known and can be done in polynomial time.
- What fractions of customers can each company win depending on the numbers of stores they place?

#### My Research
In general, finding the optimal placement of Red's stores is NP-Hard, but for specific cases, notably when Blue only has one store, there is research into finding out the minimum fraction of customers that Red can win. My research question is looking into this problem in the case where Red has 3 stores and Blue has 1, specifically trying to find a placement strategy for Red's stores that improves the minimum fraction of points that it can win from 7/15 to 1/2.

#### _Epsilon_-Nets
_Epsilon_-nets are a mathematical tool used to prove the bounds on the minimum fraction of points that Red can win. The basic idea behind an _epsilon_-net is that given a set of _n_ points and _epsilon_ in (0,1), and _epsilon_-net for that set of points is a smaller set of points such that no convex set can contain > (_epsilon * n_ points) without containing a point of the net. _Epsilon_ is dependent on the number of points in the net, and gets smaller as this number increases. This can be used to prove the bounds on the one round discrete Voronoi games by placing Red's stores as an _epsilon_-net for the customers, Voronoi cells are convex so Blue's single store's Voronoi cell cannot contain more than _epsilon * n_ customers without containing one of Red's stores as well, which it cannot do. In general, by placing Red's stores as an _epsilon_-net, Red will win at least [(1 - _epsilon_) * n] of the customers. 

_Epsilon_ depends on the number of points in the net, and the bounds are as follows:

| net points | lower bound | upper bound |
|------------|-------------|-------------|
|          1 |         2/3 |         2/3 |
|          2 |         4/7 |         4/7 |
|          3 |        5/11 |        8/15 |

The bounds on 3 points are not tight, so by reducing the upper bound to at least 1/2, I would be able to solve my research question!

Note that a __centerpoint__ is an _epsilon_-net comprised of only one point, and this term will be used frequently.

This is far more difficult than it seems though, and our focus has primarily been on sets of points already in convex position with our hope being that if we are able to solve this case we will be able to somehow extend our solution to the case where the points are in general position.

## Code Organization
All of this code has been for prototyping so none of it is particularly clean, for the most part there are two types of files, ones with utility functions used everywhere and ones with specific algorithms. There is a lot more code as well, but I am making an effort to only put code that I have cleaned up a bit in here.

## Dependencies
- __shapely__: used for "manipulation and analysis of geometric objects in the Catesian plane"
- __matplotlib__: creating graphics