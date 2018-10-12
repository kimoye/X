class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
#   难度：困难 leetcode 920
#   你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
#   每首歌至少播放一次。
#   一首歌只有在其他 K 首歌播放完之后才能再次播放。
#   返回可以满足要求的播放列表的数量。     
#   N < L
#   此处不适用reduce 直接构造连乘函数即可
    # 考虑边界条件：L=N 即想听的歌刚刚好等于歌单得数目
    # 此时，返回N得全排就好
    # K < N: K + 1 = N也是全排
    if L == N and  N == K + 1:
        res = 1
        for i in range(1,N+1):
            res = res * i
        return res
   
    # 首先将所有得歌全排，因为都得播放一次，即A（N/N）得res1
    # 然后剩下从已经播放过的N首里面全排后选出L-N首歌，得res2
    # 选出res2要在第K个位置之后的其中L-N个位置中，得res3
    # 返回res1*res2*res3
    res1 = res2 = 1
    for i in range(1,N+1):
        res1 = res1 * i
    for i in range(L-N,N+1):
        res2 = res2 * i
    for i in range

    return res1*res2