from ast import Continue


name = input("Enter file:")

handle = open(name)

counts = dict()

for email in handle:
    email = email.strip()
    
   # print(words)
    if not email.startswith("From "):
        continue
  
    
    words = email.split(" ")
    
    pair = words[1:2]   
 
    for p in pair:
        if  p in counts:
            counts[p] +=1
        else:
            counts[p] = 1



#for p, count in sorted(counts.items()):
       # print(f'{p:<30}{count}')


#print('\nNumber of unique words: ', len(counts))
#print ("Mateo is happy")


bigcount = None
bigword = None

for p, count in counts.items():
     if bigcount is None or count > bigcount:
          bigword = p
          bigcount = count

print(bigword, bigcount)

