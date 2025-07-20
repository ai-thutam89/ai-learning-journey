.. AI-Learning-Journey 
.. Self-Experience
.. Read the Docs
.. RTD Tutorials
.. Latex - Markdown


Latex - Markdown
================
:Author: Sam Santa
:Date: |today|

.. warning::

   This is just a sample content, made for same publish for practice purpose.
   Please not to refer it for your real purpose.

Latex Docs
----------

These are best practices when writing and organizing docs on Read the Docs.

- Write in clear sections
- Use proper heading levels
- Keep filenames lowercase and consistent


Math Equations
--------------

Math is typeset using KaTeX. Inline math: :math:`f(x) = \int_{-\infty}^\infty \hat{f}(\xi)\,e^{2 \pi i \xi x} \, d\xi`

Display math is also supported:

.. math::

   f(n) = \begin{cases} 
      \frac{n}{2}, & \text{if } n\text{ is even} \\ 
      3n+1, & \text{if } n\text{ is odd} 
   \end{cases}

.. math::
   :name: Fourier transform

   (\mathcal{F}f)(y)
    = \frac{1}{\sqrt{2\pi}^{\ n}}
      \int_{\mathbb{R}^n} f(x)\,
      e^{-\mathrm{i} y \cdot x} \,\mathrm{d} x.

The ``:name:`` option puts a label on the equation that can be linked to
by hyperlink references. In this case, you could link back to the previous
math equation using the `Fourier transform`_ hyperlink reference.

.. list-table:: This is a long caption for table generated as at |today|
   :class: custom-table-widths
   :header-rows: 1
   :widths: auto

   * - Surname
     - Col. One
     - Col. Two
     - Col. Three
     - Col. Four
     - Col. Five
     - Col.Six
   * - Oliver
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6


Markdown
--------

Subjects
--------