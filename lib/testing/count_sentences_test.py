#!/usr/bin/env python3

from count_sentences import MyString
import io
import sys
import pytest

class TestMyString:
    """Test suite for the MyString class in count_sentences.py"""

    @pytest.fixture
    def empty_string(self):
        """Fixture to create an empty MyString instance."""
        return MyString()

    @pytest.fixture
    def simple_string(self):
        """Fixture to create a simple MyString instance."""
        return MyString("one. two. three?")

    @pytest.fixture
    def complex_string(self):
        """Fixture to create a complex MyString instance."""
        return MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

    def test_is_class(self, empty_string):
        """MyString is a class with the name 'MyString'."""
        assert isinstance(empty_string, MyString)

    def test_value_string(self, empty_string):
        """Setting value to a non-string raises a TypeError."""
        with pytest.raises(TypeError) as excinfo:
            empty_string.value = 123
        assert str(excinfo.value) == "The value must be a string."

    def test_is_sentence(self, simple_string):
        """is_sentence() returns True if value ends with a period and False otherwise."""
        assert simple_string.is_sentence() == True

    def test_is_question(self, simple_string):
        """is_question() returns True if value ends with a question mark and False otherwise."""
        assert simple_string.is_question() == False

    def test_is_exclamation(self, simple_string):
        """is_exclamation() returns True if value ends with an exclamation mark and False otherwise."""
        assert simple_string.is_exclamation() == False

    def test_count_sentences(self, simple_string, empty_string, complex_string):
        """count_sentences() returns the number of sentences in the value."""
        assert simple_string.count_sentences() == 3
        assert empty_string.count_sentences() == 0
        assert complex_string.count_sentences() == 4
