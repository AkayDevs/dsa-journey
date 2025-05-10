/**
 * Problem: 1. Two Sum
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/two-sum/
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 
 * Description:
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 */

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Using a hash map to store values and their indices
        unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            // Check if the complement (target - current number) exists in the map
            int complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            
            // If not found, store the current number and its index
            map[nums[i]] = i;
        }
        
        // No solution found (problem guarantees a solution exists)
        return {};
    }
};

/**
 * Alternative Approach: Brute Force
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * 
 * vector<int> twoSum(vector<int>& nums, int target) {
 *     for (int i = 0; i < nums.size(); i++) {
 *         for (int j = i + 1; j < nums.size(); j++) {
 *             if (nums[i] + nums[j] == target) {
 *                 return {i, j};
 *             }
 *         }
 *     }
 *     return {};
 * }
 */ 