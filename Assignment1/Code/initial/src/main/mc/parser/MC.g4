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

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options {
	language = Python3;
}

program: many_declarations+ EOF;
many_declarations: 
    variable_declaration 
    | function_declaration;

/*----------------------------------------------------------------
                        2 Program Structure
------------------------------------------------------------------*/

//2.1 Variable declaration

variable_declaration: primitive_type (variable | many_variables) SEMI;

primitive_type: BOOL | INT | FLOAT | STRING;

variable: ID (LSB INTLIT RSB)?;

many_variables: variable (COMMA variable)*;

//2.2 Function declaration  
`
function_declaration: type ID LB parameter_list RB block_statement;

type: 
    primitive_type 
    | array_pointer_type 
    | void_type;

parameter_list: parameter_declaration (COMMA parameter_declaration)*;
parameter_declaration:  primitive_type ID (LSB RSB)?;

/*----------------------------------------------------------------
                    3 Lexical Specification 
------------------------------------------------------------------*/
//3.1 Character Set
//3.2 Comments
//3.3 Token Set 
//3.4 Separators 
//3.5 Literals


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

/*----------------------------------------------------------------
                           5 Variables 10
------------------------------------------------------------------*/
//5.1 Global Variables 
//5.2 Local Variables

/*----------------------------------------------------------------
                            6 Expressions 
------------------------------------------------------------------*/

//6.1 Precedence and Associativity 
//6.2 Type Coercions 
//6.3 Index Expression 
//6.4 Invocation Expression 
//6.5 Evaluation Order 

/*----------------------------------------------------------------
                    7 Statements and Control Flow  
------------------------------------------------------------------*/

//7.1 The if Statement
//7.2 The do while Statement 

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

/*program: mctype 'main' LB RB LP body ? RP EOF;
mctype: INTTYPE | VOIDTYPE;
body: funcall SEMI;
exp: funcall | INTLIT;
funcall: ID LB exp ? RB;
INTTYPE: 'int';
VOIDTYPE: 'void';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines*/
INT: 'int';
FLOAT: 'float';
STRING: 'string';
BOOL: 'boolean';
INTLIT: [0-9]+;
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';
WS : [ \t\r\n]+ -> skip;
IF: 'if';
FOR: 'for';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;