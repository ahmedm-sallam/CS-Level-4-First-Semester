Write a program in C++ that implements the analyzer step of our custom compiler of the TINY programming language based on the grammar rules of the language.

Program input: The scanner will take the path of a source code file written in the TINY programming language as an input; You can find an example of an input file in the file called `input.txt`.

- In the file `CompilersTask_2_Parser.cpp` you will find the solution to the scanning assignment; you can use this code to form the parse tree as the scanning step is a prerequisite to this step(This is preferable to using your own code so that it's guaranteed that the scanning step won't affect the output of this step).

- You will also find a suggested data structure to the tree node that you may use, however, this's not mandatory. You may create a different format to the tree nodes as long as your code is clean, readable, performant and follows the SOLID principles.

Program output: The program should output the terminal(leaf) nodes of the parse tree of the input file to the terminal or throw an exception once an error was found. You may use the `printTree` method found in the attached file called `CompilersTask_2_Parser.cpp` or if you decide to represent the tree nodes with a different data structure make sure your output follows the same format as in this method.

- The number of spaces to output before each node represents the level on which the node relies on(The order of the rule the node represented in related to the program node which is level 0).

- Each level in the tree is 3 spaces apart than its prior.

ex: 
input file content: if x < y
output:
[If]
   [Oper][LessThan]
      [ID][x]
      [ID][y]

input file content: temp := 20
output:
[Assign][temp]
      [Num][20]
TINY language grammar rules:
program -> stmtseq
stmtseq -> stmt { ; stmt }
stmt -> ifstmt | repeatstmt | assignstmt | readstmt | writestmt
ifstmt -> if expr then stmtseq [ else stmtseq ] end
repeatstmt -> repeat stmtseq until expr
assignstmt -> identifier := expr
readstmt -> read identifier
writestmt -> write expr
expr -> mathexpr [ (<|=) mathexpr ]
mathexpr -> term { (+|-) term }    left associative
term -> factor { (*|/) factor }    left associative
factor -> newexpr { ^ newexpr }    right associative
newexpr -> ( mathexpr ) | number | identifier
Notes:
This assignment will be graded against a unit testing module; so make sure your output follows the same format found in the `printTree` method.
The assignment should be done in teams of 3 members each.
Cheating cases will be graded negatively.
Please make sure that your code is clean as this will affect your grades(No commented out code, expressive naming, separation of concerns, No magic numbers, comments explaining complex parts of the code, code indented and styled properly, etc.).
Please make sure your code is also performant as this will affect your grade as well.