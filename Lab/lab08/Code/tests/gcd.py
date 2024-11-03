test = {
  'name': 'gcd',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 2 3)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (gcd 16 12)
          4
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
