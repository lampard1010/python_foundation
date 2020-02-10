import re

if __name__ == '__main__':
    pattern = re.compile("abc", re.I)
    match = pattern.findall("abcABCaBcAbC")
    print(match)

#查看第一个是否匹配
    match2 = re.match("a", "33333abc5A2B46CaBc78A9bC", re.I)
    print(match2)

#查看所有字符串
    match3 = re.search("a", "33333abc5A2B46CaBc78A9bC", re.I)
    print(match3)

    str = "hel^lo wor^ld, hel^lo fr^ank!"
    l = str.split(",")
    print(l)

    match4 = re.split(r"/^", str)
    print(match4)