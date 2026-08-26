class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        node = self
        for i in word:
            if i not in node.children:
                node.children[i] = WordDictionary()
            node = node.children[i]

        node.is_end = True
        
        

    def search(self, word: str) -> bool:
        

        def helper(index, node):

            if index == len(word):
                return node.is_end


            if word[index] == ".":
                for k, v in node.children.items():
                    if helper(index + 1, v):
                        return True
                    
                return False
            else:
                if word[index] not in node.children:
                    return False
                
                return helper(index + 1, node.children[word[index]])

        return helper(0, self)
                

            
