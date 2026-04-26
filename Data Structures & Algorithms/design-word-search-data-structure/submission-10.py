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
        def dfs(node, pointer):
            if pointer == len(word):
                return node.get("End", False)

            char = word[pointer]

            if char == ".":
                for key, child in node.items():
                    if key == "End":
                        continue
                    if dfs(child, pointer + 1):
                        return True
                return False

            if char not in node:
                return False

            return dfs(node[char], pointer + 1)

        return dfs(self.dictionary, 0)