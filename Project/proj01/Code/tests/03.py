test = {
  'name': 'Problem 3',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> take_turn(2, 0, 0, make_test_dice(4, 5, 1))
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(3, 0, 0, make_test_dice(4, 6, 1))
          acb7ae51e29364a82ec8f43b4d92dd9d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(0, 0, 2)
          2fb5bd9d8cd23e16588e2242320006df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(0, 0, 0)
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(0, 0, 1)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(2, 0, 0, make_test_dice(6))
          ede5516ab4a5bf350b845ed0cc751b12
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(9, 1, 0, make_test_dice(4))
          36
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(7, 0, 0, make_test_dice(4, 1))
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> take_turn(8, 0, 0, make_test_dice(5))
          40
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hog.take_turn(5, 0, 0) # Make sure you call roll_dice!
          Called roll dice!
          9002
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> def roll_dice(current_score, num_rolls, dice):
      ...     print("Called roll dice!")
      ...     return 9002
      ...
      >>> hog.roll_dice, old_roll_dice = roll_dice, hog.roll_dice
      """,
      'teardown': r"""
      >>> hog.roll_dice = old_roll_dice
      """,
      'type': 'doctest'
    }
  ]
}
