import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms
from scheme_classes import *

##############
# Eval/Apply #
##############



def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest

    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        op = scheme_eval(first, env)
        validate_procedure(op)

        if isinstance(op, MacroProcedure):  # MacroProcedure is not a `pure` string-subst
            thunk = scheme_apply(op, rest, env)   # `scheme_apply` can bind expression to variable
            if isinstance(thunk, Unevaluated):
                result = scheme_eval(thunk.expr, thunk.env)
                return Unevaluated(result, env)
            else:
                return scheme_eval(thunk, env)

        def eval_operand(operand):
            return scheme_eval(operand, env)
        operands = rest.map(eval_operand)
        return scheme_apply(op, operands, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        def scmlist2pylist(args):
            ret = []
            while args != nil:
                ret.append(args.first)
                args = args.rest
            return ret
        pyargs = scmlist2pylist(args)
        if procedure.expect_env:
            pyargs.append(env)
        try:
            return procedure.py_func(*pyargs)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # print(f"p = {procedure}, args = {args}")
        # print(f"f = {procedure.formals}, b = {procedure.body}")
        child_frame = procedure.env.make_child_frame(procedure.formals, args)
        # print(f"env = {env}, penv = {procedure.env}, cenv = {child_frame}")
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # print('DEBUG:', procedure, procedure.formals, args)
        child_frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)

def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions == nil:
        return None
    if expressions.rest == nil:
        return scheme_eval(expressions.first, env, True)
    else: 
        scheme_eval(expressions.first, env)
        return eval_all(expressions.rest, env)
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        while isinstance(result, Unevaluated):
            result = original_scheme_eval(result.expr, result.env)  # no nested env is needed for tail
        return result 
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = optimize_tail_calls(scheme_eval)
