# coding:utf-8
import re
'''
正则表达式匹配流程
'''

'''
            正则表达式引擎
                |
正则表达式文本    |编译
                |
            正则表达式对象
                |
需要匹配的文本    |匹配
                |
              匹配结果

'''

#基础的请参考文章 https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

"""
构造特殊（不作为分组）
(?...)      (...)的不分组版本，用于使用'|'或后接数量词       (?:abc){2}      abcabc
(?iLmsux)   iLmsux的每个字符代表一个匹配模式，只能用在正则表达式的开头，可选多个。匹配模式将在下面介绍    （?i）abc     Abc
(?#...)     #号后的内容作为注释被忽略       abc(?#comment)123       abc123
(?=...)     之后的字符串内容需要匹配表达式才能成功匹配 不消耗字符串内容      a(?=\d)     后面是数字的a
(?!...)     之后的字符串内容需要不匹配表达式才能成功匹配  不消耗字符串内容    a(?!\d)     后面不是数字的a
(?<=...)    之前的字符串内容需要匹配表达式才能匹配成功   不消耗字符串内容    (?<=\d)a    前面是数字的a
(?<=...)    之前的字符串内容需要不匹配表达式才能匹配成功   不消耗字符串内容    (?<!\d)a    前面不是数字的a
(?(id/name)yes-pattern|no-pattern)      如果编号为id/别名为name的组匹配到字符，则需要匹配yes-pattern,否则需要匹配no-pattern. |no-pattern可以省略
                                        （\d)abc(?(1)\d|abc)             1abc2   abcabc
"""


'''re模块'''

# #将正则表达式编译成Pattern对象
# patern = re.compile(r'hello')
#
# #使用Pattern匹配文本，获得匹配结果，无法匹配则返回None
# match = patern.match("hello world")
#
# if match:
#     # 使用Match获得分组信息
#     print match.group()


'''
re.compile(strPattern[,flag]):
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。另外，你也可以在regex字符串中指定模式，比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。 
可选值有：

re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的
'''

# pattern_a = re.compile(
#     r"""\d+     # the integral part
#         \.      #the decimal part
#         \d*     #some fractional digits"""
#     ,
#     re.X
# )
#
# pattern_b = re.compile(r"\d\.\d")

# 注释    re提供了众多模块方法用于完成正则表达式的功能。这些方法可以使用Pattern实例的相应方法替代，唯一的好处是少写一行re.compile()代码，但同时也无法复用编译后的Pattern对象。这些方法将在Pattern类的实例方法部分一起介绍
# m = re.match(r'hello', 'hello world!')
# print m.group()


'''match对象'''

'''
Match对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。

属性：

string: 匹配时使用的文本。
re: 匹配时使用的Pattern对象。
pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。


方法：
group([group1, …]): 
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。

groups([default]): 
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。

groupdict([default]): 
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。

start([group]): 
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。

end([group]): 
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。

span([group]): 
返回(start(group), end(group))。

expand(template): 
将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。
'''

# import re
#
# m = re.match(r'(\w+)(\w+)(?P<sign>.*)', 'hello world!')
#
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
#
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

'''Pattern对象'''

'''
Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。

Pattern不能直接实例化，必须使用re.compile()进行构造。


Pattern提供了几个可读属性用于获取表达式的相关信息：

pattern: 编译时用的表达式字符串。
flags: 编译时用的匹配模式。数字形式。
groups: 表达式中分组的数量。
groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。
'''

# p = re.compile(r"(\w+)(\w+)(?P<sign>.*)",re.DOTALL)
#
# print "p.pattern:",p.pattern
# print "p.flags:",p.flags
# print "p.groups:",p.groups
# print "p.groupindex:",p.groupindex


'''re模块方法'''

'''
1   match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]): 
这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；如果匹配过程中pattern无法匹配，
或者匹配未结束就已到达endpos，则返回None。 
pos和endpos的默认值分别为0和len(string)；re.match()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。 
注意：这个方法并不是完全匹配。当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'。

2   search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]): 
这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；
若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。 
pos和endpos的默认值分别为0和len(string))；re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。 

3   split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]): 
按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。  这个切割和python字符串的切割基本相同

'''

# p = re.compile(r"\d+")
# print p.split("one1two2three3four4")

'''
4   findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]): 
搜索string，以列表形式返回全部能匹配的子串。 


5   finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]): 
搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 

6   sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
使用repl替换string中每一个匹配的子串后返回替换后的字符串。 

当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
count用于指定最多替换次数，不指定时全部替换。 
'''

# p = re.compile(r"(\w+)(\w+)")
# s = 'i say,hello world!'
#
# print p.sub(r"\2\1",s) # 先匹配到了在替换，sub第一个参数是将匹配到的值替换掉
#
#
# def func(m):
#     return m.group(1).title() + "" + m.group(2).title()
#
# print p.sub(func,s)


'''
7   subn(repl, string[, count]) |re.sub(pattern, repl, string[, count]): 
返回 (sub(repl, string[, count]), 替换次数)。
'''

# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print p.subn(r'\2 \1', s)
#
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
#
# print p.subn(func, s)


# 比re 更加强大的redex模块      https://www.cnblogs.com/animalize/p/4949219.html


