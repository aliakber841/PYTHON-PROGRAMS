if __name__ == '__main__':
    s = input()
    alpha_num=False
    alpha=False
    digit=False
    lower=False
    upper=False
    for i in s:
      if i.isalnum():
        alpha_num=True
      if i.isalpha():
        alpha=True
      if i.isdigit():
        digit=True
      if i.islower():
       lower=True
      if i.isupper():
        upper=True
print(alpha_num)
print(alpha)
print(digit)
print(lower)
print(upper)