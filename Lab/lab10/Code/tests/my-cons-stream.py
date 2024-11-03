test = {
  'name': 'my-cons-stream',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a (my-cons-stream 1 (my-cons-stream (print 2) nil)))
          a
          scm> (my-car a)
          1
          scm> (define b (my-cdr-stream a))
          2
          b
          scm> (define c (my-cdr-stream a))
          2
          c
          scm> (my-cdr-stream b)
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
