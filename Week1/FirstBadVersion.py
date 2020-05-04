# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):

        ll = 1 
        ul = n
        current = 0
        while ll <= ul:
            mid = int((ll+ul)/2)
            if isBadVersion(mid):
                current = mid
                ul = mid - 1
            else:
                    ll = mid + 1
        return current
                
            
        