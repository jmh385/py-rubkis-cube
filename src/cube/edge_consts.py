from typing import Tuple, Dict, List

sides_to_bottom_middle: List[Tuple[int, int]] = [
    (1, 5),
    (2, 1),
    (3, 3),
    (4, 7)
]

sides_and_bottom_middle_to_side_5: Dict[tuple[int, int], int] = {
    (1, 5): 3,
    (2, 1): 1,
    (3, 3): 5,
    (4, 7): 7
}

edge_mappings: Dict[tuple[int, int], tuple[int, int]] = {
    (0, 1): (2, 7),
    (0, 3): (3, 5),
    (0, 5): (1, 3),
    (0, 7): (4, 1),

    (1, 1): (2, 5),
    (1, 3): (0, 5),
    (1, 5): (5, 3),
    (1, 7): (4, 5),

    (2, 1): (5, 1),
    (2, 3): (3, 1),
    (2, 5): (1, 1),
    (2, 7): (0, 1),

    (3, 1): (2, 3),
    (3, 3): (5, 5),
    (3, 5): (0, 3),
    (3, 7): (4, 3),

    (4, 1): (0, 7),
    (4, 3): (3, 7),
    (4, 5): (1, 7),
    (4, 7): (5, 7),

    (5, 1): (2, 1),
    (5, 3): (1, 5),
    (5, 5): (3, 3),
    (5, 7): (4, 7)
}

edges_with_white: List[tuple[tuple[int, int], tuple[int, int]]] = [(edge_face_1, edge_face_2) for
                                                                   edge_face_1, edge_face_2 in edge_mappings.items() if
                                                                   edge_face_2[0] == 0]
