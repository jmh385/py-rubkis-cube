import torch

from cube.cube import Cube
from ml.data_analysis.analyze_dataset import Multiclass
from ml.data_collection.create_dataset import colour_type_to_number

weights = torch.load("../../builds/best_weights.txt")
print("loaded weights")
model = Multiclass()
model.eval().cuda()
model.load_state_dict(weights)

def run_ml_solver(cube: Cube):
    cube_sides_integers = [colour_type_to_number[face] for side in cube.sides for face in side]
    x = torch.tensor(cube_sides_integers, dtype=torch.float32).cuda()
    result = model(x)
    print(result)


cube1 = Cube()
cube1.randomise()
run_ml_solver(cube1)