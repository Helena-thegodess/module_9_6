def all_variants(text):
    for variant in range(len(text)):
        for letter in range(len(text) - variant):
            yield text[letter:letter + variant + 1]
a = all_variants("abc")
for i in a:
    print(i)
