test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (substitute '(a (a b c) d) 'b 'e)
          (a (a e c) d)
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
