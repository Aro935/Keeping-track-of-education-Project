last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append([93, "visual arts"])

#print(gradebook)

full_gradebook = list(zip(last_semester_gradebook, gradebook))

print(full_gradebook)