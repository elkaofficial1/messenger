list1 = [1, 2, 3, 4, 5]

list2 = [4, 5, 6, 7, 8]

set2 = set(list2)

if any(item in set2 for item in list1):
    pass
    #тут типо есть одинаковые элементы. тут просто отправим сообщение. (ну или ошибку выдаст. мне без разницы)
else:
    # тут нет повторок! так что тут будем шифрование писать
    pass
# потом этот питон код надо переделать наверно в js чтобы запускался именно на устройстве отправителя. расшифровку тоже надо сделать так же.
