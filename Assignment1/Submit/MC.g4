/* **************************************
   * Student name: Nguyen Thi Truc Ly   *
   * Student ID: 1710187                *
   ************************************** */
<<<<<<< HEAD
=======

>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
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

<<<<<<< HEAD

=======
>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
/*----------------------------------------------------------------
                                PARSER
------------------------------------------------------------------*/

<<<<<<< HEAD
program: (var_decl | func_decl)+ EOF;

var_decl: primitive_type (var | many_var) SEMI;
many_var: var (COMMA var)*;
var: ID (LSB INTLIT RSB)?;

func_decl: types ID LB para_list? RB block_stmt;
para_list: para_decl (COMMA para_decl)*;
para_decl: primitive_type ID (LSB RSB)?;

types   : primitive_type 
        | array_pointer_type 
        | VOID; 
primitive_type: BOOL | INT | FLOAT | STRING;
array_pointer_type: primitive_type ID? LSB RSB;

exp : exp1 ASSIGN exp 
    | exp1;
exp1: exp1 OR exp2 
    | exp2;
exp2: exp2 AND exp3 
    | exp3;
exp3: exp4 (EQUAL | NOT_EQUAL) exp4 
    | exp4;
exp4: exp5 (LESS| GREATER | LESS_EQUAL | GREATER_EQUAL) exp5
    | exp5;
exp5: exp5 (ADD | SUB) exp6
    | exp6;
exp6: exp6 (DIV | MUL | MOD) exp7
    | exp7;
exp7: (SUB | NOT) exp7
    |exp8;
exp8: operand LSB exp RSB
    | operand;

operand : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT
        | LB exp RB
        | func_call
        | ID;

func_call: ID LB list_exp? RB;
list_exp : exp (COMMA exp)*;

stmt: if_stmt
    | for_stmt
    | while_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | exp_stmt
    | block_stmt;

if_stmt: IF LB exp RB stmt (ELSE stmt)?;
while_stmt: DO stmt+ WHILE exp SEMI;
for_stmt: FOR LB exp SEMI exp SEMI exp RB stmt;
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN exp? SEMI;
exp_stmt: exp SEMI;
block_stmt: LP (var_decl | stmt)* RP;
=======
program: many_declarations+ EOF;
many_declarations
    : variable_declaration 
    | function_declaration;

//2.1 Variable declaration

variable_declaration: primitive_type (variable | many_variables) SEMI;

primitive_type: BOOL | INT | FLOAT | STRING;

many_variables: variable (COMMA variable)*;

variable: ID (LSB INTLIT RSB)?;

//2.2 Function declaration  

function_declaration: types ID LB parameter_list? RB block_statement;

types
    : primitive_type 
    | array_pointer_type 
    | VOID; 

block_statement: LP (variable_declaration | statement)* RP;

parameter_list: parameter_declaration (COMMA parameter_declaration)*;

parameter_declaration:  primitive_type ID (LSB RSB)?;

expression
    : expression1 ASSIGN expression
    | expression1;

expression1
    : expression1 OR expression2 
    | expression2;

expression2
    : expression2 AND expression3
    | expression3;

expression3
    : expression4 EQUAL expression4
    | expression4 NOT_EQUAL expression4
    | expression4;

expression4
    : expression5 LESS expression5
    | expression5 GREATER expression5
    | expression5 LESS_EQUAL expression5
    | expression5 GREATER_EQUAL expression5
    | expression5;

expression5 
    : expression5 ADD expression6
    | expression5 SUB expression6
    | expression6;

expression6
    : expression6 DIV expression7
    | expression6 MUL expression7
    | expression6 MOD expression7
    | expression7;

expression7
    : SUB expression7
    | NOT expression7
    |expression8;

expression8
    : expression8 LSB expression RSB
    | expression9;

expression9
    : LB expression RB
    | operand;

array_pointer_type
    : input_parameter
    | output_parameter;

input_parameter: primitive_type ID LSB RSB;

output_parameter: primitive_type LSB RSB;

operand
    : literal 
    | ID 
    | function_call;
    //| element_of_array;

function_call: ID LB list_expression? RB;

list_expression: expression (COMMA expression)*;

statement
    : if_statement
    | for_statement
    | while_statement
    | break_statement
    | continue_statement
    | return_statement
    | expression_statement
    | block_statement;

if_statement: IF LB expression RB statement SEMI (ELSE statement SEMI)?;

while_statement: DO (statement SEMI)+ WHILE expression;

for_statement: FOR LB expression SEMI expression SEMI expression RB statement SEMI;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

return_statement: RETURN expression? SEMI;

expression_statement: expression SEMI;
>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9

/*----------------------------------------------------------------
                                LEXER
------------------------------------------------------------------*/

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
<<<<<<< HEAD
LINE_COMMENT: '//' ~[\r\n]* -> skip;

STRING: 'string';
=======
LINE_COMMENT: '//' ~[\n]* -> skip;

>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
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
<<<<<<< HEAD

=======
TRUE: 'true';
FALSE: 'false';
STRING: 'string';

// OPERATORS
>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
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

<<<<<<< HEAD
fragment DIGIT: [0-9];
fragment EXPONENT: [eE] '-'? DIGIT+;
INTLIT: DIGIT+;
FLOATLIT: DIGIT+ ('.' DIGIT*)? EXPONENT? | '.' DIGIT+ EXPONENT?;
BOOLLIT: 'true' | 'false';
=======
literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] '-'? DIGIT+;

INTLIT: DIGIT+;

FLOATLIT: DIGIT+ ('.' DIGIT*)? EXPONENT? 
        | '.' DIGIT+ EXPONENT?;

BOOLLIT: TRUE | FALSE;
>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9

ID: [a-zA-Z_][a-zA-Z0-9_]*; 
WS : [ \t\r\n]+ -> skip ; 
  
UNCLOSE_STRING: '"' (~[\n\r\\"] | '\\' [nrbft"\\])*;
ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbft"]);
STRINGLIT: UNCLOSE_STRING '"' {
    self.text = self.text[1:-1]
};
<<<<<<< HEAD
ERROR_CHAR: .;
=======
ERROR_CHAR: .;
>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
