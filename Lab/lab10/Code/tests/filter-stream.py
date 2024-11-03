test = {
  'name': 'filter-stream',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (print 'YOUR-TEST-HERE)
          your-test-here
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
