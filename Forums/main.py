import models

m1 = models.Member("name1", 19)
m2 = models.Member("name2", 38)
p1 = models.Post("p1 title", "p1 body")
p2 = models.Post("p2 title", "p2 body")
p3 = models.Post("p3 title", "p3 body")

m1.show_member()
m2.show_member()
p1.show_topic()
p2.show_topic()
p3.show_topic()
