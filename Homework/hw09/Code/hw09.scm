;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  'YOUR-CODE-HERE
)


(define (find n lst)
  'YOUR-CODE-HERE
)


(define (find-nest n sym)
  'YOUR-CODE-HERE
)


(define-macro (def func args body)
  ''YOUR-CODE-HERE
)


(define-macro (k-curry fn args vals indices)
  ''YOUR-CODE-HERE
)


(define-macro (let* bindings expr)
  ''YOUR-CODE-HERE
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
  'YOUR-CODE-HERE
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  ''YOUR-CODE-HERE
)
