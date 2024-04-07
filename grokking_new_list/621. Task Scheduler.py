"""

tasks a to z, cooling time n
each cycle completes one task
identical tasks must be separated by the cooling time
return min number of cycles to complete all

Greedy?

Make dict of all tasks and count
do in order of most tasks, use heap
if no task can be completed, add thingy

O(n) * O(26)

Tactic: Easiest way is greedy, take most frequent first and rest


Algorithmic way, non-trivial imo

case 1: 1 single most frequent char
- then arrange with potential idles
- will always be able to fill one slot each in each section with the remaining, so just subtract.
    - if you have less than the number of slots, it works.
    - if you have more, will always be able to add to the slots without getting rid of idles. 
    - and since all min, will never have a situation where you're restricted by the cooldown.

- If multiple of same frequency, just gets rid of slots

"""

# The mathy way
def solve(tasks, n):
    # first get number of most frequent chars
    tasksCount = defaultdict(lambda: 0)
    maxNumTaskOccurrences = 0
    for task in tasks:
        tasksCount[task] += 1
        maxNumTaskOccurrences = max(maxNumTaskOccurrences, tasksCount[task])
    
    # Now count number of maxes
    numMaxTasks = 0
    for task, count in tasksCount.items():
        if count == maxNumTaskOccurrences:
            numMaxTasks += 1
    

    # Now do math
    numTasks = len(tasks)
    numSlots = (maxNumTaskOccurrences - 1) * (n - (numMaxTasks - 1))
    # how many can fill
    numIdles = max(0, numSlots - (numTasks - (numMaxTasks * maxNumTaskOccurrences)))
    return numTasks + numIdles


def solve(tasks, n):
    tasksCount = defaultdict(lambda: 0)
    for task in tasks:
        tasksCount[task] += 1
    
    numCycles = 0
    numBreaks = 0 # only add breaks one new wave
    while len(tasksCount) != 0:
        numCycles += numBreaks
        # run all tasks
        numTasksRunning = 0
        toRemove = []
        for task in tasksCount:
            # run the task
            tasksCount[task] -= 1
            numCycles += 1
            numTasksRunning += 1

            if tasksCount[task] == 0:
                toRemove.append(task)

        # Remove completed tasks
        for task in toRemove:
            tasksCount.pop(task, None)

        # figure out how many breaks to take
        numBreaks = max(n - (numTasksRunning - 1), 0)
    
    return numCycles





from queue import PriorityQueue

from collections import defaultdict, deque

def solve(tasks, n):
    tasksCount = defaultdict(lambda: 0)
    for task in tasks:
        tasksCount[task] += 1
    
    # now make priority queues
    taskPool = PriorityQueue()
    for task in tasksCount:
        taskPool.put((-tasksCount[task], task)) # want max heap
    
    waitPool = deque() # Objects are (cycle free, (taskcount, task))

    # now simulate
    numCycles = 0

    while taskPool.qsize() != 0 or len(waitPool) != 0:
        numCycles += 1

        # free all waiting cycles that should be freed on this cycle
        while len(waitPool) != 0 and waitPool[0][0] == numCycles:
            _, task = waitPool.popleft()
            taskPool.put(task)

        if taskPool.qsize() != 0:
            # get from task pool
            negCount, task = taskPool.get()
            negCount += 1 # execute task

            if negCount < 0: # still needs to be redone
                waitPool.append((numCycles + n + 1, (negCount, task)))
    
    return numCycles


        

    


