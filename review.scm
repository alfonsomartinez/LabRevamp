;
; Where's Waldo 
;

(define (waldo-tail lst)
	(define (helper lst index)
		(cond ((null? lst) 'nowhere)
			  ((equal? 'waldo (car lst)) index)
			  (else (helper (cdr lst) (+ index 1)))))
	(helper lst 0))









;
; Fibonacci
;

(define (fib n)
	(define (helper k prev curr)
		(if (= k n)
			curr
			(helper (+ k 1) curr (+ curr prev))))
	(if (= n 1)
		0
		(helper 2 0 1)))








;
; Map
;

(define (map fn lst)
	(define (map-help lst so-far)
		(if (null? lst lst)
			so-far
			(map-help (cdr last) (append so-far 
										(list (fn(car lst)))))))
	(map-help lst nil))









;
; Remove
;

(define (remove lst item)
	(define (helper lst so-far)
		(cond ((null? lst) so-far)
			  ((eq? (car lst) item) (append so-far (cdr lst)))
		(else (helper (cdr lst) (append so-far (list (car lst)))))))
	(helper lst nil))
















;
; Swap
;

; scm> (swap (list 1 2 3 4))
; (2 1 4 3)
; scm> (swap (list 1 2 3 4 5))
; (2 1 4 3 5)

(define (swap s)
  (define (helper sofar rest)
    (cond ((null? rest) sofar)
          ((null? (cdr rest)) (append sofar (list (car rest))))
          (else (helper (append sofar (list (car (cdr rest)) (car rest)))
                        (cdr (cdr rest))))))
  (helper () s))









