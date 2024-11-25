# UTPB-COSC-3310-Test2
This repo contains a Python-based automatic test generation script, which randomly generates values for the Final and plugs them into a LaTeX document skeleton for rendering.

Note:
* This project requires that you install the pyparsing and schemdraw packages.  If the requirements.txt file is not picked up by your IDE you may have to install them via some other means.
* In order to get the file to compile correctly in your LaTeX compiler, you will need to upload all of the .svg files or store them in the correct directory.
* The and.svg, or.svg etc files are the same every time the script runs, but the circuit1 and circuit2 files are generated dynamically.  This means you will need to overwrite the files for each newly generated practice test.