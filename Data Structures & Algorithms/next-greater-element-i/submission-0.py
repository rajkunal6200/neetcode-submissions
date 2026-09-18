class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mp={}
        for x in nums2:
            while stack and stack[-1]<x:
                mp[stack.pop()]=x
            stack.append(x)
        return [mp.get(x,-1) for x in nums1]    

