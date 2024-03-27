immutable_var=1,2,True,'home'
print(immutable_var)
#print(immutable_var[2])=False # потому что кортеж - неизменяем. нельзя менять его элементы и нельзя добавить.
mutable_list=[15,17,'song']
print(mutable_list)
mutable_list[1]='melody'
print(mutable_list)
