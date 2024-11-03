;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
      (if (f (car s))
          (cons-stream (car s) (filter-stream f (cdr-stream s)))
          (filter-stream f (cdr-stream s)))))


(define (slice s start end)
  (cond ((or (null? s) (= end 0)) nil)
        ((= start 0) (cons (car s) (slice (cdr-stream s) 0 (- end 1))))
        (else (slice (cdr-stream s) (- start 1) (- end 1))))
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
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)


(define (exp x)
  (cons-stream 1 (combine-with +
                               (exp x)
                               (combine-with (lambda (b c) (/ (expt x c) b))
                                             (cdr-stream factorials)
                                             (naturals 1))))
)


(define (nondecrease s)
  (cond ((null? s) nil)
        ((null? (cdr-stream s)) (cons-stream (list (car s)) nil))
        (else (if (> (car s) (car (cdr-stream s)))
                  (cons-stream (list (car s)) (nondecrease (cdr-stream s)))
                  (let ((rest (nondecrease (cdr-stream s))))
                    (cons-stream (cons (car s) (car rest)) (cdr-stream rest))))))
)

(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))

;;; Just For Fun Problems

(define-macro (my-cons-stream first second)
  `(list ,first (lambda () ,second))
)

(define (my-car stream)
  (car stream)
)

(define (my-cdr-stream stream)
  ((car (cdr stream)))
)


(define (sieve s)
  (cons-stream (car s)
    (sieve (filter-stream (lambda (x) (< 0 (remainder x (car s)))) (cdr-stream s))))
)

(define primes (sieve (naturals 2)))
