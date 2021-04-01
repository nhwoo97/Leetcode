def merge(nums1, m, nums2, n):
#use [::] to nums1 at m 
#use same thing for nums 2
#append nums2 to nums1
#sort

  nums1 = nums1[0 : m : ]

  for num in range(n):
    nums1.append(nums2[num])
  nums1.sort()