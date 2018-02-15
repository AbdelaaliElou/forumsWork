import models
import stores
#
m1 = models.Member("name1", 19, 1)
m2 = models.Member("name2", 38, 2)
m3 = models.Member("Delete", 5656, 3)
p1 = models.Post("p1 title", "p1 body", m1, 1)
p2 = models.Post("p2 title", "p2 body", m2, 2)
p3 = models.Post("p3 title", "p3 body", m3, 3)
#
# m1.show_member()
# m2.show_member()
# p1.show_topic()
# p2.show_topic()
# p3.show_topic()
ms = stores.MemberStore()
ms.add(m1)
ms.add(m2)
ms.add(m3)
# l = list(ms.get_by_id(1))
print ms.get_by_id(1)
print ms.get_all()

print ms.update_member(models.Member("Ahmed", 19, 1))
print ms.get_by_id(1)
print ms.get_all()
print ms.is_exist(models.Member("Ahmed", 19, 1))
print ms.delete(3)
print ms.get_all()
ps = stores.PostStore()

ps.add(p1)
ps.add(p2)
ps.add(p3)

print ps.get_all()
