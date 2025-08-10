import pickle 

# имя файла в котором мы сохраним обьект
spoplistfile = 'shoplist.data'
# список покупок
shop = ['яблоко','манго','морковь']

# запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем обьект в файл 
f.close()

del shoplist # уничтожаем переменую shop
# Считываем из хранилищя

f = open(shoplist, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)
