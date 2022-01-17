;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (cond ((= total 0) '(()))
        ((or (< total 0) (= biggest 0)) nil)
        (else (append 
                (map 
                  (lambda (lst) (cons biggest lst)) 
                  (make-change (- total biggest) biggest)) 
                (make-change total (- biggest 1)))))
)


(define (find n lst)
  (define (find-tail i n curr)
    (if (or (null? curr) (= n (car curr))) i (find-tail (+ i 1) n (cdr curr))))
  (find-tail 0 n lst)
)


(define (find-nest n sym)
  (define (helper lst expr)
    (if (pair? lst)
      (let ((r1 (helper (car lst) (list 'car expr))))
        (if (null? r1) (helper (cdr lst) (list 'cdr expr)) r1))
      (if (and (number? lst) (= n lst)) expr nil)))
  (helper (eval sym) sym)
)


(define-macro (def func args body)
  `(define ,(cons func args) ,body)
)


(define-macro (k-curry fn args vals indices)
  `(lambda ,(remove args indices 0) ,(cons fn (replace args vals indices 0)))
)

(define (remove lst indices curr)
  (cond ((or (null? lst) (null? indices)) lst)
        ((= curr (car indices)) (remove (cdr lst) (cdr indices) (+ 1 curr)))
        (else (cons (car lst) (remove (cdr lst) indices (+ 1 curr))))))

(define (replace lst vals indices curr)
  (cond ((or (null? lst) (null? indices)) lst)
        ((= curr (car indices)) 
          (cons (car vals) (replace (cdr lst) (cdr vals) (cdr indices) (+ 1 curr))))
        (else (cons (car lst) (replace (cdr lst) vals indices (+ 1 curr))))))


(define-macro (let* bindings expr)
  (if (null? bindings) `(let ,bindings ,expr)
    `(let (,(car bindings)) (let* ,(cdr bindings) ,expr)))
)

;;; Just For Fun Problems

; Tree ADT
(define (tree label branches) (cons label branches))
(define (label t) (car t))
(define (branches t) (cdr t))
(define (is-leaf t) (null? (branches t)))

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 3 nil)
        (tree 7 (list
          (tree 7 nil)))))
    (tree 3 nil)
    (tree 6
      (list
        (tree 7 nil))))))

(define (find-in-tree t goal)
  (reduce append 
          (cons (if (= (label t) goal) `((,goal)) nil) 
                (map (lambda (b) (map (lambda (lst) (cons (label t) lst))
                                      (find-in-tree b goal))) 
                     (branches t))))
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

; Just solve 8.1 and 8.2, very simple
(define-macro (infix-simple expr)
  (if (pair? expr) 
      `(,(cadr expr) (infix-simple ,(car expr)) (infix-simple ,(caddr expr)))
      expr))

; Solve the whole p8
(define-macro (infix expr)
  (infix-cal expr)
)

(define (infix-cal expr)
  (if (pair? expr)
    (if (null? (cdr expr)) (infix-cal (car expr)) 
      (let ((left (infix-cal (car expr)))
            (operator (cadr expr))
            (right (cddr expr)))
        (if (eq? operator '+)
          (+ left (infix-cal right))
          (infix-cal (cons (* left (infix-cal (car right))) (cdr right))))))
    (eval expr)))

