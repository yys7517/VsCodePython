# 백준 브론즈 2 - 진짜 공간
N = int(input())
FileSizelist = list( map (int,input().split()))
ClusterSize = int(input())
# print(FileSizelist)           # 리스트 형태로 잘 들어갔는지 출력하여 확인.

ClusterSum = 0
for i in FileSizelist :
    if ( i % ClusterSize == 0 ) : ## 파일 크기가 0일때 또는 나누어질 때..
        ClusterSum += ( i // ClusterSize ) * ClusterSize
    else :
        ClusterSum += ( i // ClusterSize + 1 ) * ClusterSize
    
print(ClusterSum)
