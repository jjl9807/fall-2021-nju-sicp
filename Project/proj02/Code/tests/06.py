test = {
  'name': 'Problem 6',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_swap("car", "cad", big_limit)
          1
          >>> sphinx_swap("this", "that", big_limit)
          2
          >>> sphinx_swap("one", "two", big_limit)
          3
          >>> sphinx_swap("awful", "awesome", 3) > 3
          True
          >>> sphinx_swap("awful", "awesome", 4) > 4
          True
          >>> from construct_check import check
          >>> # ban while or for loops
          >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
          True
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import sphinx_swap
      >>> HW_SOURCE_FILE = 'cats.py'
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
