test = {
  'name': 'Problem 4',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wpm("12345", 3)
          20.0
          >>> wpm("", 10)
          0.0
          >>> wpm("a b c", 20)
          3.0
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import wpm
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
