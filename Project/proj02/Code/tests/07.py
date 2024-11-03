test = {
  'name': 'Problem 7',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_fixes("cats", "scat", big_limit)       # cats -> scats -> scat
          2
          >>> feline_fixes("purng", "purring", big_limit)   # purng -> purrng -> purring
          2
          >>> feline_fixes("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
          3
          >>> limit = 2
          >>> feline_fixes("ckiteus", "kittens", limit) > limit
          True
          >>> sphinx_swap("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
          True
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import feline_fixes, sphinx_swap
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
