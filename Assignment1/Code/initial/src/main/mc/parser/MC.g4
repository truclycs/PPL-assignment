/*
   **************************************
   * Student name: Nguyen Thi Truc Ly   *
   * Student ID: 1710187                *
   **************************************
*/

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

program: many_declarations+ EOF;
many_declarations
    : variable_declaration 
    | function_declaration;

/*----------------------------------------------------------------
                        2 Program Structure (done)
------------------------------------------------------------------*/

//2.1 Variable declaration

variable_declaration: primitive_type (variable | many_variables) SEMI;

primitive_type
    : BOOL 
    | INT 
    | FLOAT 
    | STRING;

variable: ID (LSB INTLIT RSB)?;

many_variables: variable (COMMA variable)*;

//2.2 Function declaration  

function_declaration: types ID LB parameter_list? RB block_statement;

types
    : primitive_type 
    | array_pointer_type 
    | VOID; //void_type = 'void'?

parameter_list: parameter_declaration (COMMA parameter_declaration)*;

parameter_declaration:  primitive_type ID (LSB RSB)?;


/*----------------------------------------------------------------
                    3 Lexical Specification 
------------------------------------------------------------------*/
//3.1 Character Set

//3.2 Comments

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\n]* -> skip;

//3.3 Token Set 

//ID: ok, final file

//KEYWORDS
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
TRUE: 'true';
FALSE: 'false';
STRING: 'string';

// OPERATORS
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

//3.4 Separators 

LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';
DOT: '.';

//3.5 Literals
literal
    : INTLIT
    | FLOATLIT
    | BOOLLIT
    | STRINGLIT;

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] '-'? DIGIT+;

INTLIT: DIGIT+;

FLOATLIT
    : DIGIT+ ('.' DIGIT*)? EXPONENT? 
    | '.' DIGIT+ EXPONENT?;

BOOLLIT
    : TRUE 
    | FALSE;

fragment BSP: '\\b';
fragment FF: '\\f';
fragment CR: '\\r';
fragment NEWLINE: '\\n'; 
fragment TAB: '\\t';
fragment DQUOTE: '\\"';
fragment BSL: '\\\\';
fragment LEGAL_ESCAPE
    : BSP
    | FF
    | CR
    | NEWLINE
    | TAB
    | DQUOTE
    | BSL;
    
UNCLOSE_STRING: '"' (~[\n\r\\"] | LEGAL_ESCAPE)*;

ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbft"]);

STRINGLIT: UNCLOSE_STRING '"' {
    self.text = self.text[1:-1]
};

/*----------------------------------------------------------------
                        4 Types and Values
------------------------------------------------------------------*/

//4.1 The void Type and Values 
//4.2 The boolean Type and Values 
//4.3 The int Type and Values
//4.4 The float Type and Values 
//4.5 The string Type and Values
//4.6 Array Types and Their Values 
//4.7 Array Pointer Type

array_pointer_type
    : input_parameter
    | output_parameter;

input_parameter: primitive_type ID LSB RSB;

output_parameter: primitive_type LSB RSB;

/*----------------------------------------------------------------
                           5 Variables
------------------------------------------------------------------*/
// variables
//     : global_variable
//     | local_variable;

//5.1 Global Variables 
//5.2 Local Variables

/*----------------------------------------------------------------
                            6 Expressions 
------------------------------------------------------------------*/

//expression: (operand | operator)+;

operand
    : literal 
    | ID 
    | function_call;
    //| element_of_array;

/*operator
    : ADD
    | MUL
    | NOT
    | OR
    | NOT_EQUAL
    | LESS
    | LESS_EQUAL
    | ASSIGN
    | SUB
    | DIV
    | MOD
    | AND
    | EQUAL
    | GREATER
    | GREATER_EQUAL;*/

//6.1 Precedence and Associativity 

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

//6.2 Type Coercions 
//6.3 Index Expression 

//element_of_array: expression9 LSB expression RSB;

//6.4 Invocation Expression 

function_call: ID LB list_expression? RB;

list_expression: expression (COMMA expression)*;

//6.5 Evaluation Order 

/*----------------------------------------------------------------
                    7 Statements and Control Flow  
------------------------------------------------------------------*/

statement
    : if_statement
    | for_statement
    | while_statement
    | break_statement
    | continue_statement
    | return_statement
    | expression_statement
    | block_statement;

//7.1 The if Statement

if_statement: IF LB expression RB statement SEMI (ELSE statement SEMI)?;

//7.2 The do while Statement 

while_statement: DO (statement SEMI)+ WHILE expression;

//7.3 The for Statement 

for_statement: FOR LB expression SEMI expression SEMI expression RB statement SEMI;

//7.4 The break Statement 

break_statement: BREAK SEMI;

//7.5 The continue Statement 

continue_statement: CONTINUE SEMI;

//7.6 The return Statement 

return_statement: RETURN expression? SEMI;

//7.7 The expression Statement

expression_statement: expression SEMI;

//7.8 The block statement 

block_statement: LP (variable_declaration | statement SEMI)* RP;

/*----------------------------------------------------------------
                        8 Built-in Functions 
------------------------------------------------------------------*/

/*----------------------------------------------------------------
                          9 Scope Rules 
------------------------------------------------------------------*/

/*----------------------------------------------------------------
                       10 The main function 
------------------------------------------------------------------*/

ID: [a-zA-Z_][a-zA-Z0-9_]*; 
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: .;