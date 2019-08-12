# coding:utf-8

# 元字符的完整列表      . ^ $ * + ? { [ ] \ | ( )


'''简单模式'''

'''
.   是一个统配符，可以匹配任意字符（但是某些情况下不能匹配行起始符）
{   花括号中的数字表示待查找的数字出现的次数    包含数字的花括号是一种量词
？   是一种量词，表示连字符是可选的 也就是说，连字符可以不出现或只出现一次
+   量词  表示一个或者多个
*   量词  表示零个或多个
^   开始  但是在[]中使用^,所代表的含义是除……之外


元字符	名称		作用
.	    句点	    	匹配任意字符
\	    反斜线		对字符转义
|	    竖线符		选择操作（或）
^	    脱字符		行起始锚位符
$	    美元符		行结束锚位符
?	    问号        匹配零次或一次的量词
*	    星号         匹配零次或多次的量词
+	    加号	        匹配一次或多次的量词
[	    左方括号	    字符组起始
]	    右方括号	    字符组结束
{	    左花括号	    量词或代码块起始
}	    右花括号    	量词或代码块结束
(	    左括号		分组起始
)	    右括号		分组结束”

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''



# 字符匹配

'''
我们首先考察的元字符是"[" 和 "]"。它们常用来指定一个字符类别，所谓字符类别就是你想匹配的一个字符集。字符可以单个列出，也可以用“-”号分隔的两个给定字符来表示一个字符区间。例如，[abc] 将匹配"a", "b", 或 "c"中的任意一个字符；也可以用区间[a-c]来表示同一字符集，和前者效果一致。如果你只想匹配小写字母，那么 RE 应写成 [a-z].
元字符在类别里并不起作用。例如，[akm$]将匹配字符"a", "k", "m", 或 "$" 中的任意一个；"$"通常用作元字符，但在字符类别里，其特性被除去，恢复成普通字符。
你可以用补集来匹配不在区间范围内的字符。其做法是把"^"作为类别的首个字符；其它地方的"^"只会简单匹配 "^"字符本身。例如，5 将匹配除 "5" 之外的任意字符。


也许最重要的元字符是反斜杠"\"。 做为 Python 中的字符串字母，反斜杠后面可以加不同的字符以表示不同特殊意义。它也可以用于取消所有的元字符，这样你就可以在模式中匹配它们了。举个例子，如果你需要匹配字符 "[" 或 "\"，你可以在它们之前用反斜杠来取消它们的特殊意义： [ 或 \。
一些用 "\" 开始的特殊字符所表示的预定义字符集通常是很有用的，象数字集，字母集，或其它非空字符集。下列是可用的预设特殊字符：
\d  匹配任何十进制数；它相当于类 [0-9]。   例如：匹配电话号码   
\D  匹配 任何非数字字符；它相当于类 [^0-9]。
\s  匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
\S  匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
\w  匹配任何字母 数字 下划线；它相当于类 [a-zA-Z0-9_]。
\W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。
这样特殊字符都可以包含在一个字符类中。如，[\s,.]字符类将匹配任何空白字符或","或"."。
本节最后一个元字符是 . 。它匹配除了换行字符外的任何字符，在 alternate 模式（re.DOTALL）下它甚至可以匹配换行。"." 通常被用于你想匹配“任何字符”的地方

更加详细的字符对照表


“字符简写式	描述
\a	报警符
\b	单词边界
[\b]	退格字符
\B	非单词边界
\cx	控制字符
\d	数字字符
\D	非数字字符
\dxxx	字符的十进制值
\f	换页符
\r	回车符
\n	换行符
\oxxx	字符的八进制值
\s	空白符
\S	非空白符
\t	水平制表符
\v	垂直制表符
\w	单词字符
\W	非单词字符
\0	空字符
\x xx	字符的十六进制值
\uxxxx	字符的Unicode值
”

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 

'''

'''
匹配各种空白符的简写式
\f	换页符
\h	水平空白符
\H	非水平空白符
\n	换行符
\r	回车符
\s	空白符
\S	非空白符
\t	水平制表符
\v	垂直制表符
\V	非垂直制表符 
'''

# 重复

'''
正则表达式第一件能做的事是能够匹配不定长的字符集，而这是其它能作用在字符串上的方法所不能做到的。 不过，如果那是正则表达式唯一的附加功能的话，那么它们也就不那么优秀了。它们的另一个功能就是你可以指定正则表达式的一部分的重复次数。
我们讨论的第一个重复功能的元字符是 。 并不匹配字母字符 "*"；相反，它指定前一个字符可以被匹配零次或更多次，而不是只有一次。
举个例子，ca*t 将匹配 "ct" (0 个 "a" 字符), "cat" (1 个 "a"), "caaat" (3 个 "a" 字符)等等。RE 引擎有各种来自 C 的整数类型大小的内部限制，以防止它匹配超过20亿个 "a" 字符；你也许没有足够的内存去建造那么大的字符串，所以将不会累计到那个限制。
象 * 这样地重复是“贪婪的”；当重复一个 RE 时，匹配引擎会试着重复尽可能多的次数。如果模式的后面部分没有被匹配，匹配引擎将退回并再次尝试更小的重复。
一步步的示例可以使它更加清晰。让我们考虑表达式 a[bcd]*b。它匹配字母 "a"，零个或更多个来自类 [bcd]中的字母，最后以 "b" 结尾。现在想一想该 RE 对字符串 "abcbd" 的匹配。
'''