#   给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：
#   left 中的每个元素都小于或等于 right 中的每个元素。
#   left 和 right 都是非空的。
#   left 要尽可能小。
#   在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。
#   示例 1：

#   输出：3
#   解释：left = [5,0,3]，right = [8,6]
#   示例 2：
#
#   输入：[1,1,1,0,6,12]
#   输出：4
#   解释：left = [1,1,1,0]，right = [6,12]                                  

class solution(object):
   def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        #A为空
        if not A:
            return 0
        #A不是全部相同
        res = 1
        bigger1    = A[0]
        bigger2    = A[0]
        #
        for i in range(n-1):
            if A[i] <= bigger1:
                res = i + 1
                if bigger1 < bigger2:
                    bigger1 = bigger2
                bigger2 = A[0]
            elif A[i] > bigger2:
                bigger2 = A[i]
        return res