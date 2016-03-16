Homework: Implementing a SAT Solver

Part 1: Implement a SAT solver

You may write the program in Python or Haskell. Alternatively, your group may use another programming language of your choice if you obtain the agreement of Janoš Vidali.

The SAT solver should take an input in conjunctive normal form. If SAT solving succeeds it should return a satisfying valuation. Apart from these constraints, you can choose whichever SAT-solving method you prefer for your implementation.

At this stage, concentrate on the correctness of your SAT solver, not on its efficiency.

Part 2: Interfacing the SAT solver

Interface your SAT solver so it takes input from a file in Dimacs format specifying a cnf formula. There are example input files in the Homework Files directory (folder) on the course webpage.

The output of a satisfying valuation should also be saved in the format illustrated by the examples in the Homework Files directory on the course webpage. 

Part 3: Construct your own test files

Construct examples of test files, in Dimacs format, containing CNF of different sizes to test your solver on.

Part 4: Improve efficiency

Try to improve the efficiency of your SAT solver (for example, by modifying the search strategy, or by implementing known techniques for SAT solving, or even by implementing techiques of your own.
