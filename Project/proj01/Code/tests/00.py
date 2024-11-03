test = {
  'name': 'Problem 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          2fb5bd9d8cd23e16588e2242320006df
          # locked
          >>> test_dice() # Second call
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          >>> test_dice() # Third call
          490c6bc3e1d941316ea5a790cc2d6d2c
          # locked
          >>> test_dice() # Fourth call
          2fb5bd9d8cd23e16588e2242320006df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'answer': 'b11d9ebd7f72653ef003f83b9207fa82',
          'choices': [
            'make_test_dice(6)',
            'make_fair_dice(6)',
            'six_sided',
            'six_sided()'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following is the correct way to "roll" a fair, six-sided die?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
