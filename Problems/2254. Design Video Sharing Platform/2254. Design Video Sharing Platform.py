# 03-02-2024 Leetcode 2254. Design Video Sharing Platform
# https://leetcode.com/problems/design-video-sharing-platform/
# Time: 15 Challenge: 2/10

# How is this a hard?

class Video:
    def __init__(self, file, id):
        # self.name
        self.file = file
        self.id = id
        self.lastMin = len(file) #Inclusive
        self.views = 0
        self.likes = 0
        self.dislikes = 0

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def view(self):
        self.views += 1


class VideoSharingPlatform:
    def __init__(self):
        self.videos = collections.defaultdict(Video)
        self.id_heap = []

    def getID(self) -> int:
        if self.id_heap == []:
            return len(self.videos)
        else:
            return heapq.heappop(self.id_heap)

    def upload(self, video: str) -> int:
        id = self.getID()
        self.videos[id] = Video(video, id)
        return id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            if videoId < len(self.videos) - 1:
                heapq.heappush(self.id_heap, videoId)
            del self.videos[videoId]

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.videos:
            # Do I need to do bounds checking on start and stop times?
            # It says the start minute is LESS than the length of the video,
            # but speficifies nothing for end. Lets do double checking
            self.videos[videoId].view()
            endMinute = min(endMinute + 1, self.videos[videoId].lastMin)
            return self.videos[videoId].file[startMinute:endMinute]
        else:
            return "-1"        

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].like()
        
    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId].dislike()
        
    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.videos:
            return [self.videos[videoId].likes, self.videos[videoId].dislikes] 
        else:
            return [-1]

    def getViews(self, videoId: int) -> int:
        if videoId in self.videos:
            return self.videos[videoId].views
        else:
            return -1


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)