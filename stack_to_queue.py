"""
Stack to queue converter.
"""

from copy import deepcopy
from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def stack_to_queue(stack: ArrayStack) -> ArrayQueue:
    """Converts the given stack to a queue and returns it."""
    queue = ArrayQueue()
    stack_copy = deepcopy(stack)
    for _ in stack:
        queue.add(stack_copy.peek())
        stack_copy.pop()
    return queue
