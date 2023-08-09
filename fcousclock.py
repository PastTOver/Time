from datetime import datetime

"""Python日期时间到时间戳"""
# 当前日期和时间
now = datetime.now()
timestamp = datetime.timestamp(now)
print('时间戳：', timestamp)
print('类型：', type(timestamp))

# 10位的时间戳，精确到秒
ts10 = str(timestamp).split('.')[0]
print('10位时间戳:', ts10)

# 13位的时间戳，精确到毫秒
ts13 = str(timestamp*1000).split('.')[0]
print('13位时间戳:', ts13)


"""Python时间戳到日期时间"""
timestamp = 1675042819.1232566
dt1 = datetime.fromtimestamp(timestamp)
print("时间戳转日期：", dt1)
print("类型：", type(dt1))

dt = datetime.fromtimestamp(int(ts10))
print("10位时间戳转日期：", dt)
