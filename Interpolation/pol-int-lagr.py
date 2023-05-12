# Interpolacion de Lagrange

points = int(input("How many evaluated p do you have? "))
matrix = []

for i in range(points):
    row = []
    row.append(float(input("Enter value for x{0}: ".format(i+1))))
    row.append(float(input("Enter value for f(x){0}: ".format(i+1))))
    matrix.append(row)    

def build_polynomial(matrix):
    def evaluate(x):
        result = 0
        for i in range(len(matrix)): # i llevara la sumatoria
            term = matrix[i][1] # Seleccionamos la primera f(x) para multiplicarla por las expresiones de (x - xj) / (xi - xj)
            for j in range(len(matrix)): # j llevara las multiplicatorias
                if j != i: # Evitamos que la i == j para no tener 0 en el denominador y que resulte en una multiplicacion invalida
                    term *= (x - matrix[j][0]) / (matrix[i][0] - matrix[j][0])
            result += term
        return result
    return evaluate

def build_polynomial_text(matrix): #Misma funcion pero 
    def get_equation():
        equation = ""
        for i in range(len(matrix)):
            term = ""
            for j in range(len(matrix)):
                if j != i:
                    if matrix[i][0] - matrix[j][0] != 0:
                        term += f"(x - {matrix[j][0]}) / ({matrix[i][0]} - {matrix[j][0]})" # Construye una cadena de texto del polinomio
            term = f"{matrix[i][1]} * ({term})" if term else str(matrix[i][1])
            equation += term if not equation else f" + {term}" # Una ecuacion general
        return equation
    return get_equation


lagrange = build_polynomial(matrix);
lagrange_eq = build_polynomial_text(matrix);

print(f'POLINOMIO DE LAGRANGE {lagrange_eq()}'); 

calculate = True
while calculate is True:
    p = float(input("Wich point you want to calculate: "))
    print('{0} evaluated in the interpolant polynomial is: {1}'.format(p, lagrange(p)))
    calculate = True if input("You want to cotinue? ") == 'y'else False

