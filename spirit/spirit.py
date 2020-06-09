"""
    Title: Highlight Spirit v1.0
    Function: 将 .cpp 文件转换为 HTML 并高亮显示 C++ 代码
    Author：Mr_Porridge
    TBC：Django + VUE 实时检测代码并展示高亮 v2.0
"""
import string


# 词法分析精灵
class spirit:
    def __init__(self, raw_string: str):
        self.raw = raw_string  # 初始化原始文件数据
        # self.de_space()
        self.furnace = ''  # 词法分析容器
        self.hold = False
        self.letters = list(string.ascii_letters)  # 26*2个字母
        self.separators = [',', ';', '(', ')', '{', '}', '[', ']', ':', '<', '>']  # 分隔符
        self.underline = '_'  # 下划线
        self.sharp = '#'
        self.digits = list(string.digits)  # 0~9数字

    def de_space(self):
        self.raw = self.raw.replace("\n", "")
        self.raw = self.raw.replace("\t", "")
        print(self.raw)

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

    def analyze(self):
        self.furnace = ''
        # 蟒生污点 不能修改循环遍历 自建指针
        pointer = -1  # pointer初始化为0时 第一个字符无法读取 所以初始化为-1
        for i in range(len(self.raw)):
            # 判断循环变量与指针的位置
            if i <= pointer:
                continue
            else:
                if self.raw[i] == ' ':
                    continue
                if self.is_letter(self.raw[i]) or self.is_underline(self.raw[i]) or self.is_sharp(self.raw[i]):
                    # 读入该字符 移动指针
                    self.furnace += self.raw[i]
                    i += 1
                    pointer = i
                    # 使用 while 读完整个单词和下一位 然后回退一位
                    while self.is_letter(self.raw[i]) or self.is_underline(self.raw[i]):
                        self.furnace += self.raw[i]
                        # 修改临时循环变量通过 while 读取下一个字符
                        i += 1
                        # 修改自定义指针
                        pointer = i
                    # 【重点】多读一位 -> 回退
                    pointer -= 1
                    print("word is: ", self.furnace)
                    self.furnace = ''
                    continue
                if self.is_separator(self.raw[i]):
                    self.furnace = self.raw[i]
                    print("separator is: ", self.furnace)
                    self.furnace = ''
                    continue


# 读取文件 采用UTF-8编码 为了防止读取中文出错
f = open('testCode.cpp', 'r', encoding='UTF-8')
# 获取文件内容 以字符串形式保存
elf = spirit(f.read())
# print(elf.raw)
elf.analyze()
