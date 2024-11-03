test = {
  'name': 'slice',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define nat (naturals 0))
          nat
          scm> (slice nat 4 12)
          (4 5 6 7 8 9 10 11)
          scm> (define a (cons-stream 1 (cons-stream 2 nil)))
          a
          scm> (slice a 1 114514)
          (2)
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
