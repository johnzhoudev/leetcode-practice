"""

636. Exclusive Time of Functions

id 0 to n-1

callstack

"{function_id}:{"start" | "end"}:{timestamp}"

return exclsuive time for each function in array

The logs are sorted

Idea:

- maintain callstack
- every log - starting a new one, end time of previous one
- stop one, end time of top and start time of previous one

O(n)
O(n) space

Better idea, just take every snippet between events and add?

Tactic:
Either store start time and interrutped time on stack and update (intuitive), or add each interval and track lastTime. Careful with times / lasttime on start / end, diff.
"""

def solve(n, logs):
    stack = [] # id
    exectimes = [0 for _ in range(n)]
    lastTime = -1

    for log in logs:
        id, op, time = log.split(":")
        id, time = int(id), int(time)

        if op == "start":
            # potentialyl add previous runtime
            if lastTime != -1 and stack:
                exectimes[stack[-1]] += time - lastTime
            stack.append(id)
            lastTime = time
        else: # end
            exectimes[id] += time - lastTime + 1
            stack.pop()
            lastTime = time + 1 # since current slice taken by current task
        
    
    return exectimes





def solve(n, logs):
    stack = [] # push (id, start time, interrupted time)
    exectimes = [0 for _ in range(n)]

    for log in logs:
        log = log.split(":")
        id = int(log[0])
        type = log[1]
        time = int(log[2])

        # start type, push onto stack and end previous one
        if type[0] == "s":
            stack.append((id, time, 0))
        else: # a task ended
            # add runtime of ended task
            _, starttime, interruptedTime = stack.pop()
            exectimes[id] += time - starttime - interruptedTime + 1 # task exclusive runtime
            # now add interrupted time to task below

            if stack:
                id2, t2, i2 = stack.pop()
                stack.append((id2, t2, i2 + (time - starttime + 1))) # interrupted time
    
    return exectimes







