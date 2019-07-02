from django.db import models


# Create your models here.
class Counter(models.Model):
    groupno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)

    def __str__(self):
        return 'Counter({0}, {1}, {2})'.format(self.groupno, self.depth, self.orderno)
