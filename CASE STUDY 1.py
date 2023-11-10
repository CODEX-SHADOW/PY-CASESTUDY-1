# Initialize an empty dictionary to store student information.
students = {}

# Get the number of students from the user.
num_students = int(input("Enter the number of students: "))

# Input student names and scores.
for i in range(num_students):
    student_name = input(f"Enter the name of student {i + 1}: ")
    scores = input(f"Enter the scores for {student_name} (comma-separated): ").split(',')
    
    # Convert the scores to a list of integers.
    scores = [int(score) for score in scores]
    
    # Calculate the average score for the student.
    average_score = sum(scores) / len(scores)
    
    # Store the student information in the dictionary.
    students[student_name] = {'scores': scores, 'average_score': average_score}

# Find the top-scoring student.
top_student = max(students, key=lambda student: students[student]['average_score'])

# Display the results.
print("\nStudent Information:")
for student, data in students.items():
    print(f"{student}: Scores - {data['scores']}, Average Score - {data['average_score']}")

print(f"\nTop-Scoring Student: {top_student} with an average score of {students[top_student]['average_score']}")
