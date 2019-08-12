# coding:utf-8



'''Unicode空白字符'''

'''
“简写或别名	名称	代码点	正则表达式
HT	水平制表符	U+0009	\u0009或\t
LF	换行符	U+000A	\u000A或\n
VT	垂直制表符	U+000B	\u000B或\v
FF	换页符	U+000C	\u000C或\f
CR	回车符	U+000D	\u000d或\r
SP	空格符	U+0020	\u0020或\s*
NEL	下一行	U+0085	\u0085
NBSP	非间断空格	U+00A0	\u00A0
—	欧甘空格	U+1680	\u1680
MVS	蒙古文母音分隔符	U+180E	\u180E
BOM	字节顺序标记	U+FEFF	\ufeff
NQSP	半身空铅	U+2000	\u2000
MQSP，Mutton Quad	全身空铅	U+2001	\u2001
ENSP，Nut	单[…]”
“ZWSP	零宽度空格	U+200B	\u200B
LSEP	行列分隔符	U+2028	\u2028
PSEP	段落分隔符	U+2029	\u2029
NNBSP	窄式不换行空格	U+202F	\u202F
MMSP	中等数学间隔	U+205F	\u205f
IDSP	表意字符间隔	U+3000	\u3000”

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''

'''控制字符'''

'''
“控制字符	Unicode值	简写	名称
c@*	U+0000	NUL	空字符
\cA	U+0001	SOH	标题起始
\cB	U+0002	STX	文本起始
\cC	U+0003	ETX	文本结束
\cD	U+0004	EOT	传输结束
\cE	U+0005	ENQ	询问
\cF	U+0006	ACK	确认
\cG	U+0007	BEL	报警符
\cH	U+0008	BS	退格符
\cI	U+0009	HT	水平制表符
\cJ	U+000A	LF	换行符
\cK	U+000B	VT	垂直制表符
\cL	U+000C	FF	换页
\cM	U+000D	CR	回车符
\cN	U+000E	SO	移出
\cO	U+000F	SI	移入
\cP	U+0010	DLE	数据链转义
\cQ	U+0011	DC1	设备[…]”
“\cV	U+0016	SYN	同步空闲
\cW	U+0017	ETB	传输块结尾
\cX	U+0018	CAN	取消
\cY	U+0019	EM	介质结尾
\cZ	U+001A	SUB	替换
\c[	U+001B	ESC	转义
\c\	U+001C	FS	信息分隔符四
\c]	U+001D	GS	信息分隔符三
\c^	U+001E	RS	信息分隔符二
\c_	U+001F	US	信息分隔符一
”
“*可以使用大写或者小写形式。例如，\cA与\ca是等价的；但是Java实现版本要求大写”

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''

'''字符属性'''

'''
属性	描述
C	其他字符
Cc	控制字符
Cf	格式字符
Cn	未分配字符
Co	专用字符
Cs	替代字符
L	字母
Ll	小写字母
Lm	修饰字母
Lo	其他字母
Lt	标题字母
Lu	大写字母
L&	Ll、 Lu或者Lt
M	标记符号
Mc	空格标记符
Me	环绕标记符
Mn	非空格标记符
N	数字
Nd	十进制数字
Nl	字母数字
No	其他数字
P	标点符号”
“Pc	连接标点
Pd	破折号
Pe	结束标点符
Pf	最终标点符
Pi	起始标点符
Po	其他标点符
Ps	开始标点符
S	符号
Sc	货币符号
Sk	修饰符号
Sm	数学符号
So	其他符号
Z	分隔符
Zl	行分隔符
Zp	段落分隔符
Zs	空格分隔符


摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''

'''POSIX字符组'''

'''
“字符组	描述
[[:alnum:]]	字母数字字符 （字母和数字）
[[:alpha:]]	字母字符（字母）
[[:ascii:]]	ASCII字符 （总共128个）
[[:blank:]]	空白字符
[[:ctrl:]]	控制字符
[[:digit:]]	数字
[[:graph:]]	图形字符
[[:lower:]]	小写字母
[[:print:]]	可打印字符
[[:punct:]]	标点符号
[[:space:]]	空格字符
[[:upper:]]	大写字母
[[:word:]]	单词字符
[[:xdigit:]]	十六进制数字”

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''


'''选项与修饰符'''

'''
选项	描述	支持平台
(?d)	Unix中的行	Java
(?i)	不区分大小写	PCRE、Perl、Java
(?J)	允许重复的名字	PCRE*
(?m)	多行	PCRE、Perl、Java
(?s)	单行（dotall）	PCRE、Perl、Java
(?u)	Unicode	Java
(?U)	默认最短匹配	PCRE
(?x)	忽略空格和注释	PCRE、Perl、Java
(?-…)	撤销设置或关闭选项	PCRE

摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks. 
'''

'''正则表达式与ASCII码表'''

