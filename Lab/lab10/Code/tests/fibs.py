test = {
  'name': 'fibs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (slice fibs 0 10)
          (0 1 1 2 3 5 8 13 21 34)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
