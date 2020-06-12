"""
@Introduction：
    Name: Highlight Spirit (v1.0)
    Function: Transfer C++ file to HTML file which performed with highlighting syntax
    Author：Mr_Porridge
    TBC：Use 'Django' and 'Vue' to build a 'Web C++ Editor' with real-time detecting (v2.0)
"""
import string

# 使用 string 包：用于初始化数字、字母 不用写函数自动生成了
"""
@使用方法：
    1、将想要转换文件放入code文件夹
    2、执行autoTest.py
    3、masterpiece文件夹下是输出的html文件
"""


# 词法分析精灵
class spirit:
    def __init__(self, raw_string: str):
        self.raw = raw_string  # 初始化原始文件数据
        # self.de_space()
        # 现在使用直接复制方法初始化 之后使用json进行初始化【之后需要改进】
        self.furnace = ''  # 词法分析容器
        self.letters = list(string.ascii_letters)  # 26*2个字母
        self.separators = [',', ';', '(', ')', '{', '}', '[', ']']  # 分隔符
        self.underline = '_'  # 下划线 用于处理标识符 _hello
        self.dash = '-'  # 短线 用于 ->
        self.sharp = '#'  # 井号 用于处理 #include #DEFINE
        self.dot = '.'  # . 用于处理 小数 和 对象
        self.left_slash = '/'  # / 用于注释
        self.single_quote = '\''  # 单引号
        self.double_quote = '\"'  # 双引号
        self.slash = '\\'  # \ 用于转义
        self.digits = list(string.digits)  # 0~9数字
        self.keywords = ['auto', 'break', 'bool', 'catch', 'char', 'cin', 'class', 'const', 'cout', 'default', 'delete',
                         'double', 'else', 'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'include',
                         'inline', 'int', 'long', 'namespace', 'new', 'operator', 'private', 'protected', 'public',
                         'return', 'short', 'signed', 'sizeof', 'static', 'stdio', 'string', 'struct', 'template',
                         'this', 'this', 'throw', 'true', 'try', 'typedef', 'union', 'using', 'unsigned', 'virtual',
                         'virtual', 'void', 'while']
        self.tab = '\t'  # 制表符 缩进
        self.enter = '\n'  # 回车换行
        self.single_op = ["%", "!", "^", '&', '|']  # 第一类操作符 包含 && 和 || 拆分成单个渲染即可
        self.double_op = ['+', '-', '=', '>', '<', '*', ':']  # 第二类操作符 有可能两个相同 or <= >= += -=
        # 存储结果
        self.bottle = []

    def de_space(self):
        self.raw = self.raw.replace("\n", "")
        self.raw = self.raw.replace("\t", "")
        # print(self.raw)

    # 判断读入字符是否为字母
    def is_letter(self, ch: str) -> bool:
        return ch in self.letters

    # 判断读入字符是否为_
    def is_underline(self, ch: str) -> bool:
        return ch == self.underline

    # 判读读入字符是否为分隔符
    def is_separator(self, ch: str) -> bool:
        return ch in self.separators

    # 判读读入字符是否为#
    def is_sharp(self, ch: str) -> bool:
        return ch == self.sharp

    # 判读读入字符是否为-
    def is_dash(self, ch: str) -> bool:
        return ch == self.dash

    # 判断读取是否为数字
    def is_digit(self, ch: str) -> bool:
        return ch in self.digits

    # 判断读入是否为.
    def is_dot(self, ch: str) -> bool:
        return ch in self.dot

    # 判断读入是否为\t
    def is_tab(self, ch: str) -> bool:
        return ch in self.tab

    # 判断读入是否为\n
    def is_enter(self, ch: str) -> bool:
        return ch in self.enter

    # 判断读入是否为 /
    def is_left_slash(self, ch: str) -> bool:
        return ch in self.left_slash

    # 判断读入是否为 '
    def is_single_quote(self, ch: str) -> bool:
        return ch in self.single_quote

    # 判断读入是否为 "
    def is_double_quote(self, ch: str) -> bool:
        return ch in self.double_quote

    # 判断读入是否为 \
    def is_slash(self, ch: str) -> bool:
        return ch in self.slash

    # 判断读入是否为 一类运算符
    def is_single_op(self, ch: str) -> bool:
        return ch in self.single_op

    # 判断读入是否为 二类运算符
    def is_double_op(self, ch: str) -> bool:
        return ch in self.double_op

    # 转义
    def trans(self, ch):
        if self.is_enter(ch):
            return "<br>"
        elif self.is_tab(ch):
            return "&emsp;"
        elif ch == ' ':
            return "&nbsp"
        else:
            return ch

    # 词法分析【不断扩充完善】
    def analyze(self):
        self.furnace = ''
        # 蟒生污点 不能修改循环遍历 自建指针
        pointer = -1  # pointer初始化为0时 第一个字符无法读取 所以初始化为-1
        for i in range(len(self.raw)):
            # 判断循环变量与指针的位置
            if i <= pointer:
                continue
            else:
                # 读入空格 继续
                if self.raw[i] == ' ':
                    continue
                # 读入标识符组成元素或# 判断：
                # 1、关键字
                # 2、#include #define 等
                # 3、标识符
                # 4、对象类
                elif self.is_letter(self.raw[i]) or self.is_underline(self.raw[i]) or self.is_sharp(self.raw[i]):
                    # 读入该字符 移动指针
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    # 使用 while 读完整个单词和下一位 然后回退一位
                    # #include 等只能以#打头 中间不允许出现 所以这里不包含self.is_sharp(self.raw[i])
                    while self.is_letter(self.raw[i]) or self.is_underline(self.raw[i]) or self.is_digit(self.raw[i]):
                        self.furnace += self.raw[i]
                        # 修改临时循环变量通过 while 读取下一个字符
                        i += 1
                        # 修改自定义指针
                        pointer = i
                    # 【重点】多读一位 -> 回退
                    pointer -= 1
                    # 1、关键字
                    if self.furnace in self.keywords:
                        # print("keyword: ", self.furnace)
                        self.bottle.append({"category": "keyword", "value": self.furnace})
                    # 2、#include #DEFINE等
                    elif self.is_sharp(self.furnace[0]):
                        # print("sharpe-special", self.furnace)
                        self.bottle.append({"category": "sharpe-special", "value": self.furnace})
                    # 3、标识符
                    else:
                        # print("word is: ", self.furnace)
                        self.bottle.append({"category": "word", "value": self.furnace})
                    self.furnace = ''
                    continue
                # 读取为分隔符
                elif self.is_separator(self.raw[i]):
                    self.furnace = self.raw[i]
                    # print("separator is: ", self.furnace)
                    self.bottle.append({"category": "separator", "value": self.furnace})
                    self.furnace = ''
                    continue
                # 读入- 判断->
                elif self.is_dash(self.raw[i]):
                    self.furnace = self.raw[i]
                    # -> 有且只有两位
                    # 所以预读一位 不改变pointer 不需要回退
                    if self.raw[i + 1] == '>':
                        self.furnace += self.raw[i + 1]
                        pointer = i + 1
                        # print("arrow-special ", self.furnace)
                        self.bottle.append({"category": "arrow-special", "value": self.furnace})
                        self.furnace = ''
                        continue
                    else:
                        # print("single-op ", self.furnace)
                        self.bottle.append({"category": "single-op", "value": self.furnace})
                        self.furnace = ''
                        continue
                # 读入数字
                elif self.is_digit(self.raw[i]):
                    dot_legal = True
                    # 读入该字符 移动指针
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    # 使用 while 读完整个number 然后回退一位
                    while self.is_digit(self.raw[i]) or self.is_dot(self.raw[i]):
                        # 判断小数点 并判断是否合法
                        if self.is_dot(self.raw[i]):
                            if dot_legal:
                                dot_legal = False
                            else:
                                # 两个小数点 非法 退出循环 直接回退一位
                                break
                        self.furnace += self.raw[i]
                        # 修改临时循环变量通过 while 读取下一个字符
                        i += 1
                        # 修改自定义指针
                        pointer = i
                    # 【重点】多读一位 -> 回退
                    pointer -= 1
                    # print("number: ", self.furnace)
                    self.bottle.append({"category": "number", "value": self.furnace})
                    self.furnace = ''
                    continue
                # 读入制表符
                elif self.is_tab(self.raw[i]):
                    # self.bottle.append({"category": "tab", "value": self.raw[i]})
                    self.bottle.append({"category": "tab", "value": "&emsp;"})
                    # print("tab: \\t")
                # 读入换行
                elif self.is_enter(self.raw[i]):
                    # self.bottle.append({"category": "enter", "value": self.raw[i]})
                    self.bottle.append({"category": "enter", "value": '<br>'})
                    # print("enter: \\n")
                # 读入 / 开始判断注释
                elif self.is_left_slash(self.raw[i]):
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    # 多行注释
                    if self.raw[i] == '*':
                        self.furnace += self.raw[i]
                        while not ((self.is_left_slash(self.raw[i])) and (self.raw[i - 1] == '*')):
                            i += 1
                            pointer = i
                            self.furnace += self.trans(self.raw[i])
                    # 单行注释
                    elif self.is_left_slash(self.raw[i]):
                        self.furnace += self.raw[i]
                        while not self.is_enter(self.raw[i]):
                            i += 1
                            pointer = i
                            self.furnace += self.trans(self.raw[i])
                    # 其它则为除号
                    else:
                        # print("single operator: ", self.furnace)
                        self.furnace = ''
                        pointer -= 1
                        continue
                    # print("comment: ", self.furnace)
                    self.bottle.append({"category": "comment", "value": self.furnace})
                    self.furnace = ''
                    continue
                # 单引号字符串
                elif self.is_single_quote(self.raw[i]):
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    while not self.is_single_quote(self.raw[i]):
                        # 转义字符
                        if self.is_slash(self.raw[i]):
                            self.furnace += "<strong class=\"escape\">" + self.raw[i] + self.raw[i + 1] + "</strong>"
                            i += 2
                            pointer = i
                        else:
                            self.furnace += self.raw[i]
                            i += 1
                            pointer = i
                    self.furnace += self.raw[i]
                    # print("string1: ", self.furnace)
                    self.bottle.append({"category": "string", "value": self.furnace})
                    self.furnace = ''
                # 双引号字符串
                elif self.is_double_quote(self.raw[i]):
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    while not self.is_double_quote(self.raw[i]):
                        # 转义字符
                        if self.is_slash(self.raw[i]):
                            self.furnace += "<strong class=\"escape\">" + self.raw[i] + self.raw[i + 1] + "</strong>"
                            i += 2
                            pointer = i
                        else:
                            self.furnace += self.raw[i]
                            i += 1
                            pointer = i
                    self.furnace += self.raw[i]
                    # print("string2: ", self.furnace)
                    self.bottle.append({"category": "string", "value": self.furnace})
                    self.furnace = ''
                # 运算符1
                elif self.is_single_op(self.raw[i]):
                    self.furnace = self.raw[i]
                    # print("single-op: ", self.furnace)
                    self.bottle.append({"category": "single-op", "value": self.furnace})
                    self.furnace = ''
                # 运算符2
                elif self.is_double_op(self.raw[i]):
                    if (self.raw[i + 1] == self.raw[i]) or (self.raw[i + 1] == '='):
                        self.furnace = self.raw[i] + self.raw[i + 1]
                        i += 2
                        pointer = i
                        # print("double operator: ", self.furnace)
                        self.bottle.append({"category": "double-op", "value": self.furnace})
                        self.furnace = ''
                    else:
                        self.furnace = self.raw[i]
                        # print("single operator: ", self.furnace)
                        self.bottle.append({"category": "single-op", "value": self.furnace})
                        self.furnace = ''
                # 读入其他 非法
                else:
                    # print("illegal identifier: ", self.raw[i])
                    self.bottle.append({"category": "illegal", "value": self.raw[i]})

    # 生成HTML文件
    def magic_wand(self, filename: str):
        name = filename.split(".")[0]
        display = open('./masterpiece/' + name + '.html', 'w+', encoding='UTF-8')
        display.write("<!DOCTYPE html>\n")
        display.write("<html>\n")
        display.write("<head>\n")
        display.write("<title>" + filename + "</title>\n")
        display.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"highlight.css\">\n")
        display.write("<meta charset=\"utf-8\">\n")
        display.write("</head>\n")
        display.write("<body>\n")
        for item in self.bottle:
            display.write("<span class=\"" + item['category'] + "\">" + item['value'] + "</span>\n")
        display.write("</body>\n")
        display.write("</html>\n")

    # HTML接口
    def render(self):
        res = ''
        for item in self.bottle:
            res += ("<span class=\"" + item['category'] + "\">" + item['value'] + "</span>\n")
        return res


def highlight(name: str):
    # 读取文件 采用UTF-8编码 为了防止读取中文出错
    f = open('./code/' + name, 'r', encoding='UTF-8')
    # 获取文件内容 以字符串形式保存
    elf = spirit(f.read())
    # print(elf.raw)
    elf.analyze()
    print(elf.bottle)
    elf.magic_wand(name)
