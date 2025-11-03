import CIS256_Minh_Do_EX4.guess_the_word as guess_the_word

def test_choose_word():
    words = ["python", "github", "pytest", "banana", "hangman"]
    chosen = guess_the_word.choose_word()
    assert chosen in words

def test_display_word_partial():
    word = "banana"
    guessed = {"a", "n"}
    result = guess_the_word.display_word(word, guessed)
    assert result == "_anana"

def test_display_word_empty():
    word = "pytest"
    guessed = set()
    result = guess_the_word.display_word(word, guessed)
    assert result == "______"