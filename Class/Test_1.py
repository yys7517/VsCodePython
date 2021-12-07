def solution( maze, start , end ) :
    qu = []
    visited = set()

    qu.append(start)
    visited.add(start)

    while qu: 
        # 큐에 처리할 경로가 남아 있으면 
        # print( 'qu = ', qu)
        p = qu.pop(0) # 현재까지 이동경로
        # print('이동경로 = ', p)
        v = p[-1] # 큐에 저장된 이동 경로의 마지막 문자가 처리해야 할 꼭짓점
        # print('v = ', v)
        if v == end: # 처리해야 할 꼭짓점이 도착점이면(목적지 도착!) 
            return p            
            # 지금까지의 전체 이동 경로를 돌려주고 종료 
        
        for x in maze[v]: 
            # print( maze[v] )
        # 대상 꼭짓점 v에 연결된 꼭짓점들 중에 
            if x not in visited: 
                # 아직 큐에 추가된 적이 없는 꼭짓점 x를 
                # 이동 경로에 새 꼭짓점으로 추가하여 큐에 저장하고 
                qu.append(p + x) 
                visited.add(x) # 방문 체크. 
               
        # 탐색을 마칠 때까지 도착점이 나오지 않으면 나갈 수 없는 미로임 
    return -1



maze = { 
    'a' : ['e'], 
    'b' : ['c','f'], 
    'c' : ['b','d'], 
    'd' : ['c'], 
    'e' : ['a','i'], 
    'f' : ['b','g','j'], 
    'g' : ['f','h'], 
    'h' : ['g','l'], 
    'i' : ['e','m'], 
    'j' : ['f','k','n'], 
    'k' : ['j','o'], 
    'l' : ['h','p'], 
    'm' : ['i','n'], 
    'n' : ['m','j'], 
    'o' : ['k'], 
    'p' : ['l'] 
    }
start = 'a'
end = 'p'

ret = solution(maze,start,end)
for i in ret :
    print(i,end='')