# score = {'国語','算数','理科','社会','英語'},

scores = []
scores.append(int(input('国語の点数を入力 >>')))
scores.append(int(input('算数の点数を入力 >>')))
scores.append(int(input('理科の点数を入力 >>')))
scores.append(int(input('社会の点数を入力 >>')))
scores.append(int(input('英語の点数を入力 >>')))
# print(sum(scores))
print(f'合計{sum(scores)}点 平均{sum(scores) / len(scores)}点')