"""

将字符串中的空格全部替换为“%20”。假定该字符串有足够的空间存放新增的字符，并且知道字符串的真实长度(小于等于1000)，同时保证字符串由大小写的英文字母组成。

给定一个string iniString 为原始的串，以及串的长度 int len, 返回替换后的string。


该题为模拟字符串的replace方法。要做到空间复杂度最低，遍历原数组，计算空格的数量，
则现字符串的长度为len+2*n.然后用倒序遍历，如果遇到' ',将空替换为‘20%’。
"""



