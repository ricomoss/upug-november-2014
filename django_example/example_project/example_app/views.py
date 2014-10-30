from django.views.generic import View
from django.http import HttpResponse


class FibNum(View):
    @staticmethod
    def fib(n):
        if n < 2:
            return 0
        a = 0
        b = 1
        i = 0
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
        return b

    def get(self, request):
        return HttpResponse(self.fib(int(request.GET.get('num', 0))))
