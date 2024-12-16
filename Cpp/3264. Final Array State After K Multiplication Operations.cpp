class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        for(int i = 0; i < k; i++){ 
        int temp = nums[0];
        int a = 0;
            for(int j = 0; j < nums.size(); j++){
                if(temp > nums[j]){
                    temp = nums[j];
                    a = j;
            }
        }
        nums[a] = nums[a] * multiplier;
    }
    return nums;
    }
};
