"""
判断  if elif else
"""
a = "1"
if a == "1":  # if 表示如果的意思 == 等于等于意思就是是否值相同
    print('a确实等于字符串"1"')

b = 1
if b == "1":
    print('b不等于字符串"1"')
elif b == 1:
    print("b确实等于整型1")
else:
    print("b不满足上面的判断条件")
