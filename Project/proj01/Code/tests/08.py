test = {
  'name': 'Problem 8',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a1406f5d04dc18073729db2f513dcf65',
          'choices': [
            'It contains a nested function',
            'It calls a function that is not itself',
            'It takes in a function as an argument',
            'It uses the *args keyword'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is one reason that make_averaged is a higher order function?'
        },
        {
          'answer': '3802b302eb8786124379b833f0632c87',
          'choices': [
            'None',
            'Two',
            'An arbitrary amount, which is why we need to use *args to call it'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How many arguments does the function passed into make_averaged take?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_dice = make_averaged(dice, 1000)
          >>> # Average of calling dice 1000 times
          >>> averaged_dice()
          88a737c26b18252743345f1f8a81c197
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
          >>> # Average of calling roll_dice 1000 times
          >>> # Hint: the first roll is (3, 1), the second roll is (5, 6)...
          >>> averaged_roll_dice(0, 2, dice)
          e72f7e36cda6454146b58b702af5691b
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
          'code': r"""
          >>> hundred_range = range(1, 100)
          >>> hundred_dice = make_test_dice(*hundred_range)
          >>> averaged_hundred_dice = make_averaged(hundred_dice, 5*len(hundred_range))
          >>> correct_average = sum(range(1, 100)) / len(hundred_range)
          >>> averaged_hundred_dice()
          50.0
          >>> averaged_hundred_dice()
          50.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 1)
          >>> averaged_roll_dice(0, 2, dice)
          1.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 5)
          >>> averaged_roll_dice(0, 2, dice)
          5.4
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
