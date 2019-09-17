/* **************************************
   * Student name: Nguyen Thi Truc Ly   *
   * Student ID: 1710187                *
   ************************************** */

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]); 
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

/*----------------------------------------------------------------
                                PARSER
------------------------------------------------------------------*/

program: many_declarations+ EOF;
many_declarations: variable_declaration | function_declaration;

variable_declaration: primitive_type (variable | many_variables) SEMI;

many_variables: variable (COMMA variable)*;

variable: ID (LSB INTLIT RSB)?;

function_declaration: types ID LB parameter_list? RB block_statement;

types   : primitive_type 
        | array_pointer_type 
        | VOID; 

primitive_type: BOOL | INT | FLOAT | STRING;

array_pointer_type: primitive_type ID? LSB RSB;

block_statement: LP (variable_declaration | statement)* RP;

parameter_list: parameter_declaration (COMMA parameter_declaration)*;

parameter_declaration:  primitive_type ID (LSB RSB)?;

expression  : expression1 ASSIGN expression
            | expression1;

expression1 : expression1 OR expression2 
            | expression2;

expression2 : expression2 AND expression3
            | expression3;

expression3 : expression4 (EQUAL | NOT_EQUAL) expression4
            | expression4;

expression4 : expression5 (LESS| GREATER | LESS_EQUAL | GREATER_EQUAL) expression5
            | expression5;

expression5 : expression5 (ADD | SUB) expression6
            | expression6;

expression6 : expression6 (DIV | MUL | MOD) expression7
            | expression7;

expression7 : (SUB | NOT) expression7
            |expression8;

expression8 : operand LSB expression RSB
            | operand;

literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
operand     : literal 
            | LB expression RB
            | function_call
            | ID;

function_call: ID LB list_expression? RB;
list_expression: expression (COMMA expression)*;

statement   : if_statement
            | for_statement
            | while_statement
            | break_statement
            | continue_statement
            | return_statement
            | expression_statement
            | block_statement;

if_statement: IF LB expression RB statement (ELSE statement)?;
while_statement: DO statement+ WHILE expression SEMI;
for_statement: FOR LB expression SEMI expression SEMI expression RB statement;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN expression? SEMI;
expression_statement: expression SEMI;

/*----------------------------------------------------------------
                                LEXER
------------------------------------------------------------------*/

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

STRING: 'string';
BOOL: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
FLOAT: 'float';
IF: 'if';
INT: 'int';
RETURN: 'return';
VOID: 'void';
DO: 'do';
WHILE: 'while';

ADD: '+';
MUL: '*';
NOT: '!';
OR: '||';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
ASSIGN: '=';
SUB: '-';
DIV: '/';
MOD: '%';
AND: '&&';
EQUAL: '==';
GREATER: '>';
GREATER_EQUAL: '>=';

LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] '-'? DIGIT+;
INTLIT: DIGIT+;
FLOATLIT: DIGIT+ ('.' DIGIT*)? EXPONENT? | '.' DIGIT+ EXPONENT?;
BOOLLIT: 'true' | 'false';

ID: [a-zA-Z_][a-zA-Z0-9_]*; 
WS : [ \t\r\n]+ -> skip ; 
  
UNCLOSE_STRING: '"' (~[\n\r\\"] | '\\' [nrbft"\\])*;
ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbft"]);
STRINGLIT: UNCLOSE_STRING '"' {
    self.text = self.text[1:-1]
};
ERROR_CHAR: .;