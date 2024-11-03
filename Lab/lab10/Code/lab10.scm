;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
      (let ((rest (filter-stream f (cdr-stream s))))
        (if (f (car s))
            (cons-stream (car s) rest)
            rest))))


(define (slice s start end)
  'YOUR-CODE-HERE
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  'YOUR-CODE-HERE
)


(define fibs
  'YOUR-CODE-HERE
)


(define (exp x)
  'YOUR-CODE-HERE
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  'YOUR-CODE-HERE
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
