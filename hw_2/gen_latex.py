from functools import reduce


start_document = \
r'''
\documentclass{article}
\begin{document}
\begin{center}
\begin{tabular}{ c c c }
'''
end_document = \
'''
\end{tabular}
\end{center}
\end{document}
'''


def foo(l):
    with open('./artifacts/table.tex', 'w') as file:
        file.write(start_document)
        list(map(
            lambda x: file.write(
                str(
                    reduce(
                        lambda c, d: str(c) + ' & ' + str(d),
                        x,
                    )
                ) + ' \\\\\n'
            ),
            l,
        ))
        file.write(end_document)


if __name__ == '__main__':
    foo([[1,2,3], [4,5,6], [7,8,9]])
