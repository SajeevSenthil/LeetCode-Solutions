class Solution {
public:
    int romanToInt(string s) {
        int total = 0;
        for (int i = 0; i < s.size(); ++i) {
            int current_value = 0;
            int next_value = 0;  
            switch (s[i]) {   // Assign integer value based on the current Roman numeral character
                case 'I': current_value = 1; break;
                case 'V': current_value = 5; break;
                case 'X': current_value = 10; break;
                case 'L': current_value = 50; break;
                case 'C': current_value = 100; break;
                case 'D': current_value = 500; break;
                case 'M': current_value = 1000; break;
                default:
                    return 0; // Return 0 for invalid input
            }
            if (i + 1 < s.size()) {   // Get the value of the next numeral if there is one
                switch (s[i + 1]) {
                    case 'I': next_value = 1; break;
                    case 'V': next_value = 5; break;
                    case 'X': next_value = 10; break;
                    case 'L': next_value = 50; break;
                    case 'C': next_value = 100; break;
                    case 'D': next_value = 500; break;
                    case 'M': next_value = 1000; break;
                }
            } 
            if (current_value < next_value) {  // Apply subtraction rule if the current value is less than the next value
                total -= current_value;
            } else {
                total += current_value;
            }
        }
        return total;
    }
};
    
