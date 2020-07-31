pushup_score_table = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17,
        17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17,
     18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18,
     18, 18, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18,
     18, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18,
     18, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18,
     19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19,
     19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19,
     20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20,
     20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20,
     20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20,
     21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21,
     21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21,
     21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
    [0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21,
     21, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
]
