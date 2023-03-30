"""

https://leetcode.com/problems/design-twitter/

Idea
- hash user to queue of 10 tweets
- on getNewsFeed, O(followed) put all in heap and get top 10 - O(followed) * O(10)
- Hash user to list of followed?

postTweet - add to queue, and for all followers, update - O(followers), since all heaps are O(log 10) - O(1)
getNewsFeed - heap, O(followed) - can keep this built, then O(10), but then unfollow becomes O(followed) to rebulid. Better.
follow - add to hash set, + O(10) heap
unfollow - remove from list of followed, O(1) with hash set. But if keep heap of follows, O(followed) to reconstruct

- followers list - keep list of people following x

Idea2:
PostTweet - O(1)
getNewsFeed - O(followers), do heap to get
follow / unfollow - O(1) to remove from set

Tactic: OOP a good idea. Can keep simple and build getNewsFeed each call, or fancier but more complex build news feed on follow

"""

import heapq
from collections import deque

class User:
    def __init__(self, userId):
        self.following = set()
        self.tweets = deque()
        self.following.add(userId)

    def addTweet(self, tweetId):
        self.tweets.appendleft(tweetId)
        if len(self.tweets) > 10:
            self.tweets.pop()


class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
    
    def getOrCreateUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getOrCreateUser(userId)
        user.addTweet((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> list[int]:
        user = self.getOrCreateUser(userId)
        feed = [] # minheap, get rid of smallest time
        for followerId in user.following:
            follower = self.getOrCreateUser(followerId)

            for time, tweet in follower.tweets:
                heapq.heappush(feed, (time, tweet))
                if len(feed) > 10:
                    heapq.heappop(feed)

        result = []
        while feed:
            result.append(heapq.heappop(feed)[1])
        result.reverse()
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        user = self.getOrCreateUser(followerId)
        user.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.getOrCreateUser(followerId)
        if followeeId in user.following:
            user.following.remove(followeeId)

class Twitter:

    def __init__(self):
        self.userToFollowers = {} # people who follow user
        self.userToFeed = {}
        self.timestamp = 0
        self.userToTweets = {}
        self.userToFollowees = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkUserExists(userId)

        # add tweet
        tweets = self.userToTweets[userId]
        tweets.appendleft((self.timestamp, tweetId))
        if len(tweets) > 10:
            tweets.pop()

        # for all followers including itself, add to feed
        for followerId in self.userToFollowers[userId]:
            feed = self.userToFeed[followerId]
            heapq.heappush(feed, (self.timestamp, tweetId)) # minheap to remove oldest timestamps, 
            if len(feed) > 10:
                heapq.heappop(feed)
        
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        self.checkUserExists(userId)

        output = self.userToFeed[userId].copy()
        output.sort(reverse=True, key=lambda x : x[0])
        return [x[1] for x in output]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.checkUserExists(followerId)
        self.checkUserExists(followeeId)
        
        # add follower
        if followerId not in self.userToFollowers[followeeId]:
            self.userToFollowers[followeeId].add(followerId)
            self.userToFollowees[followerId].add(followeeId)
            self.addToFeed(followerId, followeeId)

    def addToFeed(self, followerId, followeeId):
        # add tweets to followeeId
        followerFeed = self.userToFeed[followerId]
        for tweet in self.userToTweets[followeeId]:
            heapq.heappush(followerFeed, tweet)
            if len(followerFeed) > 10:
                heapq.heappop(followerFeed)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.checkUserExists(followerId)
        self.checkUserExists(followeeId)

        # remove follower
        if followerId in self.userToFollowers[followeeId]:
            self.userToFollowers[followeeId].remove(followerId)
            self.userToFollowees[followerId].remove(followeeId)

        # regenerate follower feed
        self.userToFeed[followerId] = []
        for newFollowee in self.userToFollowees[followerId]:
            self.addToFeed(followerId, newFollowee)

    def checkUserExists(self, userId):
        if userId not in self.userToFollowers:
            self.userToFollowers[userId] = set()
            self.userToFollowers[userId].add(userId)
            self.userToFeed[userId] = [] # heap
            self.userToTweets[userId] = deque()
            self.userToFollowees[userId] = set()
            self.userToFollowees[userId].add(userId) # people who this user follow

t = Twitter()
t.postTweet(2, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
print(t.getNewsFeed(1))
t.follow(1, 2)
print(t.getNewsFeed(1))