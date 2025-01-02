class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:     
        def checkVowel(strings):
            count = 0
            vowels = ['a','e','i','o','u']
            for string in strings:
                if len(string) == 1:
                    if string in vowels:
                        count = count + 1
                elif len(string) >= 2:
                    FC = string[0]
                    LC = string[-1]
                    if FC in vowels and LC in vowels:
                        count = count + 1
            return count

        results = []
        for query in queries:
            start, end = query 
            sub_words = words[start:end + 1] 
            results.append(checkVowel(sub_words))  

        return results

