from antlr4 import *
from parkingsignLexer import parkingsignLexer
from parkingsignParser import parkingsignParser
from parkingsignListener import parkingsignListener

input_text = input("> ")
lexer = parkingsignLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = parkingsignParser(stream)

tree = parser.parkingSign()

print(tree.toStringTree(recog=parser))