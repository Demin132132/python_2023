document = \
r'''
\documentclass{article}
\begin{document}

\usepackage{graphicx}
\graphicspath{ {artifacts/} }

\includegraphics{img}
\end{document}
'''

with open('./artifacts/img.tex', 'w') as file:
    file.write(document)
