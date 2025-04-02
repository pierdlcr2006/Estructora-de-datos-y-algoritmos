from .linked_list import LinkedList

# Función independiente para fusionar listas ordenadas
def merge_sorted_lists(list1, list2):
    merged = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.get_data() <= current2.get_data():
            merged.insert_at_end(current1.get_data())
            current1 = current1.get_next()
        else:
            merged.insert_at_end(current2.get_data())
            current2 = current2.get_next()

    while current1:
        merged.insert_at_end(current1.get_data())
        current1 = current1.get_next()

    while current2:
        merged.insert_at_end(current2.get_data())
        current2 = current2.get_next()

    return merged
