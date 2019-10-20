grammar MC;
// ID: 1710390
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

options{
	language=Python3;
}


//TOKEN SET

//TYPES:

mctype: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;

//KeyWords:

AND: '&';
BOOLEANTYPE: 'boolean';
INTTYPE: 'int';
STRINGTYPE: 'string';
FLOATTYPE: 'float';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
VOIDTYPE: 'void';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';

BACKSLASH: '\\';

//Identifiers:

fragment Int: [0-9] ;
fragment Letter: [a-zA-Z] ;
fragment Underscore: '_' ;
ID: (Letter|Underscore) (Letter|Int|Underscore)* ;

//Comment:
fragment Stringlit: ~["];
fragment Except: '\\' ~('b'|'f'|'r'|'n'|'t'|'"'|'\\');
fragment Accept: '\\' ('b'|'f'|'r'|'n'|'t'|'"'|'\\');
COMMENT: '/*' .*? '*/' | '//' .*? EOF ;


//Operators:

ADD: '+';
MUL: '*';
LOGICNOT: '!';
LOGICOR: '||';
NEQ: '!=';
LESS: '<';
LESSEQ: '<=';
ASSIGN: '=';
SUBNEG: '-';
DIV: '/';
MOD: '%';
LOGICAND:'&&';
EQ: '==';
GREATER: '>';
GREATEREQ: '>=';

//Separators: 

LB: '(';
RB: ')';
LP: '{';
RP: '}';
SM: ';';
CM: ',';
DOT: '.';
LV: '[';
RV: ']';

//Array Types:

varid: ID LV INTLIT RV | ID;

// Variables:


listID: varid CM listID | varid ;

// Statements:

// If Statement

ifstate: IF LB expr? RB EOF? stmt EOF? ( ELSE EOF? stmt)? ;

// While Statement

whilestate: DO (stmt SM)* WHILE  expr ;

// For Statement

forstate: FOR LB expr SM expr SM expr RB EOF? stmt ;

// Block Statement

blockstate: LP var_stmt* RP;

// Functions

paradec: LB paralist? RB ;
paralist: para (SM para)*;
para: mctype ID ;

var_stmt: var_dec | stmt;
var_dec: mctype listID SM;

stmt: (BREAK | CONTINUE | RETURN expr? | call | expr) SM | ifstate | whilestate | forstate  | blockstate ;

func: (VOIDTYPE|mctype) (ID|'main') paradec blockstate;

expr: expr ASSIGN expr1 | expr1;
expr1: expr2 LOGICOR expr1 | expr2;
expr2: expr3 LOGICAND expr2 | expr3;
expr3: expr4 EQ expr4 |expr4 NEQ expr4 | expr4;
expr4: expr5 LESS expr5 | expr5 LESSEQ expr5 | expr5 GREATER expr5 | expr5 GREATEREQ expr5 | expr5;
expr5: expr6 ADD expr5 | expr6 SUBNEG expr5 | expr6;
expr6: expr7 DIV expr6 | expr7 MUL expr6 | expr7 MOD expr6 | expr7;
expr7: SUBNEG expr8 | LOGICNOT expr8 | expr8;
expr8: expr9 LV RV | expr9;
expr9: call | LB expr RB | varid | FLOATLIT | INTLIT | STRINGLIT | BOOLEANLIT ;

call: ID LB explist? RB;

explist: expr (CM expr)*;

program:  decls EOF;
decls: (func|var_stmt)+;

//Literals:

fragment E: 'e'|'E' ;
fragment HasE: E '-'? INTLIT ;
INTLIT: '0' | [1-9] Int* ;
fragment Float: INTLIT? '.' INTLIT;
FLOATLIT: Float HasE? | INTLIT '.' | INTLIT HasE ;
BOOLEANLIT: TRUE|FALSE ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' (Accept|~('"'|'\\'))*  Except  (Accept|~('"'|'\\'))* '"'
{ self.text= self.text[1:-1]
};
UNCLOSE_STRING: '"' (Stringlit*|~('"'|'\\')* '\\"') Stringlit*
{ self.text= self.text[1:]
};
STRINGLIT: UNCLOSE_STRING '"'
{ self.text= self.text[1:-1]
};

