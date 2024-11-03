test = {
  'name': 'WWPD',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          608d4b7c88f747e4c5e36fd6dcbd0e5e
          # locked
          >>> next(t)
          4894ffd03a6336c8736241f591654e3f
          # locked
          >>> next(t)
          7568c556adea42382814d931fb39ed5b
          # locked
          >>> iter(s)
          2cbe6bafa533c42b71af54dc736560a7
          # locked
          >>> next(iter(s))
          4894ffd03a6336c8736241f591654e3f
          # locked
          >>> next(iter(t))
          e336bb46343de175eb933c183c5bdc4d
          # locked
          >>> next(iter(s))
          4894ffd03a6336c8736241f591654e3f
          # locked
          >>> next(iter(t))
          f8eef8f42b4b46c1669a8575cf34e74c
          # locked
          >>> next(t)
          54fbf1670d96e8ef3e22953ae3fe0948
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          28b7d8a940d2c564b28c81f880710c44
          # locked
          >>> [x + 1 for x in r]
          480ba5f1ecb4fcbe67a917c68ebded6d
          # locked
          >>> [x + 1 for x in r_iter]
          1daf1206d8acfa187ff314fe9adc0029
          # locked
          >>> next(r_iter)
          54fbf1670d96e8ef3e22953ae3fe0948
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          a5d3a1c0eca9d58a0b4cfb5b6555b1ba
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          942f5721c7c684c82af9e11c10c87be5
          # locked
          >>> next(map_iter)
          1bcbd88a18bc02d5f49ceca45472be73
          # locked
          >>> list(map_iter)
          189180fad33c7cd91412e3a53ef5bf5f
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          2be94fcb188929268b035efd8d67caf5
          fd9b13087592fb410158e3edf16ce3c2
          34cba5e447d4f3fbc5ece92283e8ebdb
          67e3edefb6eb42c9f81a05f838353029
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          2ff2c3c254ed01b52cb747375cbd4b18
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          9feb9e4fccd133d73f259a3841a5e53b
          cb178823229cffeb2b29f93dc6fed939
          945cd0879eface82dda41c81cc850a36
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
