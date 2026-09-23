measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.
print("TODO: complete the measurement summary")
review_threshold = int(review_threshold_text)
total = 0
review_count = 0
for measurement in measurements:
    total += measurement
    if measurement > review_threshold:
        review_count += 1
average = total / len(measurements)
print(f"Average measurement: {average:.2f}")
print(f"Number of measurements above threshold: {review_count}")
  