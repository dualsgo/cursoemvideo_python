from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.traceback import install
from rich import inspect

texto = 'Olá, pessoal!'
tamanho = len(texto)
caixa = Panel(texto, title='Minha Caixa', subtitle='Rich é incrível!', style='bold magenta', width=2*tamanho)
print(caixa)

inspect(caixa)


