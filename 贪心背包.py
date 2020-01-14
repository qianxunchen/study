# 完全背包问题，贪心算法
class goods:
  def __init__(self, goods_id, weight=0, value=0):
    self.id = goods_id
    self.weight = weight
    self.value = value
def knapsack(capacity=0, goods_set=[]):
  # 按单位价值量排序
  goods_set.sort(key=lambda obj: obj.value / obj.weight, reverse=True)#计算单位价值密度并排序
  result = []#定义一个数组，用来存价值密度
  for a_goods in goods_set:#遍历排序后的价值密度
    if capacity < a_goods.weight:#判断当前单位价值密度的重量是否大于背包的剩余重量
      break
    result.append(a_goods)#将价值密度加入数组
    capacity -= a_goods.weight#在背包剩余的重量中减去加入数组的，就是已经选上的
  if len(result) < len(goods_set) and capacity != 0:#判断数组中的物品数是否小于总的物品数，如果小于，并且剩余重量不等于0，
    result.append(goods(a_goods.id, capacity, a_goods.value * capacity / a_goods.weight))#将每一个结果加入数组
  return result#将结果返回


some_goods = [goods(0, 2, 4), goods(1, 8, 6), goods(2, 5, 3), goods(3, 2, 8), goods(4, 1, 2)]#定义各个物品的编号以及重量与价值
res = knapsack(6, some_goods)#调用贪心算法函数
for obj in res:#遍历输出每一个可行结果
  print('物品编号:' + str(obj.id) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.value) + '单位价值量为:' + str(obj.value / obj.weight))


