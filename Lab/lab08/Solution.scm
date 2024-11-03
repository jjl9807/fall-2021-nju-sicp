;;; Lab08: Scheme

(define (over-or-under a b)
  (cond ((< a b) -1)
        ((= a b) 0)
        (else 1))
)


(define (make-adder n)
  (lambda (x) (+ x n))
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0) a (gcd b (remainder a b)))
)


(define lst
  '((1) 2 (3 4) 5)
)


(define (ordered s)
  (or (null? s) (null? (cdr s)) (and (<= (car s) (car (cdr s))) (ordered (cdr s))))
)
