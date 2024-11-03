test = {
  'name': 'tree',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (label t1)
          1
          scm> (label (car (branches t1)))
          2
          scm> (is-leaf (car (cdr (branches t1))))
          #t
          scm> (branches (car (cdr (branches t1))))
          ()
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
