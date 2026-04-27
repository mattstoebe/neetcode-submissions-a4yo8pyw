class WordDictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        cur = self.dictionary
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["End"] = True

    def search(self, word: str) -> bool:
        # For search we need two branches. One normall one, one recursive one. This gets
        # Managed in a dfs algorithm

        def dfs(dictionary, idx):
            # if we reach the end of the word, we need to check if we are at the end of a trie
         
            if idx == len(word):
                return dictionary.get("End", False)

            # now the next 3 cases are
            # the character is a . 
            # it is a letter in the next layer of the Trie (valid, iterate)
            # It is not and we return False

            curr_char = word[idx]
            print(curr_char)
            if curr_char == ".":
                for key, child in dictionary.items():
                    
                    if key == "End": 
                        continue
                    elif dfs(child, idx+1):
                            return True # if any of them come back true we return rue
                
                return False # if we reach here this means no treus and we return False
                # here we do branching recursion

            # here we can probably just do regular recursion. 
            elif curr_char in dictionary:
                
                if dfs(dictionary[curr_char], idx+1):
                    return True

            return False
        
        return dfs(self.dictionary, 0)
                    



