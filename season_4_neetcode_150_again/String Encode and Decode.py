"""

encode to single string and back

- idea: put count + # at start of each word, and read those counts

"""

class Solution:

    def encode(self, strs) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s):
        output = []

        curr = 0
        try:
            while True:
                numChars = 0
                while s[curr] != '#':
                    numChars *= 10
                    numChars += int(s[curr])
                    curr += 1
                curr += 1 # skip #
                outs = ""
                for i in range(numChars):
                    outs += s[curr]
                    curr += 1
                output.append(outs)
        except:
            return output


