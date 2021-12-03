def solution (mid_scores, final_scores) :
    diff = []
    for i in range( 0, len(mid_scores) ) :
        diff.append( final_scores[i] - mid_scores[i] )
    # print( diff )
    result = []
    result.append( max(diff) )
    result.append( min(diff) )
    return result


mid_scores = [20,50,40]
final_scores = [10,50,70]
ret = solution(mid_scores,final_scores)
print( ret )