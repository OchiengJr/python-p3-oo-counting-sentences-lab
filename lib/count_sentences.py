class MyString:
    def __init__(self, value=''):
        self._value = str(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise TypeError("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        """Check if the string ends with a period."""
        return self._value.endswith('.')

    def is_question(self):
        """Check if the string ends with a question mark."""
        return self._value.endswith('?')

    def is_exclamation(self):
        """Check if the string ends with an exclamation mark."""
        return self._value.endswith('!')

    def count_sentences(self):
        """Count the number of sentences in the string."""
        sentences = filter(None, map(str.strip, self._value.split('.?!')))
        return len(list(sentences))

if __name__ == "__main__":
    # Example usage:
    string = MyString("Hello World.")
    print(string.is_sentence())  # Output: True
    print(string.is_question())  # Output: False
    print(string.is_exclamation())  # Output: False
    print(string.count_sentences())  # Output: 1
