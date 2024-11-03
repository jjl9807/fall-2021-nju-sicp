test = {
  'name': 'avg_difference',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM avg_difference;
          1024.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
