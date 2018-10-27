# print('[{name:<{len}}\tx'.format(name=name+']',len=22-len(name.encode('GBK'))+len(name)))

# str = 'hello'
# print('{:<20}'.format(str))
# print('{:>20}'.format(str))
# print('{:a<20}'.format(str))

# name1 = '中国'
# print('[{name:<{len}}\tx'.format(name=name1+']',len=22-len(name1.encode('GBK'))+len(name1)),chr(12288))
# name2 = 'Chinese'
# print('[{name:<{len}}\tx'.format(name=name2+']',len=22-len(name2.encode('GBK'))+len(name2)),chr(12288))
# name3 = '中国人Chinese'
# print('[{name:<{len}}\tx'.format(name=name3+']',len=22-len(name2.encode('GBK'))+len(name2)),chr(12288))

#第二种方法

# ulist =[]
# ulist.append([1, "清华大学", "10"])
# ulist.append([2, "中国科学技术大学aaaaaaaaa", "10"])
# ulist.append([3, "复旦大学", "10"])
#
# # for ul in ulist:
# #     print("{:^6}\t{:^10}\t{:^6}".format(ul[0], ul[1], ul[2]))
#
# for ul in ulist:
#     print("{0:<10}\t{1:{3}<20}\t{2:<10}".format(ul[0],ul[1],ul[2],chr(12288)))

# 第三种方法
#
# def get_str_width(string):
#     widths = [
#       (126,  1), (159,  0), (687,   1), (710,  0), (711,  1),
#       (727,  0), (733,  1), (879,   0), (1154, 1), (1161, 0),
#       (4347,  1), (4447,  2), (7467,  1), (7521, 0), (8369, 1),
#       (8426,  0), (9000,  1), (9002,  2), (11021, 1), (12350, 2),
#       (12351, 1), (12438, 2), (12442,  0), (19893, 2), (19967, 1),
#       (55203, 2), (63743, 1), (64106,  2), (65039, 1), (65059, 0),
#       (65131, 2), (65279, 1), (65376,  2), (65500, 1), (65510, 2),
#       (120831, 1), (262141, 2), (1114109, 1),
#     ]
#     width = 0
#     for each in string:
#         if ord(each) == 0xe or ord(each) == 0xf:
#             each_width = 0
#             continue
#         elif ord(each) <= 1114109:
#             for num, wid in widths:
#                 if ord(each) <= num:
#                     each_width = wid
#                     width += each_width
#                     break
#             continue
#
#         else:
#             each_width = 1
#         width += each_width
#
#     return width
#
# def align_string(string, width):
#     string_width = get_str_width(string)
#     if width > string_width:
#         return string+' '*(width-string_width)
#     else:
#         return string
#
# s1 = '一个长句子abcdef一个长句子abcde一个长句子abcde'
# s2 = '短句子12一abcde3一个长句子abcde'
# print(align_string(s1, 50) + align_string(s2, 30))
# print(align_string(s2, 50) + align_string(s1, 30))

print('放弃吧，尝试的方法都对中英文混合的对不齐...')

# import timeit
# def test():
#     L = []
#     for i in range(10):
#         L.append(i)
# if __name__ == '__main__':
#     print(timeit.timeit("test()", setup="from __main__ import test"))
#
#     x = list(range(20))
#     t0 = timeit.timeit("x.pop(0)", "from __main__ import x", number=1000)
#     print(f"cost seconds {t0}")
#
import random
print(random.randint(1,5))
print(list(range(0,5)))
