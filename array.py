#Дан массив размера N и целые числа K и L (1≤K≤L≤N).
# Найти сумму элементов массива с номерами от K до L включительно.
import random

N = random.randint(10, 20)  # Дано случайное число N от 10 по 20
L = random.randrange(0, N)  # Дано случайное число L  от 0 по N
K = random.randint(0, L)  # Дано случайное число К  от 0 по L
#N = 10
print("N = ", N)
print("L = ", L)
print("K = ", K)

A = [random.randrange(1, 20) for i in range(N)]  # Присвоить к числу А, значением которого является случайное число от 1 по 20
                                                # для i выбрать случайное i\
print("Initial:")
print(A)

s = 0
for i in range(K, L+1):
    s += A[i]
    print(i, ":", A[i])
print("Sum = ", s)

print()
print(A[K:L+1])
print("Sum = ", sum(A[K:L+1]))