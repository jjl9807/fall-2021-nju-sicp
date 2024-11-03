test = {
  'name': 'Problem 3',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy('Cute Dog!', 'Cute Dog.')
          50.0
          >>> accuracy('A Cute Dog!', 'Cute Dog.')
          0.0
          >>> accuracy('cute Dog.', 'Cute Dog.')
          50.0
          >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
          50.0
          >>> accuracy('Cute', 'Cute Dog.')
          100.0
          >>> accuracy('', 'Cute Dog.')
          0.0
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
