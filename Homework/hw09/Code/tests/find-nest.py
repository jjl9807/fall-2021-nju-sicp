test = {
  'name': 'find-nest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1 (2 3) ((4))))
          a
          scm> (find-nest 1 'a)
          (car a)
          scm> (find-nest 2 'a)
          (car (car (cdr a)))
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
