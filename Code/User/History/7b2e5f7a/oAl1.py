pythonfrom collections import deque

def solution():
    # Read grid dimensions height (H) and width (W)
    H, W = map(int, input().split())
    
    # Read target number of gray houses (N)
    N = int(input())
    
    # Read the number of initial gray houses (M)
    M = int(input())
    
    # Read the coordinates of the initial gray houses
    initial_houses = []
    for _ in range(M):
        x, y = map(int, input().split())
        initial_houses.append((x, y))
        
    # Initialize BFS queue and visited set
    queue = deque()
    visited = set()
    
    for r, c in initial_houses:
        # Ensure the initial house coordinates fall within the grid boundaries
        if 1 <= r <= H and 1 <= c <= W:
            if (r, c) not in visited:
                visited.add((r, c))
                queue.append((r, c))
                
    # Track the current elapsed months and total gray houses
    months = 0
    total_gray = len(visited)
    
    # Edge case: If the initial houses already satisfy the target N
    if total_gray >= N:
        print(0)
        return

    # Directions for moving vertically and horizontally (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Run the BFS wave by wave (month by month)
    while queue:
        months += 1
        # Process only the houses belonging to the current month's wave
        houses_this_month = len(queue)
        
        for _ in range(houses_this_month):
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the neighboring house is within bounds and not yet painted
                if 1 <= nr <= H and 1 <= nc <= W and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    total_gray += 1
                    
        # Check if we have painted enough houses at the end of this month
        if total_gray >= N:
            print(months)
            return
            
    # If the queue runs out and we still haven't hit N, it's impossible (N > H * W)
    print(months)

# Run the program
if __name__ == "__main__":
    solution()
