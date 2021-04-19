hash_table = list([i for i in range(10)])
print(hash_table)

def hash_func(key):
    return key%5
# 엥?

data1 ='Andy'
data2 = 'Dave'
data3 = 'Trump'

## ord(): 문자의 ASCII 코드 리턴 :: 범위가 작다.
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))

print(ord(data1[0]), hash_func(ord(data1[0])))

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy','0101111111')
storage_data('Dave','0102222222')
storage_data('Trump','0103333333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))
print(get_data('Dave'))
print(get_data('Trump'))