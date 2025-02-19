def get_user_input():
    """Prompt the user to enter a sentence or paragraph."""
    text = input("Enter a sentence or paragraph: ")
    return text

def count_words(text):
    """Count the number of words in the input text."""
    words = text.split()
    return len(words)

def display_word_count(word_count):
    """Print the word count to the console."""
    print(f"Word count: {word_count}")

def main():
    """Main function to orchestrate the word counting process."""
    text = get_user_input()
    if not text.strip():
        print("Error: Input cannot be empty.")
    else:
        word_count = count_words(text)
        display_word_count(word_count)

if __name__ == "__main__":
    main()
