class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def search(self, word: str):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word: str):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.children['*'] = None

    def collect_all_words(self, words: list, node=None, word: str = ""):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collect_all_words(words, child_node, word + key)
        return words

    def autocomplete(self, prefix: str):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collect_all_words([], current_node)

    def print_keys(self, node=None):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == "*":
                print(key)
            else:
                print(key)
                self.print_keys(child_node)

    def autocorrect(self, word: str):
        current_node = self.root
        word_found_so_far = ""
        for char in word:
            if current_node.children.get(char):
                word_found_so_far += char
                current_node = current_node.children.get(char)
            else:
                return word_found_so_far + self.collect_all_words([], current_node)[0]




if __name__ == "__main__":
    test_trie = Trie()
    test_trie.insert("help")
    words_to_insert = ["game", "gay", "god", "goo", "hell", "hello", "fisher", "fish", "frog", "fact", "fractal",
                       "factoid", "cigg", "change", "chief", "chug", "chode", "awesome", "awful", "abs", "abstract"]
    for word in words_to_insert:
        test_trie.insert(word)
    print(test_trie.collect_all_words([]))

    #test_trie.print_keys()
    #test_trie.autocorrect("gay")
    print(test_trie.autocorrect("chx"))