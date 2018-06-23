#coding=utf8
def decimal2bin(decimal,into=2,custom=""):
    '''十进制转into进制'''
    '''
    参数说明:
        decimal:所要转化的十进制数
        into:要转换的进制
        custom:此函数默认只定义了2,8,16进制的进制头分别为"0b","0o","0x",
        想要定义其他进制需要一个字母作为前置的第二位
        进制头组成:"0"+"一个字母"
        ''' 
   '''选择进制部分'''
    start=["0"]
    if into==2:
        start.append("b")
    elif into==8:
        start.append("o")
    elif into==16:
        start.append("x")
    elif custom and into not in [2,8,16]:
        start.append(custom) 
   '''进制计算部分''' 

   '''进制计算思路
   1，用decimal对所要转化的进制(into参数)求余(%)，这样算出来的是第一位
   数,并将求得值加入start列表
   2，用decimal对所要转换的进制求商(/),这样算出来的是下一位的decimal
   3，重复（1）（2）过程，直到decimal==0''' 
    #知道decimal==0退出循环
    while decimal:
        #求余算出这一位的值
        every_position=decimal%into
        #把求得的值插入start列表第二位["0","b","这一位"]
        start.insert(2,str(every_position))
        #decimal=decimal/into,算出下一位用来求余的十进制数
        decimal/=into
    return "".join(start)


if __name__ == "__main__":
    print decimal2bin(8,3,"k")
    print decimal2bin(8,8)
    print decimal2bin(8,16)
    print decimal2bin(8)
