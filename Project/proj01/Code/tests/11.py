test = {
  'name': 'Problem 11',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swine_swap_strategy(0, 10, cutoff=10, num_rolls=5)
          976b54e6eb8a63e73c36316e8c61f45f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap_strategy(3, 20, cutoff=10, num_rolls=6)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap_strategy(17, 3, cutoff=0, num_rolls=7)
          b0cb5865635519a2ebfd8d2300958add
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_swap_strategy(24, 5, cutoff=8, num_rolls=8)
          754e0ae22708be05fbf602cefede6d63
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(swine_swap_strategy)
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
