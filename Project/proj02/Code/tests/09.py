test = {
  'name': 'Problem 9',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = time_per_word(p, words)
          >>> all_words(game)
          ['This', 'is', 'fun']
          >>> all_times(game)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> game = time_per_word(p, ['hello', 'world'])
          >>> word_at(game, 1)
          'world'
          >>> all_times(game)
          [[2, 1], [2, 3]]
          >>> time(game, 0, 1)
          1
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import time_per_word, all_words, all_times, time, word_at
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
