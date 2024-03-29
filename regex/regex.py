"""
正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，
凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
"""

"""
在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
    '00\d'可以匹配'007'，但无法匹配'00A'；
    '\d\d\d'可以匹配'010'；
    '\w\w\d'可以匹配'py3'；
.可以匹配任意字符，所以：
    'py.'可以匹配'pyc'、'pyo'、'py!'等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
来看一个复杂的例子：\d{3}\s+\d{3,8}。
我们来从左到右解读一下：
    \d{3}表示匹配3个数字，例如'010'；
    \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
    \d{3,8}表示3-8个数字，例如'1234567'。
综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
"""

"""
要做更精确地匹配，可以用[]表示范围，比如：
    [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
    [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
    [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
    [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
"""

import re
#  re_module:

s1 = 'ABC\\-001'  # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'


s2 = r'ABC\-001'  # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

r1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r1)
r2 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(r2)

def match(r):
    if r is None:
        print('fail')
    else:
        print('pass')

match(r1)
match(r2)

str1 = 'a b   c'
str2 = 'a, b,,  c'
str3 = 'a,b;; c  d'
print(str1.split(' '))
print(re.split(r'\s+', str1))
print(re.split(r'[\s,]+', str2))
print(re.split(r'[\s,;]+', str3))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.group())

#  由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
greedy1 = re.match(r'^(\d+)(0*)$','102300')
print((greedy1.group(1), greedy1.group(2)))
#  必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
greedy2 = re.match(r'^(\d+?)(0*)$', '102300')
print((greedy2.group(1), greedy2.group(2)))

#  如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
#  编译：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#  使用：
r = re_telephone.match('010-12345')
print((r.group(1), r.group(2)))


'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

    someone@gmail.com
    bill.gates@microsoft.com

'''

def is_valid_email(addr):
    re_email = re.compile(r'^(\w+\.?\w*)@(\w+).(\w+)$')
    if re_email.match(addr) is not None:
        return True

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


'''
版本二可以提取出带名字的Email地址：

    <Tom Paris> tom@voyager.org => Tom Paris
    bob@example.com => bob

'''

re_email_match = re.compile(r'^(<?)(\w+\.?\s?\w*)(>?)(\s*\w*)@(\w+).(\w+)$')
r = re_email_match.match('<Tom Paris> tom@voyager.org')
print((r.group(0), r.group(1), r.group(2), r.group(3)))

def name_of_email(addr):
    re_email = re.compile(r'^(<?)(\w+\.?\s?\w*)(>?)(\s*\w*)@(\w+).(\w+)$')
    if re_email.match(addr) is not None:
        return re_email.match(addr).group(2)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


