test = {
  'name': 'sub-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sub-all '(a (a b c) d) '(b d) '(e f))
          (a (a e c) f)
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
