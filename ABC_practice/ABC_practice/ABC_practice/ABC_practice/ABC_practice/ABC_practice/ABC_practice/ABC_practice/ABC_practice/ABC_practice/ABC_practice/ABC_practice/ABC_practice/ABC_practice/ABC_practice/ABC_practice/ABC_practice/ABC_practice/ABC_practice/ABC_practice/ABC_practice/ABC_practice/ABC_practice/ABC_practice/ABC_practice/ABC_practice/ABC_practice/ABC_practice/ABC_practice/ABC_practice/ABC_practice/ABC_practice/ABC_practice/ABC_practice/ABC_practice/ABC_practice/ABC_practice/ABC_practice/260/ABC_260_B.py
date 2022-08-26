"""
Input variables N: the number of students, 
X: those who can pass tests by math scores, 
Y: those who can pass tests by English scores, 
Z: those who can pass tests by the sum of math and English scores.
"""
N,X,Y,Z = map(int,input().split())

"""
Input students' scores 
"""
A = list(map(int,input().split()))

B = list(map(int,input().split()))


"""
create the list of math and English scores.re
"""
math_english = [[0,0] for i in range(N)]

"""
create the list of students who pass the exam.
"""
congratulations = []

"""
input scores of math and English, and student numbers into the list "math_english."
"""
for i in range(N):
    math_english[i] = [i+1,A[i],B[i]]

"""
sort the list "math_english" by math scores
"""
math_english.sort(key=lambda x:(x[1],-x[0]),reverse = True)

for i in range(X):
    congratulations.append(math_english[i][0])

"""
define the new list "math_english_new" as the rest of the list "math_english"
"""
math_english_new = math_english[X:]
# print(math_english_new)
"""
sort the list "math_english_new by English scores"
"""
math_english_new.sort(key=lambda x:(x[2],-x[0]),reverse = True)
"""
add the list "congratulations" from higher English score students.
"""
for i in range(Y):
    congratulations.append(math_english_new[i][0])

"""
define the new list "math_english_new2" as the rest of the list "math_english_new"
"""
math_english_new2 = math_english_new[Y:]
# print(math_english_new2)

for i in range(len(math_english_new2)):
    math_english_new2[i].append(math_english_new2[i][1] + math_english_new2[i][2])

math_english_new2.sort(key=lambda x:(x[3],-x[0]),reverse = True)

# print(math_english_new2)

for i in range(Z):
    congratulations.append(math_english_new2[i][0])

congratulations.sort()

for i in congratulations:
    print(i)

