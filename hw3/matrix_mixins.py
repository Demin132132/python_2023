import numpy as np
import numbers


class StrMixin():
    def __str__(self):
        return self.value.__str__()


class WriteMixin():
    def write(self, file_path):
        with open(file_path, 'w') as f:
            f.write(self.value.__str__())


class Value():
    def __init__(self, value):
        super().__init__()
        self.value = np.asarray(value)


class ArrayLike(np.lib.mixins.NDArrayOperatorsMixin, StrMixin, WriteMixin, Value):
    # взято из примера из документации
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Поддерживать операции только с экземплярами _HANDLED_TYPES.
            # Используйте ArrayLike вместо type (self) для isinstance to
            # разрешить подклассам, которые не переопределяют __array_ufunc__, в
            # обрабатывать объекты типа ArrayLike.
            if not isinstance(x, self._HANDLED_TYPES + (ArrayLike,)):
                return NotImplemented

        # Обратимся к реализации ufunc для развернутых значений.
        inputs = tuple(x.value if isinstance(x, ArrayLike) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, ArrayLike) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # несколько возвращаемых значений
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # нет возвращаемого значения
            return None
        else:
            # одно возвращаемое значение
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)


f = ArrayLike(1)
print(f)
print(f + 1)

m1 = ArrayLike(np.random.randint(0, 10, (10, 10)))
m2 = ArrayLike(np.random.randint(0, 10, (10, 10)))

print(m1+m2)

(m1+m2+1).write('artifacts/medium/matrix+.txt')
(m1*m2).write('artifacts/medium/matrix(mul).txt')
(m1@m2).write('artifacts/medium/matrix@.txt')
