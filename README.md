# expected-edit-distance
Expected edit distance implementation using OpenFst tools.

We use the following algorithm for computing the expected edit distance between
two acyclic probabilistic finite state automata `X` and `Y` over the log
semiring:

    D(X,Y) = ShortestDistLog(-DetTrop(RmEpsTrop(Sync(-DetLog(X o T o Y)))))

where `T` is a weighted transducer over the log semiring representing the
edit cost function.

Original algorithm is from [Mehryar Mohri. "Edit-distance of weighted automata:
General definitions and algorithms." International Journal of Foundations of
Computer Science, 14(6):957-982, 2003.](www.cs.nyu.edu/~mohri/pub/edit.pdf).
There are a few small differences between the algorithm in the paper and the one
implemented here. We perform the epsilon removal operation under the tropical
semiring with inverted weights instead of log semiring with regular weights.
Also, we insert very high cost self mapping arcs to `T`, which end up as very
low cost arcs when weights are inverted, so that if `X` and `Y` accept the same
string `x`, then `D(x,x) ≈ 0`.

