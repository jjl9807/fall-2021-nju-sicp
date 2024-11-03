test = {
  'name': 'wwsd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (has-even? s)
          ....        (cond ((null? s) #f)
          ....              ((even? (car s)) #t)
          ....              (else (has-even? (cdr-stream s)))))
          d5d26d71b33538ff9c54bcafe3230c1c
          # locked
          scm> (define (f x) (* 3 x))
          7613f748b4610f588bf7e49fa882a683
          # locked
          scm> (define nums (cons-stream 1 (cons-stream (f 3) (cons-stream (f 5) nil))))
          d5b69aa58f563d16001363e31fb698b1
          # locked
          scm> nums
          1a259ef5fb0378d36b7227df373908ea
          # locked
          scm> (cdr nums)
          bc2565820754c3d9d941d57f33d9a11c
          # locked
          scm> (cdr-stream nums)
          37f15a0e118239ec66ddba8059b7490a
          # locked
          scm> nums
          019dec1fd642bbe783ef5a6a968f6052
          # locked
          scm> (define (f x) (* 2 x))
          7613f748b4610f588bf7e49fa882a683
          # locked
          scm> (cdr-stream nums)
          37f15a0e118239ec66ddba8059b7490a
          # locked
          scm> (cdr-stream (cdr-stream nums))
          8506eed89fb30d57f4520ebe53ce5788
          # locked
          scm> (has-even? nums)
          a8905bfd67d7f806d212824718508db2
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
