word='this is my activity'
count=0
for w in word:
    if len(w) == 2:
        count += 1
        print('the number of words that have 2 letters:', count)
