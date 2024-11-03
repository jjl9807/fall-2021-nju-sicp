test = {
  'name': 'sentences',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from sentences;
          The two siblings, barack plus clinton have the same size: standard
          The two siblings, abraham plus grover have the same size: toy
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
