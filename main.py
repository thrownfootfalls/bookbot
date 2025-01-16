def count_words(text):
    """The number of words in the text."""
    # Seems a bit redundant but I'll reserve judgement until I'm done
    return len(text.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print(count_words(file_contents))

main()
