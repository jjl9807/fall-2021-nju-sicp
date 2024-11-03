test = {
  'name': 'nondecrease',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define s (list-to-stream '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1)))
          s
          scm> (slice (nondecrease s) 0 8)
          ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1))
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
