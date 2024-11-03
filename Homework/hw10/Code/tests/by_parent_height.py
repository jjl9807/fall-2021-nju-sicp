test = {
  'name': 'by_parent_height',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM by_parent_height ORDER BY 1;
          abraham
          barack
          clinton
          delano
          fillmore
          grover
          herbert
          sqlite> SELECT height FROM by_parent_height, parents, dogs WHERE by_parent_height.name = parents.child AND parents.parent = dogs.name;
          46
          35
          32
          32
          32
          26
          26
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
