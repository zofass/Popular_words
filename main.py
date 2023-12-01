def popular_words(text, words):
    word_list = text.lower().split()
    word_count = {word: 0 for word in words}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
