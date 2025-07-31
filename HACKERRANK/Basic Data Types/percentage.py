if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=[]
    result=0
    if query_name in student_marks:
        marks=student_marks[query_name]
        for i in range(0,len(marks)):
            result+=marks[i]
        avg_marks=result/len(marks)
        print(f"{avg_marks:.2f}")