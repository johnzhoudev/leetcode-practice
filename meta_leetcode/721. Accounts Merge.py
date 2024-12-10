"""

721. Accounts Merge


name, then emails
merge accounts with common email

return name, then emails in sorted order
People could share names - use id's?

Graph problem

build graph
- id to name? or just use id as index in arr
- make graph of id for each entry - associate an id with each account
- for each account emails, add map of email to id's
- then for each id, do a dfs and combine. 

Way 2: emails are the nodes

Way 3: union find?? How to get emails
- emails are nodes
- merge together and keep ownership[email] => key
- then on final pass, go thru all emails and add to parent hash table and emit
- sort and emit

Tactic:
1: dfs, map email to account id. 2: dfs, emails are nodes. 3: Union find, accounts are nodes, make email to id map and 2nd pass add all emails to parent hash. Then sort and output

"""

from collections import defaultdict

def solve(accounts):

    rank = [0 for _ in range(len(accounts))]
    parent = [i for i in range(len(accounts))]

    emailToAccountId = {}
    
    # we want to union all the accounts

    def find(id):
        stack = []
        while parent[id] != id:
            stack.append(id)
            id = parent[id]
        
        # compress
        for i in stack:
            parent[i] = id
        
        return id
    
    # returns parent
    def union(id1, id2):
        p1 = find(id1)
        p2 = find(id2)

        if p1 == p2:
            return p1

        if rank[p1] > rank[p2]:
            # union into p1
            parent[p2] = p1
            rank[p1] += 1
            return p1
        else:
            parent[p1] = p2
            rank[p2] += 1
            return p2
        
        
    # union all the accounts
    for idx, account in enumerate(accounts):
        for email in account[1:]:
            if email not in emailToAccountId:
                emailToAccountId[email] = idx
            
            par = union(idx, emailToAccountId[email]) # unions account idx's
            emailToAccountId[email] = par
    
    # at this point, emailToAccountId populated with all emails to accounts. So output
    emailsMap = defaultdict(list)
    for email in emailToAccountId:
        par = find(emailToAccountId[email])
        emailsMap[par].append(email)
    
    # now sort and output
    output = []
    for id in emailsMap:
        emails = sorted(emailsMap[id])
        output.append([accounts[id][0]] + emails)
    
    return output








def solve(accounts):
    # make adj list of emails
    adj = defaultdict(set)

    def addEdge(email1, email2):
        adj[email1].add(email2)
        adj[email2].add(email1)
    
    # make adjacency list
    for account in accounts:
        baseEmail = account[1]
        for email in account[2:]:
            addEdge(baseEmail, email)

    # now do dfs on each
    visited = set()

    def dfs(email, emails):
        nonlocal visited
        if email in visited: return
        visited.add(email)
        emails.append(email)
        for nextEmail in adj[email]:
            dfs(nextEmail, emails)
    
    output = []
    for account in accounts:
        if account[1] in visited: continue

        name = account[0]
        emails = []
        dfs(account[1], emails)
        output.append([name] + sorted(emails))
    return output


def solve(accounts):
    # first, make map of email to accounts
    emailToAccountIds = defaultdict(list)

    for idx, account in enumerate(accounts):
        for email in account[1:]:
            emailToAccountIds[email].append(idx)
    
    # Now do dfs
    visited = set()
    def dfs(i, emails):
        nonlocal visited

        # already explored
        if i in visited: return

        visited.add(i)

        # Now add neighbour emails
        accountEmails = accounts[i][1:]
        for email in accountEmails:
            emails.add(email)

        # now explore neighbours
        for email in accountEmails:
            for nexti in emailToAccountIds[email]:
                dfs(nexti, emails)
    
    output = []
    for idx in range(len(accounts)):
        if idx not in visited:
            emails = set()
            dfs(idx, emails) # populates emails
            output.append([accounts[idx][0]] + sorted(emails))
    
    return output

        











