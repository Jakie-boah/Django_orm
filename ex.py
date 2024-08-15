from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.python import PythonLexer

from ecommerce.inventory.models import *
from pygments import highlight
from sqlparse import format


def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PythonLexer(), TerminalFormatter()))


x = Product.objects.all().values('id')[:10]

x = Product.objects.filter(id__gt=1)
Product.objects.exclude()
Product.objects.get()

x = Product.objects.filter(name__icontains='Widstart running sneakers')

ProductInventory.objects.filter(retail_price__gte=10)
