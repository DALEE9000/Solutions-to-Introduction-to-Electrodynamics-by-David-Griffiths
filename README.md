# Solutions Manual: Introduction to Electrodynamics
**David J. Griffiths, 4th Edition**

Worked solutions to exercises from Griffiths' *Introduction to Electrodynamics*, typeset in LaTeX with TikZ diagrams.

## About

This solutions manual is a personal project developed as part of a self-directed study in classical electromagnetism. In my writing, I emphasize rigorous derivation and physical intuition, with extended commentary on the geometrical and physical interpretation of results where relevant — the vector calculus of Chapter 1, the structure of the field equations, and the conceptual payoffs Griffiths builds toward.

## Notation

Griffiths uses a lowercase script r (the "curly r") for the separation vector **𝓇** = **r** − **r**′ from source point to field point, with a regular-weight version for its magnitude. The symbol comes from the Kaufmann font; Griffiths distributes it himself:

- [Griffiths' script-r resource (Reed College)](http://academic.reed.edu/physics/faculty/griffiths/script_r.zip)

The solutions approximate it in LaTeX via the `calligra` package:

```latex
\usepackage{calligra}
\DeclareMathAlphabet{\mathcalligra}{T1}{calligra}{m}{n}
\DeclareFontShape{T1}{calligra}{m}{n}{<->s*[2.2]callig15}{}
\newcommand{\scriptr}{\mathcalligra{r}\,}          % magnitude
\newcommand{\boldscriptr}{\pmb{\mathcalligra{r}}\,} % separation vector
```
I have, however, made some modifications to the PDF image for better formatting. You may refer to the PDF files and the header document to see my implementation.

## Building

Compile with `pdflatex` or `latexmk`:

```bash
latexmk -pdf main.tex
```

## Disclaimer

These solutions are provided for educational purposes. This is an independent work and is not affiliated with or endorsed by the author or publisher. Some solutions may contain errors — use at your own discretion.

## License

MIT
