from dataclasses import dataclass
from typing import Generator, Iterable, List, Sequence

@dataclass(frozen=True)
class BubbleSortState:
    data: Sequence[int]
    index_a: int
    index_b: int
    swapped: bool
    pass_index: int

def bubble_sort_steps(values: Iterable[int]) -> Generator[BubbleSortState, None, List[int]]:
    data = list(values)
    n = len(data)

    if n == 0:
        return data

    for pass_index in range(n - 1):
        swapped_in_pass = False

        for idx in range(n - pass_index - 1):
            swapped = False

            if data[idx] > data[idx + 1]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
                swapped = True
                swapped_in_pass = True

            yield BubbleSortState(
                data=tuple(data),
                index_a=idx,
                index_b=idx + 1,
                swapped=swapped,
                pass_index=pass_index,
            )

        if not swapped_in_pass:
            break

    return data

def bubble_sort_trace(values: Iterable[int]):
    states = list(bubble_sort_steps(values))

    if states:
        sorted_values = list(states[-1].data)
    else:
        sorted_values = list(values)

    return states, sorted_values
