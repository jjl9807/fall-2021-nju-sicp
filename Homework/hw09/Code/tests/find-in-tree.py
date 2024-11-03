test = {
  'name': 'find-in-tree',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (find-in-tree t1 0)
          ()
          scm> (find-in-tree t1 2)
          ((1 2))
          scm> (find-in-tree t1 3)
          ((1 2 3) (1 3))
          scm> (find-in-tree t1 7)
          ((1 2 7) (1 2 7 7) (1 6 7))
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
