test = {
  'name': 'k-curry',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (f a b c d) (- (+ a c) (+ b d)))
          f
          scm> (define minus-six (k-curry f (a b c d) (2 4) (1 3)))
          minus-six
          scm> (minus-six 8 10) ; (- (+ 8 10) (+ 2 4))
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
