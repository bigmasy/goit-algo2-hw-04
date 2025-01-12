from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        # Перевірка на коректність введеного параметра
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("The pattern must be a non-empty string.")

        # Лічильник слів, що закінчуються на заданий суфікс
        count = 0
        
        # Використовуємо допоміжну функцію для рекурсивного пошуку
        def _count_suffix(node, suffix):
            if len(suffix) == 0:
                # Якщо суфікс порожній, рахувати всі кінцеві слова від поточного вузла
                if node.is_end_of_word:
                    count += 1
                for child in node.children.values():
                    _count_suffix(child, suffix)
                return
            
            # Шукаємо відповідний символ у словнику
            char = suffix[0]
            if char in node.children:
                _count_suffix(node.children[char], suffix[1:])
        
        # Починаємо з кореневого вузла дерева
        _count_suffix(self.root, pattern)
        
        return count

    def has_prefix(self, prefix: str) -> bool:
        # Перевірка на коректність введеного параметра
        if not isinstance(prefix, str) or not prefix:
            raise ValueError("The prefix must be a non-empty string.")

        # Перевіряємо, чи є хоча б одне слово з заданим префіксом
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        # Якщо ми дійшли до кінця префікса, повертаємо True
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
