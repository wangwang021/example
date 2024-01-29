import csv

# 读取csv文件
result = csv.reader(open('./csv模块/example.csv', 'r'))
for row in result:
    print(row)

# 保存csv文件
data = [['a', 'b', 'c', 'd'], [1, 2, 3, 4], [1, 2, 3, 4]]
with open('./csv模块/test1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 保存一行
    writer.writerow(['a', 'b', 'c', 'd'])
    # 保存多行
    writer.writerows(data)
