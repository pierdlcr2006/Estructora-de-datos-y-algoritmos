from linked_list.linked_list import LinkedList
from linked_list.utilities import merge_sorted_lists
from queue.queue import Queue


def main():
    # Prueba de LinkedList
    ll1 = LinkedList()
    ll1.insert_at_end(1)
    ll1.insert_at_end(3)
    ll1.insert_at_end(5)

    ll2 = LinkedList()
    ll2.insert_at_end(2)
    ll2.insert_at_end(4)
    ll2.insert_at_end(6)

    print("Lista enlazada 1:")
    ll1.display()

    print("Lista enlazada 2:")
    ll2.display()

    print("Lista fusionada:")
    merged = merge_sorted_lists(ll1, ll2)
    merged.display()

    # Prueba de Queue
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Cola actual:")
    q.display()
    q.dequeue()
    print("Cola después de eliminar un elemento:")
    q.display()


if __name__ == "__main__":
    main()
