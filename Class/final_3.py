def solution(g,start,end) :
    queue = []
    route = ''                  # 경로를 담는 문자열
    visited = set()             # 방문했는가 ?

    queue.append(start)         # 시작점 이동경로에 추가.
    visited.add(start)          # 방문

    while queue :               # 모든 이동경로의 경우의 수를 소비할 때 까지 반복한다.
        route = queue.pop()     # 어떤 한 경우의 이동경로 값.
        curr = route[-1]        # 이동경로의 마지막 문자값이 처리해야 될 지점.

        if curr == end :        # 현재 처리해야될 지점이 마지막 지점이면 미로를 탈출한 것이다.
            return route        # 이동경로 값을 반환하고 함수를 종료한다.

        else :                                       # 마지막 지점이 아니라면
            for next_node in g[curr] :               # 현재지점과 인접한 노드들 리스트를 가져와서 차례대로 방문. 
                if next_node not in visited :           # 그 노드가 방문되지 않았을 시에는
                    queue.append( route + next_node )   # 그 노드를 방문하는 경우의 수를 queue에 삽입.  현재까지 이동경로에 그 인접노드 문자를 연결하여 이동경로 경우의 수를 만든다.
                    # queue에는 만들어질 수 있는 모든 이동경로의 값이 들어간다.
                    visited.add( next_node )            # 그 노드를 방문 처리.

    
        # 따라서 위 while문은 어떤 한 이동경로의 경우의 수 마지막 지점이 end값과 같을 때는 이동경로 값을 반환하고.

        # 그것이 아닐 때, 그리고 queue의 모든 경우의 수를 소비했을 때, 미로를 탈출하지 못하였으므로 아무 값도 반환하지 않는다.
    return ""


# 미로 정보.
g = { 
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
start = 'a'     # 시작점 a
end = 'p'       # 도착점 p

ret = solution(g,start,end)     # solution 함수에 미로정보, 시작점, 도착점 전달.
                                # ret에는 반환된 이동경로 값이 저장된다.

print( '미로경로는 = ',ret )