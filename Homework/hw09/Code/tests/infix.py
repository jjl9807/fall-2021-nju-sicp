test = {
  'name': 'infix',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (infix ((1 + 2) * (3 + 4)))
          21
          scm> (infix (1 + 2 * 3 + 4))
          11
          scm> (define x 5)
          x
          scm> (infix ((1 + 2) * (3 + x)))
          24
          scm> (infix (1 + 2 * 3 + x))
          12
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
