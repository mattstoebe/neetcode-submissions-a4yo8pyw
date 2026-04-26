class PrefixTree:

    def __init__(self):
        self.root = {}        

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if root.get(char) == None:
                root[char] = {}
                
            root = root[char]

        root["End"] = True

    def search(self, word: str) -> bool:
        root = self.root
        
        for char in word:
            if char in root:
                root = root[char]
            else:
                return False
        
        
        return root.get("End", False)
            
                

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        
        for char in prefix:
            if char in root:
                root = root[char]
            else:
                return False
        return True
                