def permutations(s, ans):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
         a = s[i]
         left = s[:i]
         right = s[i+1 :]
         rest = left + right
         permutations(rest, ans + s[i])
word = str(input())
permutations(word, '')