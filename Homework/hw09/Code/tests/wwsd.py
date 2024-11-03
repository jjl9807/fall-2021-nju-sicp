test = {
  'name': 'wwsd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> +
          4ba5cb09891b9dfb738f7986480c59ae
          # locked
          scm> list
          85eb03715016972885b10ff539af5fdf
          # locked
          scm> (define-macro (f x) (car x))
          7613f748b4610f588bf7e49fa882a683
          # locked
          scm> (f (2 3 4)) ; type SchemeError for error, or Nothing for nothing
          d44ff701a104143cacd428269278ccd4
          # locked
          scm> (f (+ 2 3))
          4ba5cb09891b9dfb738f7986480c59ae
          # locked
          scm> (define x 2000)
          5f8f28b8acb2d3a9ca4afddd2966fbc4
          # locked
          scm> (f (x y z))
          dbf7f8d9b0dd65eae2624120cd45bfa5
          # locked
          scm> (f (list 2 3 4))
          85eb03715016972885b10ff539af5fdf
          # locked
          scm> (f (quote (2 3 4)))
          a8beb1c43e936a2f6bcf0575635dd69c
          # locked
          scm> (define quote 7000)
          d7a8909accbce0fc471ae38bb988be54
          # locked
          scm> (f (quote (2 3 4)))
          7734425bed2c9dee05ff0b2277065263
          # locked
          scm> (define-macro (g x) (+ x 2))
          f4d169cd84fa353038885b6258ffb058
          # locked
          scm> (g 2)
          17876b77ec1f2cc9ff1cf38c061a1abe
          # locked
          scm> (g (+ 2 3))
          a8beb1c43e936a2f6bcf0575635dd69c
          # locked
          scm> (define-macro (h x) (list '+ x 2))
          a1c88cb8cb65165ca6525011130c50b6
          # locked
          scm> (h (+ 2 3))
          c1496209745bed936d500634d684251c
          # locked
          scm> (define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))
          6d9db09bfc6cbe181b113b9e3184e0cf
          # locked
          scm> (if-else-5 #t 2)
          d44ff701a104143cacd428269278ccd4
          # locked
          scm> (if-else-5 #f 3)
          49e220a0dc988559bc3c5c52995f30ab
          # locked
          scm> (if-else-5 #t (/ 1 0))
          a8beb1c43e936a2f6bcf0575635dd69c
          # locked
          scm> (if-else-5 #f (/ 1 0))
          49e220a0dc988559bc3c5c52995f30ab
          # locked
          scm> (if-else-5 (= 1 1) 2)
          d44ff701a104143cacd428269278ccd4
          # locked
          scm> '(1 x 3)
          cb752db345171f7ef317e86ad1f5c223
          # locked
          scm> (define x 2)
          5f8f28b8acb2d3a9ca4afddd2966fbc4
          # locked
          scm> `(1 x 3)
          cb752db345171f7ef317e86ad1f5c223
          # locked
          scm> `(1 ,x 3)
          cacb5f60c723c90cca9231952300e7bb
          # locked
          scm> '(1 ,x 3)
          09c20f70130acdf8fbe04a4142529465
          # locked
          scm> `(,1 x 3)
          cb752db345171f7ef317e86ad1f5c223
          # locked
          scm> `,(+ 1 x 3)
          939c49c5ed2fe64b83adc3010e7ead0c
          # locked
          scm> `(1 (,x) 3)
          78ea67ccf48edf9411bb676b57129515
          # locked
          scm> `(1 ,(+ x 2) 3)
          a4da369fbda3f755d2be4b21e3d23b1f
          # locked
          scm> (define y 3)
          a0273ae372d9c932a524443a9ca3a545
          # locked
          scm> `(x ,(* y x) y)
          329afd3b1e002e20e86609b621c19c4d
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          3736a883d918495da82f933bd6432914
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
