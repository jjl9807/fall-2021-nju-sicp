test = {
  'name': 'Problem 10',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> picky_piggy_strategy(0, 6, cutoff=9, num_rolls=5)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(9, 0, cutoff=6, num_rolls=5)
          976b54e6eb8a63e73c36316e8c61f45f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(50, 3, cutoff=8, num_rolls=5)
          976b54e6eb8a63e73c36316e8c61f45f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(32, 0, cutoff=8, num_rolls=4)
          2fb5bd9d8cd23e16588e2242320006df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy_strategy(20, 0, cutoff=1, num_rolls=4)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(picky_piggy_strategy)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
