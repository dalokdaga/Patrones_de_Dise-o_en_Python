"""
Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
"""

from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    
    
    Esta es una implementación segura para subprocesos de Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    
    
    Ahora tenemos un objeto de bloqueo que se usará para sincronizar subprocesos durante
    primer acceso al Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        

        Los posibles cambios en el valor del argumento `__init__` no afectan
        la instancia devuelta.        
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        
        # Ahora, imagina que el programa acaba de ser lanzado. Como no hay
        # Instancia Singleton aún, múltiples subprocesos pueden pasar simultáneamente el
        # condicional anterior y llegan a este punto casi al mismo tiempo. Él
        # el primero de ellos adquirirá el bloqueo y continuará, mientras que el
        # resto esperará aquí.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            
            # El primer subproceso en adquirir el bloqueo, alcanza este condicional,
            # entra y crea la instancia de Singleton. Una vez que deja el
            # bloque de bloqueo, un hilo que podría haber estado esperando el bloqueo
            # lanzamiento puede entonces entrar en esta sección. Pero dado que el campo Singleton
            # ya está inicializado, el hilo no creará un nuevo objeto.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    
    Usaremos esta propiedad para probar que nuestra Singleton realmente funciona
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        
        
        Finalmente, cualquier singleton debe definir alguna lógica comercial, que puede ser
        ejecutado en su instancia
        """


def test_singleton(value: str) -> None:    
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    # print("If you see the same value, then singleton was reused (yay!)\n"
    #       "If you see different values, "
    #       "then 2 singletons were created (booo!!)\n\n"
    #       "RESULT:\n")
    
    
    print("Si ve el mismo valor, entonces se reutilizó singleton (¡sí!)\n"
          "Si ve valores diferentes, "
          "entonces se crearon 2 singletons (¡booo!)\n\n"
          "RESULTADO:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
