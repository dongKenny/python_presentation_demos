from dataclasses import dataclass, field
from typing import List


# Frozen = True makes it immutable, therefore it writes the hash function
# Order = True makes the class implement ordering methods like total_ordering (eq, lt, gt, etc.)
@dataclass(frozen=True, order=True)
class Book:
    title: str = ""
    year: int = 2021
    author: str = ""
    chapters: List[str] = field(default_factory=list, compare=False, hash=False, repr=False)
    # Chapters is a mutable type, so it should be made with the field factory
    # We also do not include it in comparison functions, hashing, or in the repr
