class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> prevSum;

        for (int i = 0; int& n : nums) {
            int diff = target - n;
            if (prevSum.contains(diff)) {
                std::vector<int> res = {prevSum.at(diff), i};
                return res;
            }
            
            prevSum[n] = i;
            ++i;
        }

    }
};
