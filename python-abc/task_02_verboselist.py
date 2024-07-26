#!/usr/bin/env python3
class VerboseList(list):
    """Class Verboselist"""

    def append(self, item):
        """Append object to the list"""
        super().append(item)
        print("Appended [{}] to the list.".format(item))

    def extend(self, item):
        """Extend list with the items"""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove object from the list"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from the list"""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
