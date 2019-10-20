// ID : 1710009
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

options{
	language=Python3;
}


//===============PROGRAMS===============
program  : declaration+ EOF ;

declaration: vardec | fundec ;
//======================================



//===============DECLARATIONS===============
vardec: primitive var(COMMA var)* SEMI ;

var: IDENTIFIER | IDENTIFIER LSQUARE INTLIT RSQUARE ;

fundec: funtype IDENTIFIER LBRACKET paralist RBRACKET blockstmt ;

funtype: primitive | VOIDTYPE | arraypointer ;

arraypointer: (INTTYPE | FLOATTYPE | STRINGTYPE | BOOLTYPE) LSQUARE RSQUARE ;

paralist: (paradec(COMMA paradec)*)? ;

paradec: primitive IDENTIFIER | primitive IDENTIFIER LSQUARE RSQUARE ;

primitive: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE ;
//==========================================



//===============STATEMENTS===============
blockstmt: LPARENTHESIS blockmem* RPARENTHESIS ;

blockmem: vardec | stmt ;

ifstmt: IF LBRACKET exp RBRACKET stmt (ELSE stmt)? ;

whilestmt: DO stmt+ WHILE exp SEMI ;

forstmt: FOR LBRACKET exp SEMI exp SEMI exp RBRACKET stmt ;

breakstmt: BREAK SEMI ;

continuestmt: CONTINUE SEMI ;

returnstmt: RETURN (exp)? SEMI ;

expstmt: exp SEMI ;

stmt: blockstmt | ifstmt | whilestmt | forstmt | breakstmt | continuestmt | returnstmt | expstmt ;
//========================================



//===============EXPRESSIONS===============
exp: exp1 (ASSIGN exp)? | exp8 | exp9 ;

exp1: exp1 OR exp2 | exp2 ;

exp2: exp2 AND exp3 | exp3 ;

exp3: exp4 ISEQUAL exp4 | exp4 ;

exp4: exp5 COMP exp5 | exp5 COMPEQ exp5 | exp5 ;

exp5: exp5 ADD exp6 | exp5 SUB exp6 | exp6 ;

exp6: exp6 DIV exp7 | exp6 MUL exp7 | exp6 MOD exp7 | exp7 ;

exp7: SUB exp7 | NOT exp7 | exp8 ;

exp8: exp9 LSQUARE exp RSQUARE | exp9 ;

exp9: LBRACKET exp RBRACKET | funcall | literals | IDENTIFIER ;

literals: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT ;

funcall: IDENTIFIER LBRACKET (exp(COMMA exp)*)? RBRACKET ;
//=========================================





//=======================================TOKENS=======================================





//===============COMMENTS, WHITESPACES AD NEWLINE===============
//Inline comment
INLINECMT: '//'~[\r\n]* -> skip ;
//Multiline comment
MULTILINECMT: '/*'.*?'*/' -> skip ;

//Whitespaces
WS : [ \f\t\r\n]+ -> skip ;

//Newline
NEWLINE: '\n' ;
//==============================================================



//===============KEYWORDS===============
INTTYPE: 'int' ;

FLOATTYPE: 'float' ;

BOOLTYPE: 'boolean' ;

STRINGTYPE: 'string' ;

VOIDTYPE: 'void' ;

BREAK: 'break' ;

CONTINUE: 'continue' ;

ELSE: 'else' ;

IF: 'if' ;

RETURN: 'return' ;

FOR: 'for' ;

DO: 'do' ;

WHILE: 'while' ;
//======================================



//===============LITERALS===============
INTLIT: [0-9]+ ;

fragment Exponent: [eE]SUB?INTLIT ;
fragment DECIMAL: '.' ;
fragment Fractional: DECIMAL INTLIT Exponent? ;
FLOATLIT: INTLIT'.'Exponent | INTLIT Exponent | Fractional | INTLIT Fractional | INTLIT'.' ;

BOOLLIT: 'true' | 'false' ;

STRINGLIT: '"'(~[\b\f\r\n\t"\\] | '\\'[bfrnt"\\])*'"' {self.text=self.text[1:(len(self.text)-1)]} ;
//======================================



//===============IDENTIFIERS===============
fragment Letter: [a-zA-Z]+ ;
fragment Digit: [0-9]+ ;
IDENTIFIER: (Letter | '_')(Letter | '_' | Digit)* ;
//=========================================



//===============OPERATORS===============
ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIV: '/' ;

MOD: '%' ;

NOT: '!' ;

OR: '||' ;

AND: '&&' ;

ASSIGN: '=' ;

ISEQUAL: '!=' | '==' ;

COMP: '<' | '>' ;

COMPEQ: '<=' | '>=' ;
//=======================================



//===============SEPARATORS===============
LSQUARE: '[' ;

RSQUARE: ']' ;

LBRACKET: '(' ;

RBRACKET: ')' ;

LPARENTHESIS: '{';

RPARENTHESIS: '}';

SEMI: ';' ;

COMMA: ',' ;
//========================================



//==============EXCEPTIONS==============
fragment ILLEGAL_CHAR: '\\'~[bnrft"] ;

ERROR_CHAR: ~'"' {raise ErrorToken(self.text)} ;

UNCLOSE_STRING: '"'(~[\b\f\r\t"\\] | '\\'[bfrnt"\\])*NEWLINE? {raise UncloseString(self.text[1:])} ;

ILLEGAL_ESCAPE: '"'(~[\n"\\] | '\\'[bfrnt"\\])*ILLEGAL_CHAR {raise IllegalEscape(self.text[1:])} ;
//======================================