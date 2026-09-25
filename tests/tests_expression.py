

import unittest
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


class TestExpressions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(
            evaluer_expression("2+3"), 5
        )

    def test_priorite(self):
        self.assertEqual(
            evaluer_expression("2+3*4"), 14
        )

    def test_parentheses(self):
        self.assertEqual(
            evaluer_expression("(2+3)*4"), 20
        )

    def test_puissance(self):
        self.assertEqual(
           evaluer_expression("2^3"), 8
        )

    def test_decimales(self):
        self.assertEqual(
            evaluer_expression("2.5*4"), 10
        )

    def test_division_zero(self):
        with self.assertRaises(ValueError):
            evaluer_expression("10 / 0")

    def test_expression_vide(self):
        with self.assertRaises(ValueError):
            evaluer_expression("")

    def test_expression_invalide(self):
        with self.assertRaises(ValueError):
           evaluer_expression("2 +")

    def test_parentheses_invalides(self):
        with self.assertRaises(ValueError):
            evaluer_expression("(2 + 3")

if __name__ == "__main__":
    unittest.main()
