- **Superclass/Baseclass/Parentclass:** These terms refer to a class that is being inherited from. It serves as the primary class from which attributes and methods are inherited by subclasses.

- **Subclass:** A subclass is a class that inherits from a superclass. It can access attributes and methods from its superclass and may also have its own unique attributes and methods.

- **Listing attributes and methods:** The `dir()` function can be used to list attributes and methods of a class or an instance. For example:
  ```python
  class MyClass:
      def method(self):
          pass

  print(dir(MyClass))
  ```

- **New attributes for instances:** Instances in Python can have new attributes assigned at any time. For instance:
  ```python
  class MyClass:
      pass

  obj = MyClass()
  obj.new_attribute = "value"
  ```

- **Inheriting from a class:** To inherit from a class, include the superclass name in parentheses when defining the subclass:
  ```python
  class Superclass:
      pass

  class Subclass(Superclass):
      pass
  ```

- **Multiple base classes:** To define a class with multiple base classes, list them in parentheses separated by commas:
  ```python
  class Base1:
      pass

  class Base2:
      pass

  class MyClass(Base1, Base2):
      pass
  ```

- **Default class inheritance:** All classes implicitly inherit from the `object` class in Python.

- **Overriding methods or attributes:** To override a method or attribute from a superclass in a subclass, simply redefine it in the subclass with the same name.

- **Inherited attributes/methods:** Subclasses inherit all attributes and methods from their superclass, though they can also have their own unique attributes and methods.

- **Purpose of inheritance:** Inheritance promotes code reusability, enabling the creation of new classes that inherit characteristics from existing classes, reducing redundancy and promoting a hierarchical structure.

- **Built-in functions for inheritance:** 
  - `isinstance()` checks if an object is an instance of a particular class.
  - `issubclass()` checks if a class is a subclass of another class.
  - `type()` returns the type of an object.
  - `super()` is used to access methods from a superclass within a subclass.

These functions are handy for checking relationships between classes and instances and for managing inheritance hierarchies in Python.
