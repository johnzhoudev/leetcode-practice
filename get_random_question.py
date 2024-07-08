from random import choice

f = open("./random.txt", "r")
raw_lines = f.readlines()
lines = []
for line in raw_lines:
    if not line.startswith("#"):
        lines.append(line)
valid_lines = []
f.close()

for line in lines:
    if line[3] == " ":
        valid_lines.append(line)

line = choice(valid_lines)
print(line)

to_remove = input("Mark as done? y or n: ") == "y"
if to_remove:
    f = open("./random.txt", "w")
    for i in range(len(lines)):
        if lines[i] == line:
            lines[i] = line[:3] + "x" + line[4:]
    
    f.writelines(lines)
    f.close()
    print("Marked as done")



