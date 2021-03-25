from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

Number = Union[int, Decimal]


@dataclass
class Mean:
    value: Optional[Decimal] = None
    count: int = 0
    def append(self, value: Number):
        value = Decimal(value)
        old_count = self.count
        self.count += 1
        if self.value is None:
            self.value = value
        else:
            old_value = Decimal(self.value)
            self.value = ((old_value * old_count) + value) / self.count

mean = Mean()
mean.append(10)
mean.append(20)
mean.append(5)

assert mean.value == ((Decimal(10) + 20 + 5) / 3)
