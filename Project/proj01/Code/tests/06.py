test = {
  'name': 'Problem 6',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'answer': 'f4ac841b5b4bcb4d3bed284935cb6df7',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          eecac3acba4273aa168a0f8b728706d4
          3f8dee6bd7ee4f91896df15c0c775f47
          062a58753e35198c7a37b1656d84f8e4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(1), goal=3, say=count(1))
          18df35c05e8d52b0f1a5238a7a392deb
          8f70d2b18663ec9cb21395498050fb32
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          b03be06a76a9fbb41817561b7a10fe13
          fa52b212047afc9379ebf7cdd30edc0c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
          eecac3acba4273aa168a0f8b728706d4
          754e0ae22708be05fbf602cefede6d63
          54cdbe12bce16c5b57ba6aa1c3c4d134
          ed18f9abdbe3f265817c0558d826a4f5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          39c88789458170e6f6ff2ae2f5df9fe9
          10950c9024f19782cd382eeebd4d7ff7
          39c88789458170e6f6ff2ae2f5df9fe9
          5817865e305847b168146d5d83f2e087
          63c75d1bf5008bf7ba0dbba401d1da84
          5817865e305847b168146d5d83f2e087
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          e713c9b3f50d8bed6897c81a3655f4c6
          a4f9f0e0c3c118cc96d084fbf154e922
          7937f86b5caf880ffa4199c732caf1dd
          a575607a9c8bb02961bf29075ffa5ebf
          a0371163ed2f962708c1f7b9418816b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
