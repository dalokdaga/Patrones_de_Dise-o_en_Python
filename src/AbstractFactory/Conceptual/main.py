"""
Abstract Factory Design Pattern

Intent: Lets you produce families of related objects without specifying their
concrete classes.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.

    La interfaz de Abstract Factory declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos productos se denominan familia y son
    relacionados por un tema o concepto de alto nivel. Los productos de una familia suelen ser
    capaces de colaborar entre ellos. Una familia de productos puede tener varios
    variantes, pero los productos de una variante son incompatibles con los productos de
    otro.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.

    Las Fábricas de Concreto producen una familia de productos que pertenecen a un solo
    variante. La fábrica garantiza que los productos resultantes son compatibles. Nota
    que las firmas de los métodos de Concrete Factory devuelven un resumen
    producto, mientras que dentro del método se instancia un producto concreto.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.

    Cada Concrete Factory tiene una variante de producto correspondiente.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.

    Cada producto distinto de una familia de productos debe tener una interfaz base. Todos
    las variantes del producto deben implementar esta interfaz.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.

Los Productos de Concreto son creados por las Fábricas de Concreto correspondientes.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        print("ejecuta la reglas que necesite ")
        # return "The result of the product A1."
        return "esta regresando de aqui -> ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        # return "The result of the product A2."
        return "esta regresando de aqui -> ConcreteProductA2"


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.

    Aquí está la interfaz base de otro producto. Todos los productos pueden interactuar
    entre sí, pero la interacción adecuada sólo es posible entre productos de
    la misma variante concreta.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...pero también puede colaborar con el ProductA.

        The Abstract Factory se asegura de que todos los productos que crea sean de la
        misma variante y por lo tanto, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.

Los Productos de Concreto son creados por las Fábricas de Concreto correspondientes.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        # return "The result of the product B1."
        return "esta regresando de aqui -> ConcreteProductB1"

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.

    La variante, Producto B1, solo puede funcionar correctamente con la variante,
    Producto A1. Sin embargo, acepta cualquier instancia de AbstractProductA como un
    argumento.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        print("ejecutara la funcion a")
        result = collaborator.useful_function_a()
        return f"El resultado de la colaboración del B1 con el ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.

        La variante, Producto B2, solo puede funcionar correctamente con el
        variante, Producto A2. Sin embargo, acepta cualquier instancia de
        AbstractProductA como argumento.
        """
        result = collaborator.useful_function_a()
        return f"El resultado de la B2 colaborando con la ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.

    El código de cliente funciona con fábricas y productos solo a través de resumen.
    tipos: AbstractFactory y AbstractProduct. Esto le permite pasar cualquier fábrica
    o subclase de producto al código del cliente sin romperlo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    El código del cliente puede funcionar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Prueba de código de cliente con el primer tipo de fábrica:")
    client_code(ConcreteFactory1())

    print("\n")

    #print("Cliente: probando el mismo código de cliente con el segundo tipo de fábrica:")
    #client_code(ConcreteFactory2())
