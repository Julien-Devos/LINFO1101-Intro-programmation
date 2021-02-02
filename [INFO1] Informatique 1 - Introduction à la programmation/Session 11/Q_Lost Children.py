try:
    curr = first_child
    ok = curr.is_next_valid()
    curr = curr.next_child()
    while not ok or curr != first_child:
        ok = curr.is_next_valid()
        curr = curr.next_child()
except AttributeError:
    ok = False
return ok