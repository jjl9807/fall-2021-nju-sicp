test = {
  'name': 'def',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (def f(x y) (+ x y))
          f
          scm> (f 1 2)
          3
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
