"""

https://leetcode.com/problems/task-scheduler/

- task str arr, chars, could be duplicate, each 1 task
- n - cooldown time between same tasks

Idea:
- optimal soln: cycle thru, do task with largest count first and keep cooldown array, (task, n, cooldownDone)?
O(n) * O(log n)

Better: O(n)? Identify number of noops?
What is optimal solution here? 

"""

import heapq

def solve(tasks, n):

    tasksCount = {}
    for task in tasks:
        if task not in tasksCount:
            tasksCount[task] = 0
        tasksCount[task] += 1

    heap = []
    for task, count in tasksCount.items():
        heapq.heappush(heap, (-count, task)) # negative to make max heap
    
    cooldown = [] # (task, countleft, cooldownDone)
    time = 1

    while heap or cooldown:
        # add from cooldown to heap
        while cooldown and cooldown[0][2] == time:
            task, count, time = cooldown.pop(0)
            heapq.heappush(heap, (-count, task))
        
        if heap:
            count, task = heapq.heappop(heap)
            count = -count
            count -= 1

            if count > 0:
                cooldown.append((task, count, time + n + 1))        

        time += 1
    
    return time - 1



