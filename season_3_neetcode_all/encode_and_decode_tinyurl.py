"""

https://leetcode.com/problems/encode-and-decode-tinyurl/

Tactic: str to and from dictionary with counter

"""

class Codec:

    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.counter = 0
        self.base = "www.asdf.com/"

    def encode(self, longUrl: str) -> str:
        # add to dicts
        newUrl = self.base + str(self.counter)
        self.counter += 1
        self.longToShort[longUrl] = newUrl
        self.shortToLong[newUrl] = longUrl
        return newUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong[shortUrl]


