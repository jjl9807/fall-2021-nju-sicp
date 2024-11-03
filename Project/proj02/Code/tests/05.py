test = {
  'name': 'Problem 5',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          'cult'
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          'cul'
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          'car'
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import autocorrect
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
