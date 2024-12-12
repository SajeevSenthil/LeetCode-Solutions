class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        for (int i = 0; i < k; i++) {
            int a = 0;
            for (int j = 1; j < gifts.size(); j++) {
                if (gifts[j] > gifts[a]) {
                    a = j;
                }
            }
            gifts[a] = floor(sqrt(gifts[a]));
        }
        long long sum = 0;
        for (int i =  0; i < gifts.size(); i++) {
            sum += gifts[i];
        }
        return sum;
    }
};
