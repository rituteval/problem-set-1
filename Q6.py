user_input = input("Please enter a sentence:")
words = user_input.split(" ")
less_words = words[::2]
for w in less_words:
	print(w, end=' ')
