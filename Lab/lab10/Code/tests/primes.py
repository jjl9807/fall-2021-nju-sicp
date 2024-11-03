test = {
  'name': 'primes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (slice primes 0 10)
          (2 3 5 7 11 13 17 19 23 29)
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
