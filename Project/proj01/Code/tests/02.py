test = {
  'name': 'Problem 2',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> picky_piggy(0)
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(1)
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(2)
          2fb5bd9d8cd23e16588e2242320006df
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(5)
          27d7ea0c1ef247eb4d13969601b324fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = picky_piggy(24)
          >>> a # check that the value is being returned, not printed
          12fb4058d6c28b6ccc056b1156595353
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(3)
          7
          >>> # ban str and indexing (lists)
          >>> test.check('hog.py', 'picky_piggy', ['Str', 'Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(64)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_piggy(12)
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
