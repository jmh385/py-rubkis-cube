from typing import List, Tuple

corners_triples: List[List[Tuple[int, int]]] = [
    [(0, 0), (2, 6), (3, 2)],
    [(0, 2), (1, 0), (2, 8)],
    [(0, 6), (3, 8), (4, 0)],
    [(0, 8), (1, 6), (4, 2)],

    [(5, 0), (1, 2), (2, 2)],
    [(5, 6), (1, 8), (4, 8)],
    [(5, 8), (4, 6), (3, 6)],
    [(5, 2), (2, 0), (3, 0)]
]

white_corner_triples: List[List[Tuple[int, int]]] = [
    corner_triple for corner_triple in corners_triples if
    len([1 for side_index, _ in corner_triple if side_index == 0]) > 0
]

yellow_corner_triples: List[List[Tuple[int, int]]] = [
    corner_triple for corner_triple in corners_triples if
    len([1 for side_index, _ in corner_triple if side_index == 5]) > 0
]

magic_corner_bottom: List[Tuple[int, int]] = [
    (5, 2), (2, 0), (3, 0)
]

magic_corner_top: List[Tuple[int, int]] = [
    (3, 2), (2, 6), (0, 0)
]