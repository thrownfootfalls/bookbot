def count_words(text):
    """The number of words in the text."""
    # Seems a bit redundant but I'll reserve judgement until I'm done
    return len(text.split())

def tally_characters(text):
    """How often each character appears, case-insensitive."""
    # using collections.Counter feels inappropriate for the exercise
    # so I'll do it the long way
    tally = {}
    for c in text.lower():
        tally[c] = tally.get(c, 0) + 1
    return tally

def sorted_letter_tallies(text):
    """A list of paired letters and totals, starting from the most common."""
    tally = tally_characters(text)
    #most to least common:
    letters = [c for c in tally if c.isalpha()] # only include actual letters
    letters = sorted(letters, key = lambda c: tally[c], reverse = True)
    return {letter: tally[letter] for letter in letters} # order will be preserved

def report(filepath):
    """Prints out summary statistics for the given text, according to specs."""
    print(f"--- Begin report of {filepath} ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the document")
    for letter, count in sorted_letter_tallies(file_contents).items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    report("books/frankenstein.txt")
#    with open("books/frankenstein.txt") as f:
#        file_contents = f.read()
#    print(count_words(file_contents))
#    print(tally_characters(file_contents))

main()
