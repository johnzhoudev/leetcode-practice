"""

https://leetcode.com/problems/task-scheduler/

- task str arr, chars, could be duplicate, each 1 task
- n - cooldown time between same tasks

Idea:
- optimal soln: cycle thru, do task with largest count first and keep cooldown array, (task, n, cooldownDone)?
O(n) * O(log 26)

Better: O(n)? Identify number of noops? okay, technically our original impl is O(n) * O(log 26)
What is optimal solution here? 


Explaining Formulaic Solution:
- Calculate number of noops
- Imagine you take the most frequent letter and separate it out by n.
- You will notice that of the remaining tasks, you can only put one task in each "section"
- furthermore there are n-1 sections so you can place them in all of them
    - though, if you have many that have max count, place them one after another 
- so basically num open slots = slots - the tasks with same count as max (place next to each other)
- Then all other tasks, there must exist a slot to put them in since you can always extend the region too. and you can never have a double restriction
- so the only way to get a noop is if you don't have enough tasks to fill them in, hence max with 0.

Tactic: Stick with simulation, easier. Greedy, heap of counts, add largest count and then add to cooldown queue.
"""

# Extremely non-intuitive
def solveFormula(tasks, n):
    tasksCount = {}
    numMaxTasks = 0
    maxTaskCount = 0
    for task in tasks:
        if task not in tasksCount:
            tasksCount[task] = 0
        tasksCount[task] += 1

        if tasksCount[task] > maxTaskCount:
            maxTaskCount = tasksCount[task]
            numMaxTasks = 1
        elif tasksCount[task] == maxTaskCount:
            numMaxTasks += 1
    
    openSlots = (maxTaskCount - 1) * (n - numMaxTasks + 1) # if negative, means more tasks than min open slots, so can add more
    totalTasks = sum(tasksCount.values())
    availableTasks = totalTasks - (numMaxTasks * maxTaskCount)
    return totalTasks + max(0, openSlots - availableTasks)

    


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



