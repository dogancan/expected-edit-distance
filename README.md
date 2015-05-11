# expected-edit-distance
Expected edit distance implementation using OpenFst tools.

We use the following algorithm for computing the expected edit distance between
two acyclic probabilistic finite state automata `X` and `Y` over the log semiring:

    D(X,Y) = shortestDistLog(-detTrop(-removeEpsTrop(synchronize(detLog(X o T o Y)))))

where `T` is the weighted transducer over the log semiring representing the
edit cost function.

Original algorithm is from [Mehryar Mohri. "Edit-distance of weighted automata:
General definitions and algorithms." International Journal of Foundations of
Computer Science, 14(6):957-982, 2003.](www.cs.nyu.edu/~mohri/pub/edit.pdf).
There is a small difference between the algorithm in the paper and the one
implemented here. We perform the epsilon removal operation under the tropical
semiring instead of log semiring.

