test = {
  'name': 'Output Validation',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for i in range(300):
          ...    for j in range(300):
          ...        num_rolls = final_strategy(i, j)
          ...        assert \
          ...           isinstance(num_rolls, int) and 0 <= num_rolls <= 10, \
          ...           "Invalid output: final_strategy({}, {}) returned {}".format(i, j, repr(num_rolls))
          >>> assert \
          ...   isinstance(PLAYER_NAME, str) and 1 <= len(PLAYER_NAME) <= 64, \
          ...   "Invalid player name: {}".format(PLAYER_NAME)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from final_strategy import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
