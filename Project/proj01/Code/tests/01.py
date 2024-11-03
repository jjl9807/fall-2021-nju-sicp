test = {
  'name': 'Problem 1',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(1, 2, make_test_dice(4, 6, 1))
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(1, 3, make_test_dice(4, 6, 1))
          490c6bc3e1d941316ea5a790cc2d6d2c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(0, 4, make_test_dice(2, 2, 3))
          6b16528b1fa45ed56a7ff5af01f0ed21
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = roll_dice(0, 4, make_test_dice(1, 2, 3))
          >>> a # check that the value is being returned, not printed
          490c6bc3e1d941316ea5a790cc2d6d2c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(0, 3, counted_dice)
          acb7ae51e29364a82ec8f43b4d92dd9d
          # locked
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement within a loop ends the loop
          >>> roll_dice(0, 1, counted_dice)
          b0cb5865635519a2ebfd8d2300958add
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(1, 9, make_test_dice(6))
          5ef471a5d3a7a0922b7b2ce610fcb1cc
          # locked
          >>> roll_dice(0, 7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          b0cb5865635519a2ebfd8d2300958add
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
    }
  ]
}
