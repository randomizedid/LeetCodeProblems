// this code is used to complete problems from leetcode in C++.

#include <iostream>
#include <vector>

using namespace std;

// Max Consecutive Ones III (312 ms and 55.5 MB)
int maxConsecutiveOnes(vector <int> &nums, int k){
    int zero_count = 0;
    int left = 0;
    int curr = 0;
    int ans = 0;
    for (int right = 0; right <nums.size(); right++){
        if(nums[right] == 1){
            curr++;
        }
        else{
            zero_count++;
            curr++;
        }
        while(zero_count>k){
            if (nums[left] == 0){
                zero_count--;
            }
            curr--;
            left++;
        }
        ans = max(ans, curr);
        if (nums.size()-left < ans){
            return ans;
        }
    }

    return ans;
}

// Number of Zero Filled Subarrays (328 ms and 107.4 MB)
int numberOfZeroFilledSubarrays(vector <int> nums){
    int left = 0;
    int curr = 0;
    int ans = 0;
    for (int i = 0; i<nums.size(); i++){
        if (nums[i] == 0){
            curr++;
            ans+=curr;
        }
        else{
            curr = 0;
            while(left<i){
                left++;
            }
        }

    }

    return ans;
}

int main(){

    vector <int> nums = {1,3,0,0,2,0,0,4};
    vector <int> nums2 = {0,0,0,2,0,0};
    vector <int> nums3 = {2,10,2019};
    int k = 2;
    int k2 = 3;
    int k3 = 4;
    cout << numberOfZeroFilledSubarrays(nums) << endl;
    cout << numberOfZeroFilledSubarrays(nums2) << endl;
    cout << numberOfZeroFilledSubarrays(nums3) << endl;
}