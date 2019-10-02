from nltk import word_tokenize, sent_tokenize
selection = int(input("1. Word Tokenizer\n2. Sentence Tokenizer\nSelect..?? "))

if(selection == 1):
    para = input("Enter a Sentence: ")
    print("Before Replacing:\n",para)
    result = word_tokenize(para)
    print("\nTokenize Words:\n"*result, sep=", ")
    

if(selection == 2):
    para = input("Enter a Sentence: ")
    print("Before Replacing:\n",para)
    result = sent_tokenize(para)
    print("\nTokenize Sentence:\n"*result, sep=", ")

