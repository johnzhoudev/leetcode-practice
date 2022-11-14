# Usage: Copy leetcode results text and paste. Make sure you name your file exactly as the problem is called.

print("Paste Result Text: ", end='')

input() # Runtime word
runtimeLine = input() # Runtime
input() # beats
runtimePercent = input()
input() # memory
memoryLine = input()
input() # beats
memoryPercent = input()

# runtimeWords = runtimeLine.split()
# runtime = str(runtimeWords[0]) + "ms"
# runtimePercent = str(runtimeWords[5])

runtime = runtimeLine.replace(" ", "")
# runtime Percent fine

mem = memoryLine.replace(" ", "")
memPercent = memoryPercent

# prefix = "Python3 online submissions for "
# fileNameStart = memoryInput.find(prefix) + len(prefix)
# fileName = memoryInput[fileNameStart:].strip(".").lower().replace(" ", "_")
# fileName += ".py"

fileName = input("File name from url: ")
fileName = fileName.split("/")[4]
fileName = fileName.replace("-", "_").lower()
fileName += ".py"

if (not mem or not memPercent or not runtime or not runtimePercent):
	print("Error: Bad Parsing.")
	exit()

with open("season_2_neetcode_150/" + fileName, "r+") as f:
	content = f.read()
	f.seek(0, 0)
	f.write("# Results:\n# Runtime: " + runtime + " " + runtimePercent + "\n")
	f.write("# Memory Usage: " + mem + " " + memPercent + "\n\n")
	f.write(content)
	f.close()
