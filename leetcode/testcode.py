# users_scores = {"Alice": 85.3, "Bob": -5, "Charlie": 50.2, "David": 120, "Eve": 75.3}

def process_user_scores(users_scores):
    valid_users = {}
    total_score = 0
    max_score = 0
    
    
    # Remove users with invalid scores (< 0 or > 100)
    for user, score in users_scores.items():
        # if score < 0 or score > 100:
        #     del users_scores[user]
        # else:
        if 0 <= score <= 100:
            valid_users[user] = score
            total_score += score
            if score > max_score:
                max_score = score

    if len(valid_users) == 0:
        return None, 0, 0
    
    # Award bonus points=5 to users with scores < 80, but cap at 80
    bonus_threshold = 80
    for user, score in valid_users.items():
        if score <= bonus_threshold:  
            valid_users[user] = min(score + 5, bonus_threshold) 
            # score = 72
            # score = 78
    
    # Calculate average of high scores (> 50)
    high_scores = []
    for score in valid_users.values():
        if score > 50:
            high_scores.append(score)
    if len(high_scores) == 0:
        average_score = -1
    else:
        average_score = sum(high_scores) / len(high_scores)

    return valid_users, average_score, max_score
users_scores = {"Alice": -5, "Bob": -5, "Charlie": -5, "David": -5, "Eve": -5}
print(process_user_scores(users_scores))