class Solution:
    def rotate(self, nums, k):
        # 1.运行颠倒列表法
        # if len(nums)<2:
        #     return
        # nums.reverse()
        # k=k%len(nums)
        # while k>0:
        #     temp=nums.pop(0)
        #     nums.append(temp)
        #     k-=1
        # nums.reverse()
        # return 

        #2.运行逐个移动元素法 TLE
        # if len(nums)<2:
        #     return
        # k = k%len(nums)
        # while k>0:
        #     temp=nums[-1]
        #     nums[1:] = nums[:-1]
        #     nums[0]=temp
        #     k-=1
        # return

        #3.运行整体移动元素块法
        if len(nums)<2:
            return
        k = k % len(nums)
        temp=nums[len(nums)-k:]
        nums[k:]=nums[:len(nums)-k]
        nums[:k]=temp
        return
