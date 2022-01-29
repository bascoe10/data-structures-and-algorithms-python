class DictionaryBasedTrie:
    def __init__(self) -> None:
        self.__container = {'$$':0}

    
    def addWord(self, word: str) -> None:
        if word is None:
            return

        if len(word) == 0:
            self.__container['$$'] += 1
            return
        
        if word[0] not in self.__container:
            self.__container[word[0]] = DictionaryBasedTrie()
        self.__container[word[0]].addWord(word[1:])


    def searchWord(self, word) -> bool:
        if word is None:
            return False

        if len(word) == 0:
            return self.__container['$$'] > 0
        
        if word[0] not in self.__container:
            return False
            
        return self.__container[word[0]].searchWord(word[1:])

    def deleteWord(self, word) -> None:
        if word is None:
            return False

        if len(word) > 0:
            if word[0] in self.__container:
                self.__container[word[0]].deleteWord(word[1:])
        else:
            self.__container['$$'] -= 1 if self.__container['$$'] > 0 else 0
        
    

def main():
    trie = DictionaryBasedTrie()
    trie.addWord("bad")
    trie.addWord("dad")
    trie.addWord("dad")
    trie.addWord("magic")

    print(trie.searchWord("magic"))
    trie.deleteWord("magic")
    print(trie.searchWord("magic"))
    print(trie.searchWord("dad"))
    trie.deleteWord("dad")
    print(trie.searchWord("dad"))
    trie.deleteWord("dad")
    print(trie.searchWord("dad"))
    print(trie.searchWord("blah"))



if __name__ == '__main__':
    main()


        

        

