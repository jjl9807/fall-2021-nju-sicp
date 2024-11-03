test = {
  'name': 'Problem 1',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['short', 'really long', 'tiny']
          >>> s = lambda p: len(p) <= 5
          >>> choose(ps, s, 0)
          'short'
          >>> choose(ps, s, 1)
          'tiny'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
