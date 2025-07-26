def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            el = board[i][j]

            if '.' in el:
                continue
            #row validity
            if el in rows[i]:
                return False
            rows[i].add(el)
            #col validity
            if el in cols[j]:
                return False
            cols[j].add(el)
            #box validity
            box_index = (i//3)*3 + (j//3)
            if el in boxes[box_index]:
                return False
            boxes[box_index].add(el)
    return True
