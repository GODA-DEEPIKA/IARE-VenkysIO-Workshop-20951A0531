import threading
def reverse_string(string):
    return string[::-1]
def reverse_paragraph(paragraph):
    words = paragraph.split()
    results = []
    threads = [threading.Thread(target=lambda result, word: result.append(reverse_string(word)), args=(results, word))
               for word in words]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return ' '.join(results)
paragraph = input("enter a paragraph")
reversed_paragraph = reverse_paragraph(paragraph)
print(reversed_paragraph)
