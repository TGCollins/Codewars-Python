def reverse_words(text):
  words = text.split('')
  reversed_words = []
  for word in words:
    reversed_words.append(word[len(word)::-1]
  return ' '.join(reversed_words)                          
