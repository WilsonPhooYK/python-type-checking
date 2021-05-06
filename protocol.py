"""Define your own protocol
"""
from typing_extensions import Protocol
from typing import Sized

class SizedCustom(Protocol):
  def __len__(self) -> int: ...
  
def len(obj: SizedCustom) -> int:
  return obj.__len__()

def len2(obj: Sized) -> int:
  return obj.__len__()