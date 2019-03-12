"""
Q: 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

A: 1. 先计算最终需要给出的长度，然后建立两个指针p1,p2，p1指向原始字符串的末尾，p2指向替换后的字符串的末尾。同时移动p1,p2, 将p1指的内容逐个复制到p2, 当p1遇到空格时，在p2处插入 %20， p1向前移动一个位置，p2向前移动3个位置，当p1和p2位置重合时，全部替换完成。

2. python中可以利用append() [O(1)]，新建list，一次遍历，碰到空格就添加 %20，否则就添加原始字符串s内容。

"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', '%20')