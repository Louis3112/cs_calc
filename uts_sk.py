import os
import numpy as np
import matplotlib.pyplot as plt

rows = np.random.randint(1,9)
colls = np.random.randint(1,9)

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def func1() : 
    rowsfunc1, colsfunc1 = map(int, input("Enter size of matrix (rows cols): ").split())

    if rowsfunc1 < 2 or colsfunc1 < 2:
        print("Matrix size must be at least 2x2.")
        return  # Kembali jika ukuran tidak valid
    
    if rowsfunc1 != colsfunc1:
        print("Matrix must be square (rows == cols) to solve a system of linear equations.")
        return  # Kembali jika matriks bukan persegi

    matrix = []
    y = []

    print(f"Enter the elements for a {rowsfunc1}x{colsfunc1} matrix:")
    for i in range(rowsfunc1):
        while True:
            try:
                row = list(map(int, input(f"Enter row #{i+1}: ").split()))
                if len(row) != colls:
                    raise ValueError(f"Row must have exactly {colsfunc1} elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
    
    print("Enter elements for the vector (y):")
    for i in range(colsfunc1):
        while True:
            try:
                el = int(input(f"Enter element #{i+1}: "))
                y.append(el)
                break
            except ValueError:
                print("Please enter a valid integer.")

    A = np.array(matrix)
    y = np.array(y)

    # Periksa apakah determinan matriks adalah nol
    if np.linalg.det(A) == 0:
        print("The matrix is singular and cannot be solved.")
        return

    # Menyelesaikan sistem persamaan linear
    x = np.linalg.solve(A, y)
    print("\nSolution (x):")
    print(x)

def func2() :
    while True:
        print()
        print("\nMatrix Properties")
        print("1. Types of matrices")
        print("2. Behavior of matrix")
        print("3. Exit")
        try:
            choice = int(input("> "))
        except ValueError:
            print("\nInvalid input, choose from 1-2!")
            enter()
            continue
        
        if choice == 1:
            func2_1()
        elif choice == 2:
            func2_2()
        elif choice == 3:
            break
        else:
            print("\nInvalid input, choose from 1-2!")
            enter()
            continue
        
def func2_1():
    while True:    
        print("\nThere are a lot of types of matrices")
        print("1. Zero Matrix")
        print("2. Square Matrix")
        print("3. Rectangular Matrix")
        print("4. Diagonal Matrix")
        print("5. Identity Matrix")
        print("6. Scalar Matrix")
        print("7. Row Matrix")
        print("8. Column Matrix")
        print("7. Exit")
        print("Choose one to see the example")

        try:
            choice = int(input("> "))
        except ValueError:
            print("\nInvalid input, choose from 1-2!")
            enter()
            continue
        
        if choice == 1:
            print("\nZero Matrix or Null Matrix is a matrix with all its elements")
            print("having a VALUE of ZERO.")
            
            zeroMatrix = np.zeros((rows,colls))
            print("\n", zeroMatrix)
            enter()

        elif choice == 2:
            print("\nSquare Matrix is a matrix where the lengths")
            print("of row and the columns ARE the SAME.")

            squareMatrix = np.random.randint(9, size=(4,4))
            print("\n", squareMatrix)
            enter()

        elif choice == 3:
            print("\nRectangular Matrix is a matrix where the lengths")
            print("of row and the column are NOT the SAME.")

            rectangularMatrix = np.random.randint(9, size=(rows,colls))
            print("\n", rectangularMatrix)
            enter()

        elif choice == 4:
            print("\nDiagonal Matrix is a square matrix with the elements")
            print("on the MAIN DIAGONAL having real values while the others are ZERO")

            diagonalMatrix = np.diag([np.random.randint(1,9),np.random.randint(1,9),np.random.randint(1,9)])
            print("\n", diagonalMatrix)
            enter()
        
        elif choice == 5:
            print("\nIdentity Matrix is a square matrix with the elements")
            print("on the MAIN DIAGONAL having a value of '1' while the others are ZERO")

            identityMatrix = np.eye(4)
            print("\n", identityMatrix)
            enter()
        
        elif choice == 6:
            print("\nScalar Matrix is a square matrix with the elements")
            print("on the MAIN DIAGONAL having the same values while the others are ZERO")

            scalarMatrix = np.eye(4) * np.random.randint(1,9)
            print("\n", scalarMatrix)
            enter()
        
        elif choice == 7:
            print("\nRow Matrix is a matrix that only consist of one row")

            rowMatrix = np.array([np.random.randint(1,9), np.random.randint(1,9), np.random.randint(1,9)])
            print("\n", rowMatrix)
            enter()
        
        elif choice == 8:
            print("\nColumn Matrix is a matrix that only consist of one column")

            columnMatrix = np.array([[np.random.randint(1,9)], [np.random.randint(1,9)], [np.random.randint(1,9)]])
            print("\n", columnMatrix)
            enter()

        elif choice == 9:
            break

        else:  
            print("\nInvalid choice! Please choose from 1-9.")
            enter()
            continue

def func2_2():
    A = np.array([[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)], [np.random.randint(1,9),np.random.randint(1,9),np.random.randint(1,9)],[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)]])
    B = np.array([[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)], [np.random.randint(1,9),np.random.randint(1,9),np.random.randint(1,9)],[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)]])
    C = np.array([[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)], [np.random.randint(1,9),np.random.randint(1,9),np.random.randint(1,9)],[np.random.randint(1,9), np.random.randint(1,9),np.random.randint(1,9)]])
    k = np.random.randint(1,5)
    l = np.random.randint(1,5)

    while True:
        print("\nMatrix has a lot of behavior")
        print("Suppose A,B,C are matrix and k and l are scalar")
        print("1. A + B = B + A\t\tCommutative Addition")
        print("2. A + (B + C) = (A + B) + C\tAssociative Addition")
        print("3. k * (A + B) = kA + kB\tDistributive Multiplication With Scalar")
        print("4. (k+l) A = kA + lA\t\tDistributive Multiplication With Scalar")
        print("5. (kl) A = k(lA)\t\tAssociative Multiplication With Scalar")
        print("6. k(A * B) = kA(B) = A(kB)\tDistributive Multiplication With Scalar")
        print("7. A(BC) = (AB)C\t\tAssociative Multiplication")
        print("8. A(B + C) = AB + AC\t\tDistributive Addition")
        print("9. (A + B)C = AC + BC\t\tDistributive Addition")
        print("10. A * B != B * A\t\tNot Commutative Multiplication")
        print("11. If A * B = A * C, does not mean B = C ")
        print("12. If A * B = 0, it's either A = 0 and B = 0")
        print("                  or A != 0 and B != 0")
        print("13. Exit")
        print("Choose one to see the example")

        try:
            choice = int(input("> "))
        except ValueError:
            print("\nInvalid input, choose from 1-2!")
            enter()
            continue

        if choice == 1:
            print("\n1. A + B = B + A\t\tCommutative Addition")
            print("\nA + B")
            print("\n",A), print("\n+ "), print("\n",B)
            print("\n= "), print("\n",A + B)

            print("\nwhile B + A")
            print("\n",B), print("\n+ "), print("\n",A)
            print("\n= "), print("\n",B + A)

            print("\nTherefore, A + B = B + A is TRUE")
            enter()

        elif choice == 2:
            print("\n2. A + (B + C) = (A + B) + C\tAssociative Addition")
            print("\nA + (B + C)")
            print("\n",A), print("\n+ ( "), print("\n",B), print("\n+ "), print("\n",C), print("\n)")
            print("\n= "), print("\n",A + (B + C))

            print("\nwhile (A + B) + C")
            print("\n( "), print("\n",A), print("\n+ "), print("\n",B), print("\n)"), print("\n+ "),print("\n",C), 
            print("\n= "), print("\n",(A + B) + C)

            print("\nTherefore, A + (B + C) = (A + B) + C is TRUE")
            enter()

        elif choice == 3:
            print("\n3. k * (A + B) = kA + kB\tDistributive Multiplication With Scalar")
            print("\nk * (A + B)")
            print("\n",k," *"), print("\n( "), print("\n",A), print("\n+ "), print("\n",B), print("\n )")
            print("\n= "), print("\n",k * (A + B))

            print("\nwhile kA + kB")
            print("\n",k," *"), print("\n",A), print("\n+ "), print("\n",k," *"), print("\n",B),
            print("\n= "), print("\n",k*A + k*B)

            print("\nTherefore, k * (A + B) = kA + kB is TRUE")
            enter()

        elif choice == 4:
            print("\n4. (k+l) A = kA + lA\t\tDistributive Multiplication With Scalar")
            print("\n(k+l) A")
            print("\n(",k," + ",l,")"), print("\n* "), print("\n",A)
            print("\n= "), print("\n",(k+l) * A)

            print("\nwhile kA + lA")
            print("\n",k," *"), print("\n",A), print("\n+ "), print("\n",l," *"), print("\n",A),
            print("\n= "), print("\n",k*A + l*A)

            print("\nTherefore, (k+l) A = kA + lA is TRUE")
            enter()

        elif choice == 5:
            print("\n5. (kl) A = k(lA)\t\t\tAssociative Multiplication With Scalar")
            print("\n(kl) A")
            print("\n(",k," * ",l,")"), print("\n",A)
            print("\n= "), print("\n",(k * l) * A)

            print("\nwhile k(lA)")
            print("\n",k," *"), print("\n(",l," *"), print("\n",A), print("\n)") 
            print("\n= "), print("\n",k*(l*A))

            print("\nTherefore, (kl) A = k(lA) is TRUE")
            enter()
        
        elif choice == 6:
            print("\n6. k(A * B) = (kA) * B = A * (kB)\tDistributive Multiplication With Scalar")
            print("\nk(A * B)")
            print("\n",k," * "), print("\n("), print("\n",A), print("\n* "), print("\n",B)
            print("\n= "), print("\n",k * np.dot(A, B))

            print("\nwhile (kA) * B")
            print("\n(",k," * "), print("\n",A), print("\n)"), print("\n* "), print("\n",B)
            print("\n= "), print("\n",np.dot(k * A, B))

            print("\nwhile A * (kB)")
            print("\n",A), print("\n*"), print("\n("), print("\n(",k," * "), print("\n",B), print("\n)")
            print("\n= "), print("\n",np.dot(A, k * B))
            print("\nTherefore, k(A * B) = (kA) * B = A * (kB) is TRUE")
            enter()

        elif choice == 7:
            print("\n7. A(BC) = (AB)C\t\tAssociative Multiplication")
            print("\nA(BC)")
            print("\n",A), print("\n*"), print("\n("), print("\n",B), print("\n* "), print  ("\n",C), print("\n)")
            print("\n= "), print("\n",np.dot(A, np.dot(B, C)))

            print("\nwhile (AB)C")
            print("\n("), print("\n",A), print("\n*"), print("\n",B), print("\n)"), print("\n* "),print("\n",C)
            print("\n= "), print("\n",np.dot(np.dot(A, B), C))
            print("\nTherefore, A(BC) = (AB)C is TRUE")
            enter()

        elif choice == 8:
            print("\n8. A(B + C) = AB + AC\t\tDistributive Addition")
            print("\nA(B+C)")
            print("\n",A), print("\n*"), print("\n("), print("\n",B), print("\n+ "), print("\n",C), print("\n)")
            print("\n= "), print("\n",np.dot(A, B + C))

            print("\nwhile AB + AC")
            print("\n",A), print("\n*"), print("\n",B), print("\n+"), print("\n",A), print("\n*"), print("\n",C)
            print("\n= "), print("\n",np.dot(A, B) + np.dot(A, C))
            print("\nTherefore, A(B+C) = AB + AC is TRUE")
            enter()

        elif choice == 9:
            print("\n9. (A + B)C = AC + BC\t\tDistributive Addition")
            print("\n(A+B)C")
            print("\n("), print("\n",A), print("\n+"), print("\n",B), print("\n)"), print("\n* "), print("\n",C), 
            print("\n= "), print("\n",np.dot(A + B, C))

            print("\nwhile AC + BC")
            print("\n",A), print("\n*"), print("\n",C), print("\n+"), print("\n",B), print("\n*"), print("\n",C)
            print("\n= "), print("\n",np.dot(A, C) + np.dot(B, C))
            print("\nTherefore, (A+B)C = AC + BC is TRUE")
            enter()

        elif choice == 10:
            print("\n10. A * B != B * A\t\tNot Commutative Multiplication")
            print("\nA * B")
            print("\n",A), print("\n*"), print("\n",B)
            print("\n= "), print("\n",np.dot(A, B))

            print("\nwhile B * A")
            print("\n",B), print("\n*"), print("\n",A)
            print("\n= "), print("\n",np.dot(B, A))
            print("\nSince the results are different")
            print("Therefore, A * B != B * A is TRUE")
            enter()

        elif choice == 11:
            print("11. If A * B = A * C, does not mean B = C ")
            AKhusus = np.array([[0, 100], [0, 0]])
            BKhusus = np.array([[-6, 28], [0, 0]])
            CKhusus = np.array([[48, -19], [0, 0]])

            print("\nA * B")
            print("\n",AKhusus), print("\n*"), print("\n",BKhusus)
            print("\n= "), print("\n",np.dot(AKhusus, BKhusus))

            print("\nA * C")
            print("\n",AKhusus), print("\n*"), print("\n",CKhusus)
            print("\n= "), print("\n",np.dot(AKhusus, CKhusus))

            print("\nEven the results are same, but B != C")
            print("Therefore, if A * B = A * C, does not mean B = C is TRUE")
            enter()

        elif choice == 12:
            print("12. If A * B = 0, it's either A = 0 and B = 0")
            print("                  or A != 0 and B != 0")
            AKhusus = np.array([[1, 2], [2, 4]])
            BKhusus = np.array([[6, -4], [-3, 2]])

            print("\nSuppose A = 0 * B = 0")
            print(np.array([[0, 0], [0, 0]])), print("\n*")
            print(np.array([[0, 0], [0, 0]]))

            print("\nBut if A != 0 * B != 0")
            print("\n",AKhusus), print("\n*"), print("\n",BKhusus)
            print("\n= "), print("\n",np.dot(AKhusus, BKhusus))

            print("\nTherefore, if A * B = 0, it's either A = 0 and B = 0")
            print("                  or A != 0 and B != 0")
            enter()
        
        elif choice == 13:
            break

        else:  
            print("\nInvalid choice! Please choose from 1-13.")
            enter()
            continue

