test = {
  'name': 'let',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 0)
          y
          scm> (let* ((x 1) (y (+ x 1))) y)
          2
          scm> y
          0
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
