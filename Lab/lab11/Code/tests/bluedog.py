test = {
  'name': 'bluedog',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Clair De Lune
          blue|dog|Shake It Off
          blue|dog|Old Town Road
          blue|dog|Dancing Queen
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
