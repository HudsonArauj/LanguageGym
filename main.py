import sys
from preprocessor import PrePro
from parser import Parser
from symbol_table import SymbolTable

def main():
    source_code = sys.argv[1]
    with open(source_code, 'r') as file:
        code = file.read()
    filtered_code = PrePro.filter(code)
    try:
        parser = Parser(filtered_code)
        program = parser.parse()
        symbol_table = SymbolTable()
        program.evaluate(symbol_table)
        print("Tabela de Símbolos:", symbol_table.table)
    except Exception as e:
        print("Erro:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
