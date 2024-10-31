#include <stack>
#include <string>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> charStack;  # create a stack
        
        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') { # if it's open paranthesis push onto the stack
                charStack.push(ch);
            } else {
                if (charStack.empty()) return false; # return false if stack is empty (we have closed paranthesis and stack is empty, is an invalid case)

                char top = charStack.top();
                if ((ch == ')' && top == '(') ||   # if char and top of stack matches pop out
                    (ch == '}' && top == '{') ||
                    (ch == ']' && top == '[')) {
                    charStack.pop();
                }
                else {      # return false when char and top of stack mismatch
                    return false;
                }
            }
        }

        return charStack.empty(); # return true when the stack is empty, it means verified every single char in the stack
    }
};
