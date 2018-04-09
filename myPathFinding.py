# Kyle Marcus Enriquez
# Python 3

# G       : our map with cells
# a       : starting x coordinate
# b       : starting y coordinate
# y       : ending x coordinate
# z       : ending y coordinate
# v       : list of visited cells
# row     : adjacent rows to check
# col     : adjacent columns to check


def findPath(G, a, b, y, z, v, row, col):
    # print("We are at [{0}][{1}]".format(a,b)) # For keeping track of where we are
    v[a][b] = True

    if a == y and b == z:
        global pathFound
        pathFound = True
        return
    for i in range(len(row)):
        if(0 <= a + row[i] < len(G) and                     # if adjacent cell is within 0 and (number of rows - 1)
                0 <= b + col[i] < len(G[0]) and             # if adjacent cell is within 0 and (number of cols - 1)
                v[a + row[i]][b + col[i]] is False and      # if cell is not yet visited
                G[a + row[i]][b + col[i]] == 0 and          # if cell is passable
                pathFound is False):                        # if we haven't already found a path (for early exit)
            findPath(G, a + row[i], b + col[i], y, z, v, row, col)


# SETTING UP
pathFound = False
def main():
    # This is our map, '0' means passable while anything else means not passable
    graph = [[0, 0, 0, 0, 0, 0],
             [0, 5, 5, 5, 0, 0],
             [0, 5, 0, 5, 0, 0]]

    # Our visited list
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]

    # Adjacent-rows-to-check list and adjacent-columns-to-check list
    rowToCheck = [-1, 0, 0, 1]
    colToCheck = [0, -1, 1, 0]

    # his is our function to find a path
    findPath(graph, 0, 5, 2, 2, visited, rowToCheck, colToCheck)

main()
print(pathFound)
