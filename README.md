# combinatoricsEquation
An exercise in solving an equation with blank variables. Inspired by a Facebook post. 

### Background ###

A friend of mine recently posted this problem on Facebook:

Use 1-6 in any order to solve this equation. Each number can only be used once.

(__+__-__)×__÷__×__ = 50

Admittedly, I honestly had to look at this for a while. At first I thought I could totally figure this out in my head. I made some basic assumptions, such as everything before the division should be as large as possible, and the last number within the paranthesis should probably be as small as possible. I wasted too much time on this and I had to leave the house, leaving this unfinished. 

I figured that the best way to solve this problem would be programatically, but even that wasn't an easy. I thought naively to just make 6 nested for loops. They're only going from 1-6, how bad could it be? Well it turns out that's 6^6, which is 46656 iterations. I've heard people say that n^2 is inefficient, this is of order n^n. On top of that, this problem is actually a combinatorics one. It's 6 choose 6, no repetition and order matters. That's a permuation, and its equation is n!/(n-r)! with n = r = 6. Recalling that 0! = 1, this makes the pool of possible answers a mere 720 permutations. 

My goal with this exercise is to sort of see how I can get the solution to this particular problem as efficiently as possible. Once I hit that point, I can go on and maybe find a general solution to this type of problem. I'm not entirely sure what the implications of this kind of problem are. I'll try to research that too. 

###Contribution Guidlines
None. This is just a small exercise that I'm doing for myself. I put it on github because I work on many different machines, and maybe it's cool to someone else. If anyone sees this and wishes to add onto it, I'll gladly take a look at your own fork. 
