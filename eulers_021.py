from _util import Util
devisors = Util().listDevisors


for n in range(1,101):
    x=devisors(30)
    x=x[:len(x)-1]
