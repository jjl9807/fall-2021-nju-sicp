test = {
  'name': 'find',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (find 1 '(1 2 3))
          0
          scm> (find 2 '(1 2 3))
          1
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
