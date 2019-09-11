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
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
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
                        2 Program Structure
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

function_declaration: type ID LB parameter_list RB block_statement;

type
    : primitive_type 
    | array_pointer_type 
    | void_type;

parameter_list: parameter_declaration (COMMA parameter_declaration)*;

parameter_declaration:  primitive_type ID (LSB RSB)?;

block_statement: LP (variable_declaration | statement)* RP;


/*----------------------------------------------------------------
                    3 Lexical Specification 
------------------------------------------------------------------*/
//3.1 Character Set

//3.2 Comments

//LINE_COMMENT: '//'~[\n]* -> skip;

//BLOCK_COMMENT: '/*' .*? '*/' -> skip;

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
FALSE 'false';
STRING: 'string';

// OPERATORS
ADD: '+';
MUL: '*';
NOT: '!';
OR: '|';
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

//3.5 Literals
literal
    : INTLIT
    | FLOATLIT
    | BOOLIT
    | STRINGLIT;

INTLIT: [0-9]+;
FLOATLIT: ;
BOOLIT: TRUE | FALSE;
STRINGLIT:;

/*----------------------------------------------------------------
                        4 Types and Values
------------------------------------------------------------------*/
types
    : primitive_type 
    | void_type 
    | (array | array_pointer_type);

//4.1 The void Type and Values 
void_type: ;
//4.2 The boolean Type and Values 
//4.3 The int Type and Values
//4.4 The float Type and Values 
//4.5 The string Type and Values
//4.6 Array Types and Their Values 
//4.7 Array Pointer Type

/*----------------------------------------------------------------
                           5 Variables
------------------------------------------------------------------*/
variables
    : global_variable
    | local_variable;

//5.1 Global Variables 
global_variable:;
//5.2 Local Variables
local_variable:;

/*----------------------------------------------------------------
                            6 Expressions 
------------------------------------------------------------------*/
expression: (operand | operator)+;

operand
    : literal 
    | ID 
    | element_of_array 
    | function_call;

//6.1 Precedence and Associativity 
//6.2 Type Coercions 
//6.3 Index Expression 
//6.4 Invocation Expression 
//6.5 Evaluation Order 

/*----------------------------------------------------------------
                    7 Statements and Control Flow  
------------------------------------------------------------------*/

statements
    : if_statement
    | for_statement
    | while_statement
    | break_statement
    | continue_statement
    | return_statement
    | expression_statement
    | block_statement;

//7.1 The if Statement

if_statement
    : if_else 
    | if_no_else;

if_else: 
    IF LB BOOL RB 
        statement1
    ELSE
        statement2;

if_no_else:
    IF LS BOOL RS
        statement1;

//7.2 The do while Statement 

DO ;

//7.3 The for Statement 
for_statement: FOR LB exp1 SEMI exp2 SEMI exp3 RNB statement;


//7.4 The break Statement 
//7.5 The continue Statement 
//7.6 The return Statement 
//7.7 The expression Statement
//7.8 The block statement 
/*----------------------------------------------------------------
                        8 Built-in Functions 
------------------------------------------------------------------*/

/*----------------------------------------------------------------
                          9 Scope Rules 
------------------------------------------------------------------*/

/*----------------------------------------------------------------
                       10 The main function 
------------------------------------------------------------------*/





WS : [ \t\r\n]+ -> skip;
ID: [a-zA-Z_][a-zA-Z_0-9]*;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;