test = {
  'name': 'make-change',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-change 2 2)
          ((2) (1 1))
          scm> (make-change 3 3)
          ((3) (2 1) (1 1 1))
          scm> (make-change 4 3)
          ((3 1) (2 2) (2 1 1) (1 1 1 1))
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
