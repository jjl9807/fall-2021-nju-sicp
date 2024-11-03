test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (add-one x) (+ x 1))
          add-one
          scm> (define (mul-two x) (* x 2))
          mul-two
          scm> (define mul-two-then-add-one (composed add-one mul-two))
          mul-two-then-add-one
          scm> (mul-two-then-add-one 2)
          5
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
