test = {
  'name': 'Problem 9',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'answer': '83453fee152e8e3bf558d9d267e338b0',
          'choices': [
            'The lowest num_rolls',
            'The highest num_rolls',
            'A random num_rolls'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If multiple num_rolls are tied for the highest scoring
          average, which should you return?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3)   # dice always returns 3
          >>> max_scoring_num_rolls(0, dice, trials_count=1000)
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
          >>> max_scoring_num_rolls(1, dice, trials_count=1000)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(*([2] * 55 + [1, 2] * 500)) # test that you are actually using trials_count
          >>> max_scoring_num_rolls(0, dice, trials_count=1) # dice is 2 for the first 55 rolls, then is 1 followed by 2 for 1000 rolls
          10
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
          >>> dice = make_test_dice(2)     # dice always rolls 2
          >>> max_scoring_num_rolls(0, dice, trials_count=1000)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
          >>> max_scoring_num_rolls(1, dice, trials_count=1000)
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # 100 2s and then 100 1s (don't worry about how this works)
          >>> dice = make_test_dice(*([2] * 100 + [1] * 100))
          >>> max_scoring_num_rolls(1, dice, trials_count=1)
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(6, 5, 4, 3, 2, 1)  # dice sweeps from 1 through 6
          >>> max_scoring_num_rolls(2, dice, trials_count=1) # ensure trials_count is being used
          4
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
