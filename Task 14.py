def calculate_top_k_students(positive_feedback, negative_feedback, report, student_id, k):
    student_points = {i: 0 for i in student_id}

    for i in range(len(report)):
        for j in report[i].split():
            if j in positive_feedback:
                student_points[student_id[i]] += 3
            elif j in negative_feedback:
                student_points[student_id[i]] -= 1

    sorted_students = sorted(student_points.items(), key=lambda x: (x[1], x[0]), reverse=True)
    top_k_students = [student[0] for student in sorted_students[:k]]
    return top_k_students

pf = ["smart", "brilliant", "studious"]
nf = ["not"]
rep = ["this student is studious", "the student is smart"]
stud_id = [1, 2]
kth = 2

result = calculate_top_k_students(pf, nf, rep, stud_id, kth)
print(f"Top {kth} Students: {result}")
