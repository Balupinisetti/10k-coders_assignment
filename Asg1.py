#    *
#   * * 
#  * * * 
# * * * * 
#* * * * *


rows=int(input("enter the rows:"))
res=" "
for i in range(1,rows+1):
    res=" " * (rows-i)
    for j in range(1,i+1):
        res+="* "
    print(res)



# "abc" sequence
def vowel(text):
    count=0
    word='abc'
    for char in text:
        if char in word:
            count+=1
    return count
print(vowel("hsfakhbjgfcjggjdlaa"))





# printing chess board 
rows=5
res=" "
for i in range(1,rows+1):
    for j in range(1,rows+1):
        res=("X "+"O ") * 5
    print(res)  