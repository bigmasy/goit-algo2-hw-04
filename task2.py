from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        # Перевірка на порожній масив
        if not strings:
            return ""

        # Додаємо всі рядки в дерево
        for string in strings:
            self.put(string, 1)  # 1 — довільне значення для кожного слова
        
        # Шукаємо найдовший спільний префікс
        current_node = self.root
        prefix = ""

        while current_node and len(current_node.children) == 1:  # Якщо є тільки один наступний вузол
            for char, child in current_node.children.items():
                prefix += char
                current_node = child
        
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
