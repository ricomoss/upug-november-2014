from django.db import models


class FibHistory(models.Model):
    fib_index = models.PositiveIntegerField()
    fib_num = models.TextField(max_length=10000)

    def do_something_pointless(self):
        return self.fib_index * int(self.fib_num)
