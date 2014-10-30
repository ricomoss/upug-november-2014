from django.views.generic import View
from django.http import HttpResponse, Http404

from example_app.forms import FibNumForm
from example_app.models import FibHistory


class FibNumView(View):
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
        form = FibNumForm(request.GET)
        if form.is_valid():
            fib_index = form.cleaned_data.get('fib_index', 0)
            try:
                fib_history = FibHistory.objects.get(fib_index=fib_index)
                fib_num = fib_history.fib_num
            except FibHistory.DoesNotExist:
                fib_num = self.fib(fib_index)
                FibHistory.objects.create(fib_index=fib_index, fib_num=fib_num)
            return HttpResponse(fib_num)
        return Http404()
