from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.python import PythonLexer
from sqlparse import format

from ecommerce.inventory.models import *


def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PythonLexer(), TerminalFormatter()))


y = ProductInventory.objects.filter(product_id=1)

x = ProductInventory.objects.raw(
    "SELECT * FROM inventory_productinventory WHERE product_id = 1"
)
