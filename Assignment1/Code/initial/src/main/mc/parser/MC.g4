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

/*----------------------------------------------------------------
                                LEXER
------------------------------------------------------------------*/

BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS : [ \t\f\r\n]+ -> skip ; 

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
  
UNCLOSE_STRING: '"' (~[\n\r\b\f\t\\"] | '\\' [nrbft"\\])*('\\')*;
ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbft"]);
STRINGLIT: UNCLOSE_STRING '"' {
    self.text = self.text[1:-1]
};
ERROR_CHAR: .;