"""

single thread cpu
0, n-1 id

call stack for functions, top is current execution
log id, start or end, and timestamp
"{function_id}:{"start" | "end"}:{timestamp}"

- greedy? just count for each interval the execution time between events. use an arr


"""

class Log:
    def __init__(self, s):
        s = s.split(":")
        self.id = int(s[0])
        self.timestamp = int(s[2])
        self.action = s[1]

        # To simplify, all end times will be adjusted +1 so it's like it ends at the start of the next second
        if self.action == "end":
            self.timestamp += 1

def solve(n, logs):
    exec_times = [0 for _ in range(n)]

    logs = [Log(l) for l in logs]

    callstack = []
    previous_time = 0

    for log in logs:

        # First, add time
        # Only add time if nothing on callstack
        if len(callstack) != 0:
            curr_id = callstack[-1]
            exec_times[curr_id] += log.timestamp - previous_time
        
        # now update callstack
        if log.action == "start":
            callstack.append(log.id)
        else:
            callstack.pop()

        # Reset data
        previous_time = log.timestamp
    
    return exec_times



