"""

71. Simplify Path

multiple slashes = single slash
. curr dir
.. parent dir

anything else is valid dir name

Path must start with single /
directories separated byt single slash

cannot end iwth slash unless root dir

no . or ..

Basically just parse the path

Idea:
- basically just turn all slashes into single slashes
- and also pop from stack or remove all dots.
- can just go thru and do it. maintain stack of pathnames
- if ever do illegal move, just stop and return /

O(n) time
O(n) space

Tactic:
If can use string.split('/') so easy. use stack for pathnames. Else parse manually.

"""

def solve(path):

    pathnames = []
    names = path.split('/')

    for name in names:
        if name == '.' or name == "":
            continue # do nothing
        elif name == "..":
            if pathnames: pathnames.pop()
        else:
            pathnames.append(name)
    
    return '/' + '/'.join(pathnames)

def solve(path):
    pathnames = []
    i = 0
    while i < len(path):
        try:
            assert(path[i] == '/')

            # first parse all slashes
            while i < len(path) and path[i] == '/':
                i += 1
            if i >= len(path):
                break

            # now parse all content until next slash
            name = ""
            while i < len(path) and path[i] != '/':
                name += path[i]
                i += 1
            # do not advance i at this point. already primed

            if name == ".":
                pass
            elif name == "..":
                pathnames.pop() # pop previous value
            else:
                pathnames.append(name)
        
        except:
            # if failed, just continue with path = []
            pathnames = []
    # print(pathnames)

    return '/' + '/'.join(pathnames)

print(solve("/a/../../b/../c//.//"))

