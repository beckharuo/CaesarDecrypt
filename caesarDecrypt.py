#coding:utf8
"""
    委员长博客凯撒密码解密
    @param1 str (string) 加密后的字符串
    @param2 offset （int） 偏移量
"""
str = raw_input("请输入您要解密的字符串: ");
offset = raw_input("请输入偏移量：")
res = ''
num = 1
for i in str:
    character = ord(i)
    #只有大写字母才会被处理，我所有加密过后的数据全是大写
    if (65<=character)&(90>=character):
        size = (int(offset)*(2**(num-1)))%26
        character -= size
        if 64>character:
            character += 90-64
        num += 1
    res += chr(character)
res = res.lower()
print('解密后的字符串为：'+res)
