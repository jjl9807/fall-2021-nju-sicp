test = {
  'name': 'factorials',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (slice factorials 0 10)
          (1 1 2 6 24 120 720 5040 40320 362880)
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
