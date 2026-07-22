def calculate_grade(marks):
    if marks >= 90:
        return "A Grade"
    elif marks >= 75:
        return "B Grade"
    elif marks >= 60:
        return "C Grade"
    else:
        return "F Grade"
if __name__ == "__main__":
    marks = 82
    print("Marks:", marks)
    print("Grade:", calculate_grade(marks))
