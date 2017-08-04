def hide_last_exception(hidden_depth=1):
    # we're going to raise a custom error to show where the problem is
    # manipulating the stack trace so the resulting error is more helpful
    import sys
    import traceback

    # we're hooking exception handler to trim out one level of stack trace
    def excepthook(type, value, tb):
        depth = 0
        current = tb

        # walk to the bottom of the trace and report depth
        while current:
            depth += 1
            current = current.tb_next

        # print the error minus the final (this current) line
        traceback.print_exception(type, value, tb, depth-hidden_depth)

    # replace the hook
    sys.excepthook = excepthook
