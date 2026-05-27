class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() == t.length()) {
            std::unordered_map<char, int> countS;
            std::unordered_map<char, int> countT;
            for (int i = 0; i < s.length(); ++i) {
                countS[s.at(i)]++;
                countT[t.at(i)]++;
            }

            if (countS == countT) {
                return true;
            }
        }
        return false;
    }
};
