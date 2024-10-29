class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> nums_1(2);
        for(int i =0; i < nums.size(); i++){
            for (int j = i+1; j < nums.size(); j++){
                if(target - nums[i] == nums[j]){
                    nums_1[0] = i;
                    nums_1[1] = j;
                }
            }
        }
        return nums_1;
    }
};
