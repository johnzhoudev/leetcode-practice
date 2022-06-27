runtimeInput = input("Paste Runtime Text: ")
memoryInput = input("Paste Memory Text: ")

runtimeWords = runtimeInput.split()
runtime = str(runtimeWords[1]) + "ms"
runtimePercent = str(runtimeWords[5])

memWords = memoryInput.split()
mem = str(memWords[2]) + "MB"
memPercent = str(memWords[6])

prefix = "Python3 online submissions for "
fileNameStart = runtimeInput.find(prefix) + len(prefix)
fileName = runtimeInput[fileNameStart:].strip(".").lower().replace(" ", "_")
fileName += ".py"

if (not mem or not memPercent or not runtime or not runtimePercent):
	print("Error: Bad Parsing.")
	exit()

with open("season_1/" + fileName, "r+") as f:
	content = f.read()
	f.seek(0, 0)
	f.write("# Results:\n# Runtime: " + runtime + " " + runtimePercent + "\n")
	f.write("# Memory Usage: " + mem + " " + memPercent + "\n\n")
	f.write(content)
	f.close()
