from abc import abstractmethod, ABC
from datetime import date
from typing import TypeVar, Type

TAnimal = TypeVar("TAnimal", bound="Animal")

class Animal(ABC):
  @abstractmethod
  def __init__(self, name: str, birthday: date) -> None:
    self.name = name
    self.birthday = birthday
    
  @classmethod
  def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
    return cls(name, date.today())
  
  def twin(self: TAnimal, name: str) -> TAnimal:
    cls = self.__class__
    return cls(name, self.birthday)
  
class Dog(Animal):
  def bark(self) -> None:
    print(f"{self.name} says wolf!")
    
fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
# Cannot instantiate base class
# animal = Animal("Animal", date.today())
fido.bark()
pluto.bark()

