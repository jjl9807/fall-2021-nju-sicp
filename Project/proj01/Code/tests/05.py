test = {
  'name': 'Problem 5',
  'points': 400,
  'suites': [
    {
      'cases': [
        {
          'answer': '65ea24a4f765643d858ab7ca8f668d8e',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'ac0e08c5591c6b9c23602ccf446bf6ab',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': 'bb921813009fe56fd309f9d1b9116552',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
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
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
          >>> s0
          80f32db00fef9c728b0fb3ba241e1fdb
          # locked
          >>> s1
          eec979b1214e3645f3f9a2f6565eae70
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
          >>> s0
          be4a1be13b1c8619088ba7e6b10abd62
          # locked
          >>> s1
          0b19e2d0e0e3a7972243801cf8e912eb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Hint: use Python!
          >>> s0, s1 = hog.play(always(3), always(5), goal=20, dice=always_four)
          >>> s0
          2090485a62474fb3135db1ef936504d2
          # locked
          >>> s1
          be4a1be13b1c8619088ba7e6b10abd62
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_four = hog.make_test_dice(4)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Use strategies
          >>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
          >>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
          >>> s0
          5b654ceb97bdbc1192a6afd624f0cc94
          # locked
          >>> s1
          437fd3ade14b6ccf4bd8a776db8d77c8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_seven = hog.make_test_dice(7)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Player 0 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=88, score1=87, dice=always_three)
          >>> s0
          91052584d7b24cb1203d1a140e7e4764
          # locked
          >>> s1
          3e7570fcc1240bcc77500114f29d7c48
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Picky piggy refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=5, score1=96, dice=always_three)
          >>> s0
          ede5516ab4a5bf350b845ed0cc751b12
          # locked
          >>> s1
          91052584d7b24cb1203d1a140e7e4764
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s0, s1 = hog.play(always(1), always(1), goal=25, dice=hog.make_test_dice(5, 22, 8, 1, 2, 6, 3))
          >>> s0
          be4a1be13b1c8619088ba7e6b10abd62
          # locked
          >>> s1
          2090485a62474fb3135db1ef936504d2
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
