test = {
  'name': 'Prologue - Reader',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '335e073a1cf6dfcf2d9615ce9c39f5a1',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': '8daa122fc80eecb017a656bbd3702479',
          'choices': [
            'Evaluates call expressions',
            'Turns input into tokens',
            'Ensures a function has been defined before it is called',
            'Turns input into a useful data structure'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the read component of the REPL loop do?'
        },
        {
          'answer': '0a4c12327fcbb6f55ab2d60bdcce46cb',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the tokenize function in reader.py return?'
        },
        {
          'answer': '36910e73ebeb60354b6ef86dc70c087e',
          'choices': [
            "['add', '(', 3, ',', 4, ')']",
            "['a', 'd', 'd', '(', '3', ',', '4', ')']",
            "['add', '(', '3', ',', '4', ')']",
            "['a', 'd', 'd', '(', 3, ',', 4, ')']"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What will tokenize('add(3, 4)') output?"
        },
        {
          'answer': 'dae434487e3900ad65014b0b8947167d',
          'choices': [
            "['(', LambdaExpr, 4, ')', '(', ')']",
            "['lambda', 4, '(', ')']",
            "['(', 'lambda', ':', 4, ')', '(', ')']",
            "['(', LambdaExpr, ':', 4, ')', '(', ')']"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What will tokenize('(lambda: 4)()') output?"
        },
        {
          'answer': '205e0ee67ced19edb40d6cf20a59f4c0',
          'choices': [
            'List of tokens and number of parentheses',
            'Input expression and list of tokens',
            'List of tokens and an instance of a subclass of Expr',
            'Input expression and an instance of a subclass of Expr'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What does the read_expr function in reader.py accept as input and
          return?  (looking at the read function may help answer this question)
          """
        },
        {
          'answer': '38d93d9daa46eba5e48a732180c5c991',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the read function in reader.py return?'
        },
        {
          'answer': '75978caa33d69044a6d5e88d39a39b4e',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What will read('1') output?"
        },
        {
          'answer': 'ac02304c9e1e97cf8d89e1d1b0dd78a1',
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What will read('x') output?"
        },
        {
          'answer': '098a45c74e16138b2227d354b677f60a',
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What will read('add(3, 4)') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