def inverse_matrix(matrix_el):
    A = np.array(matrix_el, dtype=np.float64)

    n = A.shape[0]

    print("n: ", n)

    if n != A.shape[1]:
        raise ValueError("Matrix must be square")
    
    augmented = np.column_stack((A, np.eye(n)))

    for i in range(n):
        max_element = abs(augmented[i:, i]).argmax() + i

        if max_element != i:
            augmented[[i, max_element]] = augmented[[max_element, i]]
            
        if np.isclose(augmented[i, i], 0):
            raise ValueError("Matrix is not invertible")
        
        augmented[i] = augmented[i] / augmented[i, i]

        for j in range(n):
            if i != j:
                augmented[j] -= augmented[i] * augmented[j, i]

    return augmented[:, n:]

def lu_decomposition(A): 
    n = len(A)
    L = [[0]*n for _ in range(n)]
    U = [[0]*n for _ in range(n)]
    print("L: ", L)
    print("U: ", U)

    for i in range(n):
        for j in range(i, n): 
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    return L, U
    
def plot_linear_equation_point_slope(point, slope, x_range=(-10, 10)):
    x0, y0 = point
    
    x = np.linspace(x_range[0], x_range[1], 100)
    
    y = slope * (x - x0) + y0
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'Line: y - {y0} = {slope}(x - {x0})')
    
    plt.plot(x0, y0, 'ro', label='Given Point')

    plt.title('Point-Slope Form Linear Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.show()   

class nonlinear(): # func6
    def main_non_linear(self):
        while True:
            print()
            print("Non Linear Equation Calculator")
            print("1. Quadratic Equation ( ax^2 + bx + c = 0 )")
            print("2. Exponential Equations ( e^x = 3x )")
            print("3. Trigonometric Equations ( e^x = 0 )")
            print("0. Exit")
            choice = input("> ")
            if choice == '1':
                self.quadratic()
            elif choice == '2':
                self.exponential()
            elif choice == '3':
                self.trigonometric()
            elif choice == '0':
                return
            else:
                input("Invalid choice! Please choose from 1-3.")
                enter()

    def quadratic(self):
        pass
    def exponential(self):
        pass
    def trigonometric(self):
        pass
nonlin   = nonlinear()

def func7() : 
    print("WIP") # Work in progress

def func8() : 
    print()
    print("Simulation is a training method that demonstrates something")
    print("AS AN IMITATION form that is SIMILAR with real situation")
    print()
    print("Some simulation require RANDOM VARIABLE INPUT")
    print("to produce realistic OUTPUTS")
    print()
    enter()

    print()
    print("Random variable input can be generated with PSEUDO RANDOM NUMBER GENERATOR (PRNG)")
    print("One example of PRNG that can be used is Linear Congruential Generator (LCG)")
    print()
    print("The Formula of LGC is : ")
    print("Zi = (a * Zi-1 + c) * mod m")
    print("a = multiplier")
    print("c = increment")
    print("m = modulus")
    print()
    enter()

    print()
    print("Input start state ")
    start = int(input("> "))
    print("Input a (multiplier) ")
    a = int(input("> "))
    print("Input c (increment) ")
    c = int(input("> "))
    print("Input m (modulus) ")
    m = int(input("> "))
    print("Input iteration ")
    iteration = int(input("> "))
    print()
    data = {'iteration': [], 'calc': [], 'Zi': [], 'mod': [], 'Ui = Zi/m': []}
    
    print("a = ", a)
    print("c = ", c)
    print("m = ", m)
    print("start = ", start)
    print()

    print("Zi = (a * Zi-1 + c) * mod m")
    print("calc = (a * Zi-1 + c)")
    
    for i in range(iteration):
        calc = (a * start + c)
        mod = m
        zi = calc % m
        ui = zi / m
        
        data['iteration'].append(i+1)
        data['calc'].append(calc)
        data['mod'].append(m)
        data['Zi'].append(zi)
        data['Ui = Zi/m'].append(round(ui, 4))

        start = zi
    
    print(f"{'iteration':<12}{'calc':<10}{'mod':<7}{'Zi':<8}{'Ui = Zi/m':<12}")
    print("-" * 40)
    for i, calc, mod, zi, ui in zip(data['iteration'], data['calc'], data['mod'], data['Zi'],data['Ui = Zi/m']):
        print(f"{i:<12}{calc:<10}{mod:<7}{zi:<8}{ui:<12}")  
    print()
    enter()

    print()
    print("if you look carefully, around iteration", mod , "or", mod + 1, ", the result of Zi and Ui with iteration 1 are similar")
    print("The calc, Zi, Ui of iteration number 2 are similar with iteration" , mod + 1, "or" , mod + 2,)
    print("You might recognize other pattern as well")

    print()
    print("PNRG has a certain period where if it has reached that period,")
    print("the resulting sequence of numbers will repeat from the beginning, starting the previous pattern")

def func9() :
    print()
    print("Iterative method is one of the ways to solve complex linear equations")
    print()
    print("As its name suggests, the iterative method finds the solution by using REPEATED ITERATIONS ")
    print("until the solution CONVERGES with desired accuracy")
    print()
    enter()
            

    print("To solve the complex linear equation, we have to convert the linear equation into 2 matrixes")
    print("Matrix A stores the coefficients of the variables")
    print()
    A = [
        [4, 1, 1],
        [4, -8, 1],
        [-2, 1, 5],
        ]
    print("A: ", A)
    print()

    print("Matrix b stores the constants on the right side of the equations")
    b = [7, -21, 15]
    print()
    print("b: ",b)
    print()
    enter()
            
    print()
    print("After some iterations, here's the result of the calculation using Jacobi iterative and Gauss-Seidel iterative")
    print()
    try:
        solutionJacobi, iterationJacobi = jacobi(A, b)
        solutionGauss, iterationGauss = gauss_seidel(A, b)
        print("Solution with Jacobi:", solutionJacobi)
        print("Iterations with Jacobi:", iterationJacobi)
        print()

        print("Solution with Gauss-Seidel:", solutionGauss)
        print("Iterations with Gauss-Seidel:", iterationGauss)
                
        print("\nVerification:")
        print("A * Solution Jacobi\t\t =", np.dot(A, solutionJacobi))
        print("A * Solution Gauss-Seidel\t =", np.dot(A, solutionGauss))
                
        print("B\t\t\t\t = ",b)
        print()
        print("Usually, Jacobi iterative requires more iteration than Gauss-Seidel iterative")
        print()
        print("The results are close to the expected values, differing only by small amounts ")
        print("If we want a MORE ACCURATE solution, we can decrease the TOLERANCE VALUE")
        print()
        enter()
        
    except ValueError as e:
        print(e)
        enter()

def jacobi(A,b, x0=None, tolerance=1e-10,max_iterations = 1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(A)

    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = np.array(x0, dtype=float)
    
    for i in range(max_iterations):
        x_new = np.zeros_like(x)

        for j in range(n):
            sum1 = np.dot(A[j, :], x) - A[j, j] * x[j]
            x_new[j] = (b[j] - sum1) / A[j, j]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new, i + 1
        
        x = x_new
    raise ValueError(f"Method did not converge after {max_iterations} iterations")

def gauss_seidel(A, b, x0=None, tolerance=1e-10, max_iterations=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(A)

    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = np.array(x0, dtype=float)

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            
            x[i] = (b[i] - sigma) / A[i][i]
        
        if np.linalg.norm(x - x_old) < tolerance:
            return x, iteration + 1
    raise ValueError(f"Method did not converge after {max_iterations} iterations")

def func10() : 
    print("WIP") # Work in progress

def func11() : 
    print("WIP") # Work in progress
        
def enter(): # biar gak perlu klik input() terus
    input("Press Enter to continue")

def print_matrix(matrix_el):
    for row in matrix_el:
        print(" ".join(f"{x:8.4f}" for x in row))

def main():
    print("================== Group 7 ===================")
    print("| 1. Sandhika Lyandra P        074 - TI 23 C |")
    print("| 2. Rayhan Hendra Atmadja     075 - TI 23 C |")
    print("| 3. Adriano Emmanuel          082 - TI 23 C |")
    print("| 4. Cornelius Louis Nathan    085 - TI 23 C |")
    print("==============================================")

    while True:
        print("\n========= Science Comp Implementation ========")
        print("1. Systems of Linear Equations") # Sistem Persamaan Linear
            # nanti terbagi menjadi 2, cara triangularisasi dan eliminasi gauss
        print("2. Matrix Practices and Operations")
            # ini bisa cuma ngeprint sifat" matrix, atau menampilkan penerapan matrix nya
        print("3. Invertible Matrik") # Invers Matrix
        print("4. LU Decomposition")
        print("5. Numeric Method of Linear Equations")  # Persamaan linear
            # sebenarnya aku bingung mau implemen ini, karena pptnya gk dikasih ama ibunya
        print("6. Numeric Method of Non Linear Equations")
            # ada 2 metode, metode biseksi (metode tertutup) dan newton rhapson (metode terbuka) (pilih salah satu aja gak seh?)
        print("7. Interpolation") # Interpolasi
            # ada 3, interpolasi linear, interpolasi kuadrat/non linear, polinom newton (pilih salah satu aja gak seh?)
        print("8. Basic Simulation")
            # sejauh ini, kalau simulasi..  paling mentok bisa nerapin Linear Congruential Generators (LCG) (PPT Slide 18)
            # LCG itu teori kalau misalkan hasil perhitungannya melebihi mod itu, maka hasil perhitungannya akan kembali seperti semula
        print("9. Iterative Method") # Teori iterasi
            # iterasi jacobi dan gauss-seidler
        print("10. Monte-Carlo Simulation")
        print("11. Markov Chain")
        print("12. Exit\n")

        print("Choose from 1-11")
        try:
            choice = int(input("> "))
        except ValueError:
            print("\nInvalid input, choose from 1-12!")
            enter()
            continue

        if choice == 1:
            func1()

        elif choice == 2:
            func2()

        elif choice == 3:
            A = [
                [4, 7, 2],
                [2, 6, 1],
                [1, 5, 3]
            ]
            inverse = inverse_matrix(A)
            print("Original matrix:")
            print_matrix(A)
            print("Inverse matrix:")
            print_matrix(inverse)
            print("Inverse matrix with numpy:")
            print_matrix(np.linalg.inv(A))
            enter()

        elif choice == 4:
            A = [
                [4, 7, 2],
                [2, 6, 1],
                [1, 5, 3]
            ]
            L, U = lu_decomposition(A)
            print("L:")
            print_matrix(L)
            print("U:")
            print_matrix(U)
            enter()

        elif choice == 5:
            # Persamaan : y = mx + b = 5x - 3/4
            # m(slope) = -3/4
            # b(y-intercept) = 5
            plot_linear_equation_point_slope(point=(0, 5), slope=-3/4)
            enter()

        elif choice == 6:
            nonlin.main_non_linear()

        elif choice == 7:
            func7()

        elif choice == 8:
            func8()

        elif choice == 9:
            func9()

        elif choice == 10:
            func10()

        elif choice == 11:
            func11()

        elif choice == 12:
            print("Thank you")
            break


if __name__ == "__main__" : main() 