
Guides
==========

This repository includes the code of the detailed guidelines for installing the MAZI toolkit starting from a plain Rasbian image. The corresponding web page is available here: http://nitlab.inf.uth.gr/mazi-guides/ 

In the wiki of this repository you can find additional documentation for quick installation, administrator manuals, and guidelines for deploying your MAZI Zone as described in detail here: https://github.com/mazi-project/guides/wiki 

Building Documentation
======================

This repository depends on [Sphinx]. You should install it first. The source files are in [ReStructutedText], and they live in `tech/source`.

Use the `Makefile` to automatically rebuild the documentation:

- `make clean` will remove the generated files.
- `make`       will regenerate the HTML files.

[Sphinx]: http://www.sphinx-doc.org/en/stable/
[ReStructuredText]: http://docutils.sourceforge.net/rst.html
