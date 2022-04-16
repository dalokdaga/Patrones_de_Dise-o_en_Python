"""
Observer Design Pattern

Intent: Lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they're observing.

Note that there's a lot of different terms with similar meaning associated with
this pattern. Just remember that the Subject is also called the Publisher and
the Observer is often called the Subscriber and vice versa. Also the verbs
"observe", "listen" or "track" usually mean the same thing.

Intención: le permite definir un mecanismo de suscripción para notificar múltiples objetos
sobre cualquier evento que le suceda al objeto que están observando.

Tenga en cuenta que hay muchos términos diferentes con un significado similar asociado con
este patrón Recuerde que el Sujeto también se llama Editor y
el observador a menudo se denomina suscriptor y viceversa. También los verbos
"observar", "escuchar" o "rastrear" suelen significar lo mismo.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    
    La interfaz Asunto declara un conjunto de métodos para administrar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.

    El Sujeto posee algún estado importante y notifica a los observadores cuando el estado
    cambios.    
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
        
    En aras de la simplicidad, el estado del Sujeto, esencial a todo
    suscriptores, se almacena en esta variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    
    Lista de suscriptores. En la vida real, la lista de suscriptores se puede almacenar
    de forma más completa (categorizados por tipo de evento, etc.).    
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Adjunto un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Activar una actualización en cada suscriptor.
        """

        print("Subject: Notificar a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        
        Realmente lo hago. Los sujetos comúnmente tienen alguna lógica comercial importante, que
        activa un método de notificación cada vez que algo importante está a punto de suceder
        ocurrir (o después).        
        """
        print(self._observers)
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
        
    La interfaz de Observer declara el método de actualización, utilizado por los sujetos.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:        
        """
        Receive update from subject.
        
        Recibir actualización del asunto.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.

Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto que les había sido
adjunto a.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        #if subject._state < 3:
        print("Envio notificacion al sns Observer A")
        print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        #if subject._state == 0 or subject._state >= 2:
        print("Envio notificacion al sns Observer B")
        print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.detach(observer_a)
    subject.some_business_logic()

    subject.detach(observer_b)

    subject.some_business_logic()
