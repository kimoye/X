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
#   N =< L
        #经过学习，掌握了DP的核心思想之后，该题目也较容易找出状态转移方程为：
        #       f(n,l,k)=f(n-1,l-1,k)*n+f(n,l-1,k)*(n-k)
        #       接下来考虑边界条件和怎么用py实现这个转移方程即可

        #创建一个二维数组
        memo = [[0]*(L+1) for _ in range(N+1)]
        #状态方程
        for i in range(1,N+1):
            for j in range(i,L+1):
                if i == j or i == K+1:
                    memo[i][j] = math.factorial(i)
                else:
                    memo[i][j] = i*memo[i-1][j-1] + (i-K)*memo[i][j-1]
        
        return memo[-1][-1]%(10**9 + 7) 