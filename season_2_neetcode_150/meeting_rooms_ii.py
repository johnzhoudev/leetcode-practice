"""

https://www.lintcode.com/problem/919/

- given array of meeting times
- max rooms needed?

Ideas:
- basically just need to find max number of rooms needed at a single point in time

- sort by start point
- invariant: in the queue, all meetings overlap with bottom

- just add things one by one and remove once can no longer add since doesn't overlap
- if 2nd thing doesn't overlap fully, doesn't matter since getting max.
- and if you have to add something else, that means that 2nd in line extends past end.
- when to decrease count? maybe only pop when not current anymore?


"""