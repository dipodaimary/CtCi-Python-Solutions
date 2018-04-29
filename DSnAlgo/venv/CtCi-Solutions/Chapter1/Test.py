from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
col_count = Counter()
for c in z:
    col_count[c]+=1
print(col_count)
