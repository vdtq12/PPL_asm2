grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF ;

decls: decl decls | decl ;
decl: var_decl | func_decl ;

// KEYWORDS
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
//
//FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
//
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
//TRUE: 'true';
WHILE: 'while';
//
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
//
ARRAY: 'array';



// OPERATOR
ADDOP: [+];
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
REMOP: '%';
//
NOTOP: '!';
ANDOP: '&&';
OROP: '||';
EQOP: '==';
//
NEQOP: '!=';
LTOP: '<';
LEQOP: '<=';
GTOP: '>';
GEQOP: '>=';
//
SCCOP: '::';



//SEPARATOR
LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
DOT: '.';
COMMA: ',';
SM: ';';
CM: ':';
EQUAL: '=';
fragment QUOTE: ['] ;
fragment DQUOTE: ["];



//LITERAL
INTLIT: ([0] | [1-9] ([0-9]*'_'[0-9]+)* | [1-9][0-9]*){self.text = self.text.replace('_','')};
fragment DECPART: [.][0-9]*;
fragment EXPPART: [e|E][+|-]?[0-9]+;
FLOATLIT: ((INTLIT DECPART | INTLIT EXPPART | INTLIT DECPART EXPPART)) {self.text = self.text.replace('_','')} ;
BOOLIT: 'true'|'false';
fragment ESCAPE: '\\' [btnfr'"\\];
fragment CHAR: ~[\b\t\n\f\r'"\\] | ESCAPE;
STRLIT: DQUOTE CHAR* DQUOTE {
	s = str(self.text)
	s = s[1:-1]
	self.text = s
};
//ARRAY LIST
arr_lit: LCB arr_ele_list? RCB;
arr_ele_list: expr COMMA arr_ele_list | expr;

//Atomic types
// BOO_TYP: BOOLEAN ;
// BOO_TYP_OPRD: OROP | ANDOP | EQOP | NEQOP | NOTOP;
// // INT_TYP: INTEGER;
// INT_TYP_OPRD: ADDOP | SUBOP | MULOP | DIVOP | REMOP |
// 				EQOP | NEQOP | GTOP | GEQOP | LTOP | LEQOP;
// // FLOAT_TYP: FLOAT;
// FLOAT_TYP_OPRD: ADDOP | SUBOP | MULOP | DIVOP |
// 				EQOP | NEQOP | GTOP | GEQOP | LTOP | LEQOP;
// // STR_TYP: STRING;
// STR_TYP_OPRD: SCCOP;
// array literal




//ARRAY TYPE
array_typ: ARRAY dimslist OF element_typ;
dimslist: LSB dims RSB;
dims: INTLIT COMMA dims | INTLIT;
element_typ: BOOLEAN | INTEGER | FLOAT | STRING;

arr_ele_access: ID LSB idxlist RSB;
idxlist: INTLIT COMMA idxlist | INTLIT;



//Variable declarations
var_decl: (s_var_decl | l_var_decl) SM;
s_var_decl: id_list CM typ;
l_var_decl: ID COMMA l_var_decl COMMA (expr|arr_lit) | ID CM typ '=' (expr|arr_lit);
id_list: ID COMMA id_list | ID;
typ: INTEGER | FLOAT | STRING | BOOLEAN | AUTO | array_typ;


// param_decl: param_list;
param_list: param COMMA param_list | param;
param: INHERIT? OUT? ID CM typ;


//func declaration
// func_decl:.;
func_decl: func_proto block_stmt;
func_proto: ID CM FUNCTION ret_typ LRB param_list? RRB (INHERIT ID)?;
ret_typ: VOID | typ;
// func_body: block_stmt;



// expression
expr_list: expr COMMA expr_list | expr;
//is_2list_eq: (ID is_2list_eq expr | );

expr: expr1 SCCOP expr1 | expr1;
expr1: expr2 (EQOP|NEQOP|LTOP|GTOP|LEQOP|GEQOP) expr2 | expr2;
expr2: expr2 (ANDOP|OROP) expr3 | expr3;
expr3: expr3 (ADDOP|SUBOP) expr4 | expr4;
expr4: expr4 (MULOP|DIVOP|REMOP) expr5 | expr5;
expr5: NOTOP expr5 | expr6;
expr6: SUBOP expr6 | expr7;
expr7: expr7 LSB expr_list RSB | operand;
operand: INTLIT | FLOATLIT | BOOLIT | STRLIT | ID | arr_lit | func_call;

idx_oprt: ID LSB expr_list RSB;
func_call: ID LRB expr_list? RRB;

// special function
// spl_func_1: 'readInteger()';
// spl_func_2: 'printInteger(' (ID|idx_oprt) ')';
// spl_func_3: 'readFloat()';
// spl_func_4: 'writeFloat(' (ID|idx_oprt) ')' ;
// spl_func_5: 'readBoolean()';
// spl_func_6: 'printBoolean('(ID|idx_oprt) ')';
// spl_func_7: 'readString()';
// spl_func_8: 'printString(' (ID|idx_oprt) ')';
// spl_func_9: 'super(' expr_list ')';
// spl_func_10: 'preventDefault()';
// spl_func: spl_func_1 | spl_func_2 | spl_func_3 | spl_func_4 | spl_func_5 
// 			| spl_func_6 | spl_func_7 | spl_func_8 | spl_func_9 | spl_func_10;
// spl_stmt: spl_func SM;




// // statements
assign_stmt: (ID|idx_oprt) EQUAL expr SM;

if_stmt:IF LRB expr RRB stmt (ELSE stmt)?;

for_stmt: FOR LRB ID EQUAL expr COMMA expr COMMA expr RRB stmt;

while_stmt: WHILE LRB expr RRB stmt;

dowhile_stmt: DO block_stmt WHILE LRB expr RRB SM;

break_stmt: BREAK SM;

cont_stmt: CONTINUE SM;

return_stmt: RETURN expr? SM;

call_stmt: ID LRB expr_list? RRB SM;

block_stmt: LCB stmt* RCB;

stmt: assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt
		| break_stmt | cont_stmt | return_stmt | call_stmt | block_stmt | var_decl ; //spl_stmt



ID: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip;

WS : [ \t\r\n]+ -> skip ; 

ERROR_CHAR: .{raise ErrorToken(self.text)};

fragment ILL_ESC: ('\\' ~[bfnrt'"\\] | ~'\\' ['] );

ILLEGAL_ESCAPE: DQUOTE CHAR* ILL_ESC {
	s = str(self.text)
	raise IllegalEscape(s[1:])
};

UNCLOSE_STRING: DQUOTE CHAR* ([\r\n]| EOF) {
    s = str(self.text)
    e = '\r\n'
    if s[-1] in e:
        raise UncloseString(s[1:-1])
    else:
        raise UncloseString(s[1:])
}; 