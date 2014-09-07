import time
start = time.time()
print(len([w for w in open('words.txt', 'r').read().strip('"').split('","') if(sum([ord(l)-64 for l in w]) in [i * (i+1) / 2 for i in range(1, 20)])]))
print(time.time() - start)