'''
二进制	八进制	十进制	十六进制	字符	键盘	正则表达式	名称
00000000	0	0	0	NUL	^@	\c@	空字符
00000001	1	1	1	SOH	^A	\cA	标题开始
00000010	2	2	2	STX	^B	\cB	文本开始
00000011	3	3	3	ETX	^C	\cC	文本结束
00000100	4	4	4	EOT	^D	\cD	传输结束
00000101	5	5	5	ENQ	^E	\cE	询问
00000110	6	6	6	ACK	^F	\cF	确认
00000111	7	7	7	BEL	^G	\a， \cG	警报字符
00001000	10	8	8	BS	^H	[\b]， \cH	退格符
00001001	11	9	9	HT	^I	\t， \cI	水平制表符
00001010	12	[…]”
“00010111	27	23	17	ETB	^W	\cW	传输块结尾
00011000	30	24	18	CAN	^X	\cX	取消
00011001	31	25	19	EM	^Y	\cY	介质结尾
00011010	32	26	1A	SUB	^Z	\cZ	替换
00011011	33	27	1B	ESC	^[	\e， \c[	转义
00011100	34	28	1C	FS	^|	\c|	文件分隔符
00011101	35	29	1D	GS	^]	\c]	分组分隔符
00011110	36	30	1E	RS	^^	\c^	记录分隔符
00011111	37	31	1F	US	^_	\c_	单元分隔符
00100000	40	32	20	SP	SP	\s， [ ]	空格
00100001	41	33	21	!	!	!	感叹号
00100010	42	34	22	"	"	"	引号
00100011	43	35	23	#	#	#	井号
00100100	44	36	24	$	$	\$	美元符
00100101	45	37	25	%	%	%	百分号
00100110	46	38	26	&	&	&	和号
00100111	47	39	27	'	'	'	撇号
00101000	50	40	28	(	(	(， \(	左括号
00101001	51	41	29	)	)	)， \)	右括号
00101010	52	42	2A	*	*	*	星号
00101011	53	43	2B	+	+	+	加号
00101100	54	44	2C	,	,	,	逗号
00101101	55	45	2D	-	-	-	连字符
00101110	56	46	2E	.	.	\.， [.]	句号
00101111	57	47	2F	/	/	/	斜线
00110000	60	48	30	0	0	\d， [0]	数字0
00110001	61	49	31	1	1	\d， [1[…]”
“00110101	65	53	35	5	5	\d， [5]	数字5
00110110	66	54	36	6	6	\d， [6]	数字6
00110111	67	55	37	7	7	\d， [7]	数字7
00111000	70	56	38	8	8	\d， [8]	数字8
00111001	71	57	39	9	9	\d， [9]	数字9
00111010	72	58	3A	:	:	:	冒号
00111011	73	59	3B	;	;	;	分号
00111100	74	60	3C	<	<	<	小于号
00111101	75	61	3D	=	=	=	等于号
00111110	76	62	3E	>	>	>	大于号
00111111	77	63	3F	?	?	?	问号
01000000	100	64	40	@	@	@	at
01000001	101	65	41	A	A	\w， [A]	拉丁大写字母A
01000010	102	66	42	B	B	\w， [B]	拉丁大写字母B
01000011	103	67	43	C	C	\w， [C]	拉丁大写字母C
01000100	104	68	44	D	D	\w， [D]	拉丁大写字母D
01000101	105	69	45	E	E	\w， [E]	拉丁大写字母E
01000110	106	70	46	F	F	\w， [F]	拉丁大写字母F
01000111	107	71	47	G	G	\w， [G]	拉丁大写字母G
01001000	110	72	48	H	H	\w， [H]	拉丁大写字母H
01001001	111	73	49[…]”
“01010011	123	83	53	S	S	\w， [S]	拉丁大写字母S
01010100	124	84	54	T	T	\w， [T]	拉丁大写字母T
01010101	125	85	55	U	U	\w， [U]	拉丁大写字母U
01010110	126	86	56	V	V	\w， [V]	拉丁大写字母V
01010111	127	87	57	W	W	\w， [W]	拉丁大写字母W
01011000	130	88	58	X	X	\w， [X]	拉丁大写字母X
01011001	131	89	59	Y	Y	\w， [Y]	拉丁大写字母Y
01011010	132	90	5A	Z	Z	\w， [Z]	拉丁大写字母Z
01011011	133	91	5B	[	[	\[	左方括号
01011100	134	92	5C	\	\	\	反斜线
01011101	135	93	5D	]	]	\]	右方括号
01011110	136	94	5E	^	^	^， [^]	抑扬符号
01011111	137	95	5F	_	_	_， [_]	下划线
00100000	140	96	60	`	`	\`	重音符
01100001	141	97	61	a	a	\w， [a]	拉丁小写字母A
01100010	142	98	62	b	b	\w， [b]	拉丁小写字母B
01100011	143	99	63	c	c	\w， [c]	拉丁小写字母C
01100100	144	100	64	d	d	\w， [d]	拉丁小写字母D
01100101	145	101[…]”
“01110001	161	113	71	q	q	\w， [q]	拉丁小写字母Q
01110010	162	114	72	r	r	\w， [r]	拉丁小写字母R
01110011	163	115	73	s	s	\w， [s]	拉丁小写字母S
01110100	164	116	74	t	t	\w， [t]	拉丁小写字母T
01110101	165	117	75	u	u	\w， [u]	拉丁小写字母U
01110110	166	118	76	v	v	\w， [v]	拉丁小写字母V
01110111	167	119	77	w	w	\w， [w]	拉丁小写字母W
01111000	170	120	78	x	x	\w， [x]	拉丁小写字母X
01111001	171	121	79	y	y	\w， [y]	拉丁小写字母Y
01111010	172	122	7A	z	z	\w， [z]	拉丁小写字母Z
01111011	173	123	7B	{	{	{	左花括号
01111100	174	124	7C	|	|	|	竖线
01111101	175	125	7D	}	}	}	右花括号
01111110	176	126	7E	~	~	\~	波浪符
01111111	177	127	7F	DEL	^?	\c?	删除


摘录来自: [美]Michael Fitzgerald. “学习正则表达式 (图灵程序设计丛书)。” iBooks.  

'''