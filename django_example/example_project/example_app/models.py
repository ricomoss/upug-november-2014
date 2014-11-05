from django.db import models


class FibHistory(models.Model):
    fib_index = models.PositiveIntegerField()
    fib_num = models.TextField(max_length=10000)

    def sum_fib_nums(self):
        qs = self.all()
        total = 0
        for q in qs:
            total += int(q.fib_num)
        return total