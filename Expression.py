
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

def evaluer_noeud(noeud, dernier_resultat=None):

    if isinstance(noeud, ast.Constant):
        if (isinstance(noeud.value, (int, float)) and not isinstance(noeud.value, bool)):
            return noeud.value
        raise ValueError("valeur non autorisee")

    if isinstance(noeud, ast.Name):
        if noeud.id == "ANS":
            if dernier_resultat is None:
                raise ValueError("Aucun resultat disponible")
            return dernier_resultat

        raise ValueError(
            f"variable inconnue: {noeud.id}"
        )
    
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

    




def evaluer_expression(expression, dernier_resultat=None):
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
        return evaluer_noeud(arbre.body, dernier_resultat)
    
    except ZeroDivisionError:
        raise ValueError("division par zero impossible")
    
    except OverflowError:
        raise ValueError("le resultat est trop grand")

























