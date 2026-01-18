def breaking_records(scores):
    result = [0, 0]
    min_score = scores[0]
    max_score = scores[0]
    
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            result[0] += 1
        elif score < min_score:
            min_score = score
            result[1] += 1
    
    return result