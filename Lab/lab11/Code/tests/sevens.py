test = {
  'name': 'sevens',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          seven
          7
          7
          7
          7
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
