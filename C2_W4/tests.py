
def get_windows(words, C):
    i = C
    while i < len(words) - C:
        center_word = words[i]
        context_words = words[(i-C):i] + words[(i+1):(i+C+1)]
        yield context_words, center_word
        i += 1
        
for x,y in get_windows(
    ['i','am','happy','because','i','am','learning'], 2
    ):
    print(f"{x}\t{y}")