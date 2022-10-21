print('*** Início do módulo')

class MetaAnseriforme(type):
    print('*** Início da metaclasse')

    def __new__(meta_cls, cls_name, bases, cls_dict, **kw):
        print(f'*** __new__ da metaclasse')

        cls = super().__new__(meta_cls, cls_name, bases, cls_dict, **kw)

        return cls

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print(f'*** __init__ da metaclasse')
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __call__(cls):
        print('*** __call__ da metaclasse')
        return super().__call__()

    def __repr__(cls):  # <8>
        cls_name = cls.__name__
        return f"classe {cls_name!r} com repr MetaAnseriforme"

    print('*** Fim da metaclasse')


print('*** Entre metaclasse e classe')

class Pato(metaclass=MetaAnseriforme):

    print("*** No começo da declaração da classe")

    def __new__(self):
        print("*** Durante o __new__ da classe")
        return super().__new__()

    def __init__(self):
        print("*** Durante o init da classe")

    def quack(self):
        print("Quack!")

    print("*** No fim da declaração da classe")

print('*** Entre classe e instância')

pato = Pato()

print('*** Fim do módulo')