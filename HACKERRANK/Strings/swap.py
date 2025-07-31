def swap_case(s):
    # swap_case_string=s.swapcase()
    swap_case_string=''
    for i in range(len(s)):
      if s[i].islower():
        swap_case_string+=s[i].upper()
      elif s[i].isupper():
        swap_case_string+=s[i].lower()
      else:
        swap_case_string+=s[i]
    return swap_case_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# def reverse_words_order_and_swap_cases(sentence):
#     orignal_sentence=''
#     for i in range(len(sentence)):
#         if sentence[i].islower():
#             orignal_sentence+=sentence[i].upper()
#         elif sentence[i].isupper():
#             orignal_sentence+=sentence[i].lower()
#         else:
#             orignal_sentence+=sentence[i]
#     words=orignal_sentence.split()
#     reversed_sentence=' '.join(reversed(words))
#     return reversed_sentence

# def numCells(grid):
#     res=0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             value=grid[i][j]
#             flag=1
#             for ii in range(max(0,i-1),min(len(grid),i+2)):
#                 for jj in range(max(0,j-1),min(len(grid[0]),j+2)):
#                     if (ii,jj)!=(i,j) and value<=grid[ii][jj]:
#                         flag=0
#                         break
#                 if flag==0:
#                     break
#             else:
#                 res+=1
#     return res
