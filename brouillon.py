import ast

expression = "2 + 3 * 4"

arbre = ast.parse(expression, mode="eval")

print(ast.dump(arbre, indent=4))