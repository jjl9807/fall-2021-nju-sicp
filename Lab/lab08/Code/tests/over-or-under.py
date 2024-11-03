test = {
  'name': 'over-or-under',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (over-or-under 1 2)
          -1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (over-or-under 2 1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (over-or-under 1 1)
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
