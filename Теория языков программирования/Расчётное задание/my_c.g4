grammar my_c;

run_program
    :  program EOF
    ;

program
    :
    (   main
    |   data
    |   struct)*
    ;

data
    :  typeData Identifier init (',' Identifier init)* ';'
    ;

typeData
    :   'double'
    |   'short' ('int')?
    |   Identifier
    ;

init
    :   ('=' priority_level1)?
    ;

main
    :   typeData 'main' '(' ')' block
    ;

block
    :   '{' blockContent* '}'
    ;

blockContent
    :   blockItem
    |   blockContent blockItem
    ;

blockItem
    :   (data
    |   operator
    |   struct)
    ;

operator
    :   ';'
    |   assignment
    |   condition
    |   block
    ;

assignment
    : Identifier ('.' Identifier)* '=' priority_level1 ';'
    ;

condition
    :   'if' '(' priority_level1 ')' operator ('else' operator)?
    ;

struct
    :   'struct' Identifier '{' dataStruct* '}' ';'
    ;

dataStruct
    : typeData Identifier (',' Identifier)* ';'
    ;

conditionalOperates
    :   '>'
    |   '<'
    |   '>='
    |   '<='
    ;

shiftOperates
    :   '>>'
    |   '<<'
    ;

ariphmeticOperates
    :   '+'
    |   '-'
    ;

mmdOperates
    :   '*'
    |   '/'
    |   '%'
    ;

priority_level1
    :   priority_level2 (conditionalOperates priority_level2)*
    ;

priority_level2
    :   priority_level3 (shiftOperates priority_level3)*
    ;

priority_level3
    :   priority_level4 (ariphmeticOperates priority_level4)*
    ;

priority_level4
    :   elementaryExpression (mmdOperates elementaryExpression)*
    ;

elementaryExpression
    :   Identifier ('.' Identifier)?
    |   Constant
    |   '(' priority_level1 ')'
    ;



Double : 'double';
Else : 'else';
If : 'if';
Int : 'int';
Return : 'return';
Short : 'short';
Struct : 'struct';

LeftParen : '(';
RightParen : ')';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LeftShift : '<<';
RightShift : '>>';

Plus : '+';
Minus : '-';
Star : '*';
Div : '/';
Mod : '%';

Semi : ';';
Comma : ',';

Assign : '=';

Dot : '.';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

Constant
    :   IntegerConstant
    |   FloatingConstant
    ;

fragment
IntegerConstant
    :   DecimalConstant
    ;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    |   [0]
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
FloatingConstant
    :   DecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart?
    |   DigitSequence ExponentPart
    ;

fragment
FractionalConstant
    :   DigitSequence? '.' DigitSequence
    |   DigitSequence '.'
    ;

fragment
ExponentPart
    :   'e' Sign? DigitSequence
    |   'E' Sign? DigitSequence
    ;

fragment
Sign
    :   '+' | '-'
    ;

fragment
DigitSequence
    :   Digit+
    ;

Whitespace
    :   [ \t]+
        -> skip
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
;