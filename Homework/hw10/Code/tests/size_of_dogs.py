test = {
  'name': 'size_of_dogs',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from size_of_dogs;
          abraham|toy
          barack|standard
          clinton|standard
          delano|standard
          eisenhower|mini
          fillmore|mini
          grover|toy
          herbert|mini
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
