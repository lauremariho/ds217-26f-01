measurements = [18, 21, 24, 19]
review_threshold_text = "20"

review_threshold = int(review_threshold_text)
total = 0
review_count = 0

for measurement in measurements:
    total += measurement  
    
    if measurement >= review_threshold:
        print(f"Measurement: {measurement} review")
        review_count += 1  
    else:
        print(f"Measurement: {measurement} within range")

count = len(measurements)
average = total / count if count > 0 else 0

print(f"Count: {count}")
print(f"Total: {total}")
print(f"Mean: {average:.1f}")
print(f"Review count: {review_count}")