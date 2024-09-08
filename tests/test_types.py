from drive_events.types import BaseEvent, EventGroup


def test_node_hash():
    def mock_a():
        return 1

    def mock_b():
        return 2

    n1 = BaseEvent(mock_a)
    n2 = BaseEvent(mock_a)
    n3 = BaseEvent(mock_b)
    assert n1.id == n2.id
    assert n1.id != n3.id


def test_node_debug_print():
    def mock_a():
        return 1

    def mock_b():
        return 2

    n1 = BaseEvent(mock_a)
    g1 = EventGroup("1", [n1])
    n2 = BaseEvent(mock_a, parent_groups={g1.hash(): g1})
    g2 = EventGroup("2", [n1, n2])
    n3 = BaseEvent(mock_b, parent_groups={g1.hash(): g1, g2.hash(): g2})

    print(n1, n1.debug_string())
    print(n2, n2.debug_string())
    print(n3, n3.debug_string())
