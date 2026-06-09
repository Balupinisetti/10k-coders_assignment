# rows=5
# for i in range(rows):
#     res=" "
#     for j in range(i+1):
#         res+="* "
#     print(res)


# *                          
# * * 
# * * * 
# * * * *              
# * * * * *

# * * * * 
# *     *
# *     *
# * * * *
# row=5
# for i in range(1,row+1):
#     res=" "
#     for j in range(1,row+1):
#         if i==1 or i==5 or j==1 or j==5:
#             res+="* "
#         else:
#             res+="  "
#     print(res)

rows=5
for i in range(1,rows+1):
    res=" "
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
            res+="* "
    print(res)
for i in range(rows-1,0,-1):
    res=""
    for sp in range(rows-i):
         res+=" "
    for j in range(i):
        res+="* "
    print(res)