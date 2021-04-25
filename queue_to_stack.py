"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue: ArrayQueue) -> ArrayStack:
    """Converts the given queue to a stack and returns it."""
    stack = ArrayStack()
    values = reversed([elem for elem in queue])
    for elem in values:
        stack.push(elem)
    return stack
