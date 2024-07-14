## Two sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Solution Link:https://leetcode.com/problems/two-sum/description/

## Merge Intervals:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Solution: https://leetcode.com/problems/merge-intervals/submissions/1259991547/

![image](https://github.com/Simran-99/DSA/assets/68385902/a43e40c4-8205-465e-b113-4429c393ab38)


## ThreeSum:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


## 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


## 4 Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

## Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

## Reduce Array Size to half

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

### Approach to solve:
1. Create a hashmap where the elements of array are stored as key and values are initialized as 0.
2. Traverse through the array and increment the value of the element(key in the hashmap) by 1 in the hashmap
3. Sort the hashmap in descending order of the value count
4. Initialize n =len(arr) , count =0, size =n
5. Traverse through the array, increment the counter by 1 and reduce the size by the value of key in the map
6. Add a condition inside the loop for when the size<=n the loop breaks and the count is returned

Solution Link: https://leetcode.com/problems/reduce-array-size-to-the-half/description/

## Rotate image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

### Approach to Solve:

1.Initialization:

The left pointer is initialized to 0, representing the starting column.
The right pointer is initialized to len(matrix) - 1, representing the ending column.

2.Outer While Loop:

The loop continues until left is less than right.

3.Inner For Loop:

Iterates over the range from 0 to right - left (inclusive), effectively iterating over the layers of the matrix.

4.Element Swapping:

Four elements are rotated in each iteration:
The top row element (matrix[top][left + i]) is moved to the rightmost column.
The leftmost column element (matrix[bottom - i][left]) is moved to the top row.
The bottom row element (matrix[bottom][right - i]) is moved to the leftmost column.
The rightmost column element (matrix[top + i][right]) is moved to the bottom row.
This swapping effectively rotates the elements 90 degrees clockwise.

5.Updating Pointers:

After completing the swaps for the current layer, the left pointer is incremented, and the right pointer is decremented to move inward to the next layer.

6.Return:

The function does not explicitly return anything (None), but it modifies the input matrix in place.

Solution Link: https://leetcode.com/problems/rotate-image/

![image](https://github.com/Simran-99/DSA/assets/68385902/e8ae736f-1009-45eb-88cb-5f7bbfcad0c2)


## Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


### Approach:

1. Interate through digits list and append the elements to an emplty string
2. convert the string to int and add 1
3. Convert it back to a string and append to the list

Solution Link: https://leetcode.com/problems/plus-one/description/

![image](https://github.com/Simran-99/DSA/assets/68385902/099bf754-cce1-4e86-87fe-692ccd8099d4)

## Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

### Approach:

1. Interate through nums1 and add the numbers in the lst inside a hashmap
2. Iterate through nums2 and add the numbers in the lst inside another hashmap
3. Interate through the keys of hashmap1
4. Add a conditional statement inside the loop. If the key exists in hashmap2 . It would be added to the result list
5. return the result

Solution Link: https://leetcode.com/problems/intersection-of-two-arrays/description/

## Fruits in Basket

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

### Approach:

1. Create a defaultdict hashmap.
2. Set the total, res, and l (left pointer) as 0.
3. Iterate through fruits. For each category increment the value in hashmap and increment total as well.
4. Add a while loop inside the for loop to continue as long as the length of the hashmap is greater than 2.
5. Store value of the category on left most pointer l inside another variable f.
6. Decrement the hashmap value for category f and total. if the value of a key becomes 0. remove the key.
7. Increment l
8. End of while loop
9. res=max(res,total)
10. return total

Solution Link:https://leetcode.com/problems/fruit-into-baskets/

![image](https://github.com/user-attachments/assets/eb57d47c-f1ef-432e-9b00-d996b65599a4)

## Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

### Approach:

1. Set max_zeros as 0, l (left pointer) as 0 and max_w  as 0
2. Iterate through the entire list
3. Inside the loop if the value at index r (right pointer) is 0 then increment max_zeros
4. Add a while loop with the condition that the max_zeros is greater than k
5. If at left pointer l , the value is 0. Decrement the max_zeros and the loop will break
6. w=r-l+1
7. find maximum of w and max_w
8. return the max_w

Solution Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/

![image](https://github.com/user-attachments/assets/b130269d-57e5-4ead-b017-d7fb7eb01377)

## Container with Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

### Approach:

1. Assign the left pointer as 0, max_area =0, l (left pointer) as 0, r (right pointer) as len(nums)
2. while l<r
3. area=min(height[l],height[r])*(r-l)
4. max_area=max(area,max_area)
5. if height[l]<height[r] : left=left +1, else right = right -1
6. return max_area





