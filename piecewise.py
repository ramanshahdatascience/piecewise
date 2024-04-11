#! /usr/bin/env python3

from collections import defaultdict
from numbers import Number

class ReluLC:
    def __init__(self, constant_term, *relu_terms):
        if not isinstance(constant_term, Number):
            raise ValueError('First (constant) argument must be a number')
        self.constant_term = constant_term

        if not all(len(term) == 2 for term in relu_terms) and \
                all(isinstance(term[0], Number) for term in relu_terms) and \
                all(isinstance(term[1], Number) for term in relu_terms):
            raise ValueError('ReLU arguments must be numerical (coefficient, offset) pairs')

        # Simplify linear combination of ReLUs on initialization: sort by
        # offset, simplify terms with the same offset, and drop zeros
        term_groups = defaultdict(list)
        for term in relu_terms:
            term_groups[term[1]].append(term[0])
        offsets = sorted(term_groups.keys())
        terms_with_zeros = tuple((sum(term_groups[offset]), offset) for offset in offsets)
        self.relu_terms = tuple((term[0], term[1]) for term in terms_with_zeros if term[0] != 0)

    def __repr__(self):
        return f'ReluLC({self.constant_term}, {self.relu_terms})'

    def __add__(self, other):
        if isinstance(other, Number):
            return ReluLC(self.constant_term + other, *(self.relu_terms))
        elif isinstance(other, ReluLC):
            return ReluLC(self.constant_term + other.constant_term, *(self.relu_terms + other.relu_terms))
        else:
            raise ValueError('ReluLC objects can only be added to others or to scalars')

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Number):
            self.constant_term += other
        elif isinstance(other, ReluLC):
            self.constant_term += other.constant_term

            term_groups = defaultdict(list)
            for term in (self.relu_terms + other.relu_terms):
                term_groups[term[1]].append(term[0])
            offsets = sorted(term_groups.keys())
            terms_with_zeros = tuple((sum(term_groups[offset]), offset) for offset in offsets)
            self.relu_terms = tuple((term[0], term[1]) for term in terms_with_zeros if term[0] != 0)
        else:
            raise ValueError('ReluLC objects can only be added to others or to scalars')

        return self

    def __neg__(self):
        neg_terms = tuple((-term[0], term[1]) for term in self.relu_terms)
        return ReluLC(-self.constant_term, *neg_terms)

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __mul__(self, other):
        if isinstance(other, Number):
            new_terms = ((term[0] * other, term[1]) for term in self.relu_terms)
            return ReluLC(other * self.constant_term, *new_terms)
        else:
            raise ValueError('Only scalar multiplication is defined')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, Number):
            self.constant_term *= other
            self.relu_terms = tuple((other * term[0], term[1]) for term in self.relu_terms)
        else:
            raise ValueError('Only scalar multiplication is defined')

        return self

    def __call__(self, x):
        active_terms = [term for term in self.relu_terms if x >= term[1]]
        return self.constant_term + sum(term[0] * (x - term[1]) for term in active_terms)

    def excel_formula(self, target_cell):
        parts = ['=']

        if self.constant_term != 0:
            parts.append(str(self.constant_term))

        for i, relu_term in enumerate(self.relu_terms):
            if i == 0:
                parts.append('{:} * IF({:s} > {:}, {:s} - {:}, 0)'\
                        .format(relu_term[0], target_cell, relu_term[1],
                                target_cell, relu_term[1]))
            elif relu_term[0] < 0:
                parts.append('- {:} * IF({:s} > {:}, {:s} - {:}, 0)'\
                        .format(-1 * relu_term[0], target_cell, relu_term[1],
                                target_cell, relu_term[1]))
            else:
                parts.append('+ {:} * IF({:s} > {:}, {:s} - {:}, 0)'\
                        .format(relu_term[0], target_cell, relu_term[1],
                                target_cell, relu_term[1]))

        return ' '.join(parts)

    def excel_derivative(self, target_cell):
        parts = ['=']

        terms = ['IF({:} > {:}, {:}, 0)'.format(target_cell, relu_term[1], relu_term[0])
                 for relu_term in self.relu_terms]

        parts.append(' + '.join(terms))

        return ' '.join(parts)

if __name__ == '__main__':
    x = ReluLC(1, [2, 3], [4, 5])

    # Test attributes, __repr__,  __call__
    print(x)
    print(x.constant_term)
    print(x.relu_terms)
    print(x(10))

    # Test __add__, __radd__, __iadd__
    y = ReluLC(0, [6, 7])
    print(x + y)
    print(x + 6)
    print(6 + x)
    y += x
    print(y)

    # Test __mul__, __rmul__, __imul__
    print(x * 2)
    print(2 * x)
    z = x
    z *= 2
    print(z)

    # Test simplification
    print(x - x)
