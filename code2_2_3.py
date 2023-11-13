A = {'国語','算数','理科','社会','英語'}
B = {'国語','数学','理科','地理','物理'}
print('心の準備ができたらEnterキーを押してください')
# (len(A &B))
print((len(A & B)/len( A | B))*100)
total = len(A & B)
result = len(A | B)
print(f'相性度は{(total / result)*100}%')

total1 = A & B
result1 = A | B
rate = len(total1) / len(result1) *100
print(f'相性度は{rate}%')