from Expression import *

class NumericExpression(Expression):
    """
    Class representing a numeric expression node in the AST of a MLP
    """

class NumericExpressionWithFunction(NumericExpression):
    """
    Class representing a numeric expression with function node in the AST of a MLP
    """

    ABS    = "abs"
    ATAN   = "atan"
    CARD   = "card"
    CEIL   = "ceil"
    COS    = "cos"
    FLOOR  = "floor"
    EXP    = "exp"
    LENGTH = "length"
    LOG    = "log"
    LOG10  = "log10"
    ROUND  = "round"
    SIN    = "sin"
    SQRT   = "sqrt"
    TRUNC  = "trunc"

    def __init__(self, function, numericExpression):
        """
        Set the numeric expression and the function

        :param function          : (abs | atan | card | ceil | cos | floor | exp | length | log | log10 | round | sin | sqrt | trunc)
        :param numericExpression : NumericExpression
        """

        self.function = function
        self.numericExpression = numericExpression

    def __str__(self):
        """
        to string
        """

        return str(self.function) + "(" + str(self.numericExpression) + ")"

    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this numeric expression with function
        """
        return codeGenerator.generateCode(self)
    

class ValuedNumericExpression(NumericExpression):
    """
    Class representing a valued numeric expression node in the AST of a MLP
    """

    def __init__(self, value):
        """
        Set the single value of this numeric expression

        :param value : Variable | Number
        """

        self.value = value

    def __str__(self):
        """
        to string
        """
        
        return "ValuedExpr:" + str(self.value)
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this valued linear expression
        """
        return codeGenerator.generateCode(self)


class NumericExpressionBetweenParenthesis(NumericExpression):
    """
    Class representing a numeric expression between parenthesis node in the AST of a MLP
    """

    def __init__(self, numericExpression):
        """
        Set the numeric expression

        :param numericExpression : NumericExpression
        """

        self.numericExpression = numericExpression

    def __str__(self):
        """
        to string
        """
        
        return "NE: (" + str(self.numericExpression) + ")"
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this valued linear expression
        """
        return codeGenerator.generateCode(self)


class NumericExpressionWithArithmeticOperation(NumericExpression):
    """
    Class representing a numeric expression with arithmetic operation node in the AST of a MLP
    """
    
    PLUS  = "+"
    MINUS = "-"
    TIMES = "*"
    DIV   = "/"
    MOD   = "%"
    POW   = "^"

    def __init__(self, op, numericExpression1, numericExpression2):
        """
        Set the expressions participating in the arithmetic operation
        
        :param op                 : (PLUS, MINUS, TIMES, MOD, POW)
        :param numericExpression1 : NumericExpression
        :param numericExpression2 : NumericExpression
        """
        
        self.op                 = op
        self.numericExpression1 = numericExpression1
        self.numericExpression2 = numericExpression2
    
    def __str__(self):
        """
        to string
        """
        
        return "OpArthNE:" + str(self.numericExpression1) + " " + self.op + " " + str(self.numericExpression2)
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this numeric expression with arithmetic operation
        """
        return codeGenerator.generateCode(self)


class MinusNumericExpression(NumericExpression):
    """
    Class representing a minus numeric expression node in the AST of a MLP
    """
    
    def __init__(self, numericExpression):
        """
        Set the numeric expression being negated
        
        :param numericExpression: NumericExpression
        """
        
        self.numericExpression = numericExpression
    
    def __str__(self):
        """
        to string
        """
        
        return "MinusNE:" + "-(" + str(self.numericExpression) + ")"
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this minus numeric expression
        """
        return codeGenerator.generateCode(self)


class IteratedNumericExpression(NumericExpression):
    """
    Class representing a iterated numeric expression node in the AST of a MLP
    """

    SUM  = "sum"
    PROD = "prod"
    MAX  = "max"
    MIN  = "min"

    def __init__(self, op, numericExpression, indexingExpression, supNumericExpression = None):
        """
        Set the components of the iterated linear expression

        :param op                   : op
        :param numericExpression    : NumericExpression
        :param indexingExpression   : IndexingExpression
        :param supNumericExpression : NumericExpression
        """
        
        self.op                   = op
        self.numericExpression    = numericExpression
        self.indexingExpression   = indexingExpression
        self.supNumericExpression = supNumericExpression

    def __str__(self):
        """
        to string
        """
        
        res = str(self.op) + "(" + str(self.indexingExpression) + ")"

        if self.supNumericExpression:
            res += "^(" + str(self.supNumericExpression) + ")"

        res += str(self.numericExpression)

        return "ItLE:" + res
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the variables and sets used in this numeric expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this iterated numeric expression
        """
        return codeGenerator.generateCode(self)