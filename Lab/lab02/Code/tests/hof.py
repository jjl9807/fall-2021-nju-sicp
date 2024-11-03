test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> steven = lambda x: x
          >>> stewart = even(steven)
          >>> stewart
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> stewart(61)
          8172f1db1cfeec62d758dc7d4734f853
          # locked
          >>> stewart(-4)
          b2c695bc3b980a62202ceceb03bee56f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          44cd1432120a6eb46c3f5a05d1da4510
          # locked
          >>> chocolate
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> chocolate()
          9efeae4fa136883ec4b2ed6f9672d4ba
          29afcce4e82f33fe0fa96c31b155fdad
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          9efeae4fa136883ec4b2ed6f9672d4ba
          # locked
          >>> more_chocolate
          29afcce4e82f33fe0fa96c31b155fdad
          # locked
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          36a08b27428b4f46661e44032fbc1e46
          # locked
          >>> snake(10, 20)()
          9efeae4fa136883ec4b2ed6f9672d4ba
          29afcce4e82f33fe0fa96c31b155fdad
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          3b992504c5ed5ef1914c4ba5ec2c979f
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
