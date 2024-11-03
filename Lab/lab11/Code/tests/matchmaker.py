test = {
  'name': 'matchmaker',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker;
          dog|Clair De Lune|blue|green
          dog|Clair De Lune|blue|purple
          cat|Shake It Off|white|#ccff00
          dragon|STAY|turquoise|green
          cat|Shelter|green|pink
          cat|Shelter|green|blue
          horse|Shake It Off|deep blue|green
          cat|Shelter|pink|blue
          dog|Clair De Lune|green|purple
          tiger|STAY|red|blue
          cat|All I want for Christmas|blue|don't have one
          dog|Dancing Queen|black|red
          dog|Dancing Queen|black|blue
          dog|Dancing Queen|red|blue
          panda|STAY|purple|green
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
