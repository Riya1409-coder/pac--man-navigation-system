from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation

    def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        n = len(self.navigator_maze)
        m = len(self.navigator_maze[0])
        path = Stack()
        
        visited = []
        for i in range(n):
            vis = []
            for j in range(m):
                vis.append(False)
            visited.append(vis)

        cur = start
        path.push(cur)
        visited[cur[0]][cur[1]] = True
        if self.navigator_maze[start[0]][start[1]] == 1:
            raise PathNotFoundException
        if self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException
        while (True):
            cur = path.top()
            if cur == end:
                break
            if (cur[0] + 1 < n and not visited[cur[0]+1][cur[1]] and self.navigator_maze[cur[0] + 1][cur[1]] == 0):
                path.push((cur[0] + 1, cur[1]))
                visited[cur[0]+1][cur[1]] = True
                continue
            if (cur[1] + 1 < m and not visited[cur[0]][cur[1] + 1] and self.navigator_maze[cur[0]][cur[1] + 1] == 0):
                path.push((cur[0], cur[1] + 1))
                visited[cur[0]][cur[1] + 1] = True
                continue
            if (cur[0] > 0 and not visited[cur[0]-1][cur[1]] and self.navigator_maze[cur[0] - 1][cur[1]] == 0):
                path.push((cur[0] - 1, cur[1]))
                visited[cur[0]-1][cur[1]] = True
                continue
            if (cur[1] > 0 and not visited[cur[0]][cur[1]-1] and self.navigator_maze[cur[0]][cur[1] - 1] == 0):
                path.push((cur[0], cur[1] - 1))
                visited[cur[0]][cur[1]-1] = True
                continue
            path.pop()
            if (path.is_empty()):
                break
            
        if (not path.is_empty()):
            print(path.get())
            return path.get()
        else:
            raise PathNotFoundException