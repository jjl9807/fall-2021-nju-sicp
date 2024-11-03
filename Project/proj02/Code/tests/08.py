test = {
  'name': 'Problem 8',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> prompt = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
          ID: 1 Progress: 0.6
          0.6
          >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
          ID: 2 Progress: 0.2
          0.2
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import report_progress
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
