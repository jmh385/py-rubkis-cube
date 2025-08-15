import csv
from typing import Dict

from common.color_type_enum import ColourType
from cube.cube import Cube
from solver.solve_cube import solve_cube

colour_type_to_number: Dict[ColourType, int] = {
    ColourType.red: 1,
    ColourType.white : 2,
    ColourType.green: 3,
    ColourType.blue : 4,
    ColourType.orange : 5,
    ColourType.yellow : 6
}

def create_dataset(data_points_count=50_000):
    cube = Cube()
    results = []
    fixtures = []
    for i in range(data_points_count):
        print(f"data set: {i}")
        cube.randomise()
        moves = solve_cube(cube, False)
        for move in moves:
            cube_state = [colour_type_to_number[face] for side in cube.sides for face in side]
            fixtures.append(cube_state)
            results.append([move.value])
            cube.movement_parser(move)
    return fixtures, results


def write_dataset():
    fixtures, results = create_dataset()
    print(results)
    with open("builds/fixtures.csv", "w", newline="") as fixtures_file:
        writer = csv.writer(fixtures_file)
        writer.writerows(fixtures)
    with open("builds/results.csv", "w", newline="") as results_file:
        writer = csv.writer(results_file)
        writer.writerows(results)

