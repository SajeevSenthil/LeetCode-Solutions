class Solution(object):
    def romanToInt(self, s):
        s = s.upper()  # convert the string into upper case
        total = 0 # set total = 0 and prev_ value = 0
        prev_value = 0
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in reversed(s): # revere and loop through the string
            if char in roman_values:
                current_value = roman_values[char] #  for every iteration, assume char in s is equal to current value
                if current_value < prev_value: # this is for handling cases like iv,ix,iix etc., if prev_value < current_value, sub current_value from total
                    total -= current_value
                else: # thisis for normal cases
                    total += current_value
                    prev_value = current_value
            else: # ensures every char is added
                return 0
                break
        return total
        
