"""

https://leetcode.com/problems/course-schedule-iii/

n courses
duration, last day
courses must be taken continuously
cannot take 2 courses simultaneously
start on day 1

how many courses can you take?

Idea:
- dp for each day, 10^4
- sort courses by end date, and duration?
- dp[day] = max num courses you could take that end on this day

- for each course, for each day, go thru and see
O(n^2)

- binary search for which day to take it? 

"""

def solve(courses):
    finalDays = [course[1] for course in courses]
    maxDays = max(finalDays)
    days = [0 for _ in range(maxDays + 1)]
    newDays = [0 for _ in range(maxDays + 1)]

    # now do dp
    for duration, final in courses:
        for day in range(duration, final + 1):
            if day - duration < 1: continue
            newDays[day] = max(days[day], 1 + days[day - duration])
        
        days = newDays
    
    return days[maxDays]

