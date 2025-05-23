s1 = input("Enter the first phrase: ")
s2 = input("Enter the second phrase: ")
s1 = s1.casefold()
s2 = s2.casefold()
for i in s1:
    if i.isalpha():
        if s1.count(i)!=s2.count(i):
            print("Phrases are not Anagrams")
            break
else:
    print("Phrases are Anagrams")
