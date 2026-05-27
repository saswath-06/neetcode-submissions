class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (const string& s : strs) {
            vector<int> count(26, 0);
            for (const char& c : s) {
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i = 1; i < 26; ++i) {
                key += "," + to_string(count[i]);
            }

            groups[key].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& val : groups) {
            res.push_back(val.second);
        }

        return res;
    }
};