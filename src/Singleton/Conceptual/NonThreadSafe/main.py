"""
Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).


Intención: le permite asegurarse de que una clase tenga solo una instancia, al tiempo que proporciona una
punto de acceso global a esta instancia. Una instancia por cada subclase (si corresponde).
"""


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    
    La clase Singleton se puede implementar de diferentes maneras en Python. Algunos
    los métodos posibles incluyen: clase base, decorador, metaclase. Usaremos el
    metaclase porque es la más adecuada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        
        Los posibles cambios en el valor del argumento `__init__` no afectan
        la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        
        
        Finalmente, cualquier singleton debe definir alguna lógica comercial, que puede ser
        ejecutado en su instancia.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas variables contienen la misma instancia.")
        
    else:
        print("Singleton falló, las variables contienen diferentes instancias.")
