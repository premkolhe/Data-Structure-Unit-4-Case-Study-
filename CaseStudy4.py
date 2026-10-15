class HashTableDictionary:
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, word):
        """Convert a word into a bucket index."""
        return sum(ord(character) for character in word.lower()) % self.capacity

    def add_word(self, word, meaning):
        """Add a new word or update its meaning if it already exists."""
        word = word.strip()
        meaning = meaning.strip()

        if not word or not meaning:
            raise ValueError("Word and meaning cannot be empty.")

        index = self._hash(word)

        # Update the meaning if the word is already present.
        for entry in self.buckets[index]:
            if entry[0].lower() == word.lower():
                entry[1] = meaning
                print(f"Updated '{word}'.")
                return

        self.buckets[index].append([word, meaning])
        print(f"Added '{word}'.")

    def get_meaning(self, word):
        """Return a word's meaning, or None if the word is not found."""
        index = self._hash(word)

        for stored_word, meaning in self.buckets[index]:
            if stored_word.lower() == word.lower():
                return meaning

        return None

    def remove_word(self, word):
        """Remove a word from the dictionary."""
        index = self._hash(word)

        for position, entry in enumerate(self.buckets[index]):
            if entry[0].lower() == word.lower():
                del self.buckets[index][position]
                print(f"Removed '{word}'.")
                return True

        print(f"'{word}' was not found.")
        return False

    def display(self):
        """Display all words and meanings in the hash table."""
        print("\nDictionary contents:")
        found_word = False

        for bucket in self.buckets:
            for word, meaning in bucket:
                print(f"- {word}: {meaning}")
                found_word = True

        if not found_word:
            print("(The dictionary is empty.)")


def main():
    dictionary = HashTableDictionary(capacity=5)

    dictionary.add_word("listen", "To give attention to sound.")
    dictionary.add_word("silent", "Making little or no sound.")
    dictionary.add_word("python", "A popular programming language.")

    # With this simple hash function and capacity, "listen" and "silent"
    # collide, so they are stored in the same bucket.
    dictionary.display()

    search_word = "listen"
    meaning = dictionary.get_meaning(search_word)

    if meaning:
        print(f"\nMeaning of '{search_word}': {meaning}")
    else:
        print(f"\n'{search_word}' was not found.")

    dictionary.add_word("listen", "To pay attention to what someone says.")
    print(f"\nUpdated meaning of 'listen': {dictionary.get_meaning('listen')}")

    dictionary.remove_word("silent")
    dictionary.display()


if __name__ == "__main__":
    main()