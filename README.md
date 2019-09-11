# Broken Binsearch problem

Will you solve it the most efficient way?

## The problem

You are given an array of integers from 0 to 99 included:

```
[0, 1, 2, 3, ..., 99]
```

A random number from the array is picked. Your task is to guess this number by making requests of type `is the number GREATER than [N]?`. You know, a common binary search problem.

In this particular problem, when you make a request, you get **false** answer in 1 of 4 cases. For example, number 42 was picked and you are asking `is this number greater than 50?`. Then an imaginary die is rolled to determine whether to tell you truth of lie. With 1/4 chance you will get `False` (lie), otherwise you get `True`.

Also there is another type of request: `Is the number [N]?`. In this case the answer is always **truth**. Thus, is the number picked is [N], you win, otherwise you continue playing.

### Summary

The game randomly picks a number from 0 to 99 included.

You can make 2 types of requests:
+ `Is the number GREATER than [N]?` (the game lies in 1 of 4 cases)
+ `Is the number [N]?` (you win if the number *is* [N])

Your task is to minimize number of requests.

## API

```
Some kind of documentation is coming soon...
You can find example code in Untitled.ipynb
```
