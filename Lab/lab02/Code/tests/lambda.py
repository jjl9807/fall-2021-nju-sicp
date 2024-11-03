test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '1ec9bb860ebfb1ac075b03c1294307c6',
          'choices': [
            'A lambda expression does not automatically bind the function object that it returns to any name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following statements describes a difference between a def statement and a lambda expression?'
        },
        {
          'answer': '81f74e68d1c167350f45313a88df6730',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'e8f9f0009c378d71a44b00d1237cdd34',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> lambda x: x  # A lambda expression with one parameter x
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          7eb642f0e7486853009a51efefaac67f
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          13109c646a53e65280a61c8c1ad8d64d
          # locked
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> c()
          ef320d54ac07db169016e7ef445e9d96
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          4c5eb3ccbb3f19328aef2580205939be
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> x = None # remember to review the rules of WWPD given above!
          >>> x
          >>> lambda x: x
          36a08b27428b4f46661e44032fbc1e46
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          b2c695bc3b980a62202ceceb03bee56f
          # locked
          >>> f = lambda z: x + z
          >>> f(3)
          dfe33a8a341afd132925d9c31ac11778
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          dfe33a8a341afd132925d9c31ac11778
          # locked
          >>> higher_order_lambda(g)(2)
          b2c695bc3b980a62202ceceb03bee56f
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          13109c646a53e65280a61c8c1ad8d64d
          # locked
          >>> print_lambda = lambda z: print(z)
          >>> print_lambda
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> one_thousand = print_lambda(1000)
          315b2ee2e80f4b85b2c6179c5ac040dc
          # locked
          >>> one_thousand
          bd4e2072d9ffc96025c292287c2da64e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
