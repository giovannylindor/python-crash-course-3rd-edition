fav_lang = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, lang in fav_lang.items():
    print(f"\n{name.title()}'s fav lang: ")
    for language in lang:
        print(f"\t{language.title()}")