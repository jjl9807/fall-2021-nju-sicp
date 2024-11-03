test = {
  'name': 'Problem 2',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
          'Cute Dog!'
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
          'Nice pup.'
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('"DOGS" stands for Department of Geophysical Science.')
          True
          >>> dogs("Do gs and ho unds don't count")
          False
          """,
          'hidden': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose, about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
