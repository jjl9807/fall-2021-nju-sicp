test = {
  'name': 'label-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (label-sum t1)
          36
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
