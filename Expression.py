
import ast
import operator

OPERATEURS = {
    ast.Add: operator.add,
    ast.Sub:operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}

def evaluer_noeud(noeud):

    if isinstance(noeud, ast.Constant):
        if (isinstance(noeud.value, (int, float)) and not isinstance(noeud.value, bool)):
            return noeud.value
        raise ValueError("valeur non autorisee")

    if isinstance(noeud, ast.BinOp):
        operateur = type(noeud.op)
        if operateur not in OPERATEURS:
            raise ValueError("valeur non autorisee")
        gauche = evaluer_noeud(noeud.left)
        droite = evaluer_noeud(noeud.right)
        return OPERATEURS[operateur](gauche, droite)

    if isinstance(noeud, ast.UnaryOp):
        operateur = type(noeud.op)
        if operateur not in OPERATEURS:
            raise ValueError("valeur non autorisee")
        valeur = evaluer_noeud(noeud.operand)
        return OPERATEURS[operateur](valeur)
    raise ValueError("expression non autorisee")

def evaluer_expression(expression):
    expression = expression.strip()

    if not expression:
        raise ValueError("l'expression est vide")
    
    expression = expression.replace("^","**")
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")

    try:
        arbre = ast.parse(expression, mode="eval")

    except SyntaxError:
        raise ValueError("expression invalide")
    try:
        return evaluer_noeud(arbre.body)
    except ZeroDivisionError:
        raise ValueError("division par zero impossible")
    
    except OverflowError:
        raise ValueError("le resultat est trop grand")

print(evaluer_expression("(2+4)x5"))























expression = input("expression:")
def calculer_expression(expression):
    expression = expression.replace(" ", "")
    print(f"expression recue: {expression}")

operateurs = "+-*/"
def est_operateur(caractere):
    return caractere in operateurs


def tokeniser(expression):
    tokens = []
    nombre= ""

    for caractere in expression:
        if caractere.isdigit() or caractere == ".":
            nombre+=caractere
        elif est_operateur(caractere):
            if nombre:
                tokens.append(nombre)
                nombre=""
            tokens.append(caractere)

    if nombre:
        tokens.append(nombre)
    return tokens

print(tokeniser(expression))

