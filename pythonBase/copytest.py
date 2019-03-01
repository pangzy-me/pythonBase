import copy

'''
    赋值：简单地拷贝对象的引用，两个对象的id相同。 
    浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。 
    深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。
           虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。

参考博客  https://www.cnblogs.com/xueli/p/4952063.html
'''

# # 复制-直接赋值，默认浅拷贝传递对象的引用而已,原始a列表改变，被赋值的b也会做相同的改变
# lista = [1, 2, 3, ['aa', 'bb', 'cc']]
# listb = lista     # 赋值，传对象的引用
# print(lista)
# print(listb)
#
# lista.append(4)
# print(lista)
# print(listb)
#
# lista[3].append('dd')
# print(lista)
# print(listb)

# # copy浅拷贝，没有拷贝子对象，所以原始数据a改变，子对象会改变(共享同一个子对象)
# lista1 = [1, 2, 3, ['aa', 'bb', 'cc']]
# listb1 = copy.copy(lista1)        # 对象拷贝，浅拷贝
# print(lista1)
# print(listb1)
#
# lista1.append(4)
# print(lista1)
# print(listb1)   # 没有改变
#
# lista1[3].append('dd')
# print(lista1)
# print(listb1)   # 里面的子对象共享，改变了

# 深拷贝，包含对象里面的子对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
lista2 = [1, 2, 3, ['aa', 'bb', 'cc']]
listb2 = copy.deepcopy(lista2)      # 对象拷贝，深拷贝
print(lista2)
print(listb2)

lista2.append(4)
print(lista2)
print(listb2)   # 始终没有改变

lista2[3].append('dd')
print(lista2)
print(listb2)   # 始终没有改变

