test = {
  'name': 'combinations',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (- 10 4)
          f43a983c0daf6c1d050dbe0833c15187
          # locked
          scm> (* 7 6)
          9f2845c08838e3d74a4a825544551738
          # locked
          scm> (+ 1 2 3 4)
          3ec9872f57999918aff6256a4468475f
          # locked
          scm> (/ 8 2 2)
          12ff846b5df2ea6bda9ece2c27d4e07d
          # locked
          scm> (quotient 29 5)
          14b862d1cc1ac887a348e7877803d91c
          # locked
          scm> (modulo 29 5)
          35335a4cb21b81bbdd7c9fde450ac2ba
          # locked
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          1d68a21f5e10a0b34e0e72d9ed47796f
          # locked
          scm> (< 1 3)
          2d7cbeef49a0612644978f75b0aff19d
          # locked
          scm> (or 1 #t)                  ; or special form short circuits
          ab602226889628a880f560d548c9532f
          # locked
          scm> (and #t #f (/ 1 0))
          1d68a21f5e10a0b34e0e72d9ed47796f
          # locked
          scm> (not #t)
          1d68a21f5e10a0b34e0e72d9ed47796f
          # locked
          scm> (define x 3)
          556d7474b05028c5f33a8dbe76672010
          # locked
          scm> x
          331378a62fb7d46a780484bd24dd9bc4
          # locked
          scm> (define y (+ x 4))
          6b3fe8d55a9adf0d4813e02496ddad7d
          # locked
          scm> y
          d389f94a5f34049b2a7d5ca263c63628
          # locked
          scm> (define x (lambda (y) (* y 2)))
          556d7474b05028c5f33a8dbe76672010
          # locked
          scm> (x y)
          92a7d397a794074ba6a711853088fe9d
          # locked
          scm> (if (not (print 1)) (print 2) (print 3))
          ab602226889628a880f560d548c9532f
          331378a62fb7d46a780484bd24dd9bc4
          # locked
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          6b20a778cd26fa9470e9c7c675e76925
          # locked
          scm> (define foo (lambda (x y z) (if x y z)))
          cd6dbf3fc5fa76db00b4a63b6f47a298
          # locked
          scm> (foo 1 2 (print 'hi))
          e5a021da3be17dba99a7c815cf974c33
          12ff846b5df2ea6bda9ece2c27d4e07d
          # locked
          scm> ((lambda (a) (print 'a)) 100)
          cc8f26e398984759770a00540b27b1c9
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
