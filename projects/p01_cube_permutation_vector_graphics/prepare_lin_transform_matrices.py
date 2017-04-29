import numpy as np


row_matrices = [
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ],
    [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, -1]
    ],
    [
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, -1]
    ],
    [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
    ],
    [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
    ]
]


col_matrices = [
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ],
        [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ],
    [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
]


lin_transform_matrices = {}
for row in range(8):
    for col in range(6):
        prod = np.dot(row_matrices[row], col_matrices[col])
        lin_transform_matrices[(row, col)] = prod.tolist()

print(lin_transform_matrices)

# result copied to tests.py
