Build Status - master (This is stable branch): [![Build Status - master](https://travis-ci.org/BhallaLab/moose.svg?branch=master)](https://travis-ci.org/BhallaLab/moose)

Build Status - trunk (This is development branch) [![Build Status - trunk](https://travis-ci.org/BhallaLab/moose.svg?branch=trunk)](https://travis-ci.org/BhallaLab/moose)

# MOOSE

MOOSE is the Multiscale Object-Oriented Simulation Environment. It is designed
to simulate neural systems ranging from subcellular components and biochemical
reactions to complex models of single neurons, circuits, and large networks.
MOOSE can operate at many levels of detail, from stochastic chemical
computations, to multicompartment single-neuron models, to spiking neuron
network models.

MOOSE is multiscale: It can do all these calculations together. For example it
handles interactions seamlessly between electrical and chemical signaling.
MOOSE is object-oriented. Biological concepts are mapped into classes, and a
model is built by creating instances of these classes and connecting them by
messages. MOOSE also has classes whose job is to take over difficult
computations in a certain domain, and do them fast. There are such solver
classes for stochastic and deterministic chemistry, for diffusion, and for
multicompartment neuronal models.  MOOSE is a simulation environment, not just a
numerical engine: It provides data representations and solvers (of course!), but
also a scripting interface with Python, graphical displays with Matplotlib,
PyQt, and OpenGL, and support for many model formats. These include SBML,
NeuroML, GENESIS kkit and cell.p formats, HDF5 and NSDF for data writing.

# VERSION

This is MOOSE 3.0.2pre "Ghevar"

# ABOUT VERSION 3.0.2, Ghevar

The Ghevar release is the third of series 3 of MOOSE releases.

Ghevar is a Rajasthani sweet with a stiff porous body soaked in sugar syrup.

MOOSE 3.0.2pre is an evolutionary increment over 3.0.1::

- There has been substantial development on the multiscale modeling front, with
the implementation of the rdesigneur class and affiliated features. 
- MOOSE can now read NeuroMorpho .swc files natively.

# LICENSE

MOOSE is released under GPLv3.


# HOMEPAGE 

http://moose.ncbs.res.in/


# SOURCE REPOSITORY

https://sourceforge.net/projects/moose/


# REQUIREMENTS

## Core MOOSE

- g++ (>= 4.6.x)  REQUIRED For building the C++ MOOSE core.
- GSL (1.16.x) OPTIONAL For core moose numerical computation
- OpenMPI (1.8.x) OPTIONAL For running moose in parallel on clusters


## PyMOOSE                      REQUIRED except on cluster worker nodes

Python interface for core MOOSE API

- GSL     (1.16.x)                      REQUIRED For core moose numerical computation
- PyQt4         (4.8.x)                 REQUIRED For Python GUI    
- Matplotlib    ( >= 1.1.x)             REQUIRED For plotting simulation results
- SBML          (5.9.x)                 OPTIONAL For reading and writing signalling models to SBML files

### Compartmental Model Visualization       OPTIONAL



- GSL     (1.16.x)                      REQUIRED For core moose numerical computation
- OSG           (3.2.x)                 REQUIRED For 3D rendering and simulation of neuronal models
- Qt4           (4.8.x)                 REQUIRED For C++ GUI of Moogli
- PyQt4         (4.8.x)                 REQUIRED For Python GUI    
- Matplotlib    ( >= 1.1.x)             REQUIRED For plotting simulation results

# AUTHORS

- Upinder S. Bhalla     -   Primary Architect, Chemical kinetic solvers
- Niraj Dudani          -   Neuronal solver
- Subhasis Ray          -   PyMOOSE Design and Documentation, Python Plugin Interface, NSDF Format
- G.V.HarshaRani        -   Web page design, SBML support, Kinetikit Plugin Development
- Aditya Gilra          -   NeuroML reader development, integrate-and-fire neurons/networks, STDP
- Aviral Goel           -   Moogli/Neurokit Development
- Dilawar Singh         -   Packaging


# Support:

You can join the MOOSE generic mailing list for your queries -
https://lists.sourceforge.net/lists/listinfo/moose-generic


# Bugs:

You can file bug reports and feature requets at the sourceforge tracker -
http://sourceforge.net/p/moose/bugs/

# Getting started:

# Running MOOSE: the short short guide.
Moose is usually run within Python. Here is a template Python script that will
load and run various kinds of predefined model files:


    >>> import moose
    >>> help( moose ) # See what you can do with MOOSE.
    >>> moose.loadModel( file_path, modelname )	# Load in your model
    >>> moose.reinit()				# Set initial conditions
    >>> moose.start( runtime )			# Run the model

Using Matplotlib and a few more lines, one can plot the output of this 
simulation, which will have been been stored in tables somewhere in the model:

    >>> import pylab
    >>> import numpy
    >>> for x in moose.wildcardFind( '/modelname/##[ISA=Table]' ):
    >>>	t = numpy.arange( 0, x.vector.size, 1, ) * dt
    >>>	pylab.plot( t, x.vector, label = x.name )
    >>> pylab.legend()
    >>> pylab.show()


# Examples, tutorials and Demos: 

Look in the Demos directory for sample code. 

- Demos/tutorials: Standalone scripts meant for teaching. Students are expected
  to modify the scripts to learn the principles of the models.
- Demos/squid: The Hodkin-Huxley squid model, fully graphical interface.
- Demos/Genesis_files: A number of kinetics models used in MOOSE demos.
- Demos/neuroml: A number of NeuroML models used in MOOSE demos
- Demos/traub_2005: Example scripts for each of the individual cell models from
  the Traub 2005 thalamocortical model.
- Demos/snippets: Code snippets that can be used as building blocks and to
  illustrate how to use certain kinds of objects in MOOSE. These snippets are
  all meant to run as individual files.


# Supported file formats.

MOOSE comes with a NeuroML reader. Demos/neuroml has some python scripts showing
how to load NeuroML models.

MOOSE is backward compatible with GENESIS kinetikit.  Demos/Genesis_files has
some examples. You can load a kinetikit model with the loadModel function:

    moose.loadModel(kkit_file_path, modelname )

MOOSE is backward compatible with GENESIS <model>.p files used for neuronal
model specification. The same loadModel function can be used for this but you
need to have all the channels used in the .p file preloaded in /library:

    moose.loadModel(prototype_file_path, modelname )

MOOSE can also read .swc files from NeuroMorpho.org.

# Documentation

Top level moose documentation can be accessed in the Python interpreter the
usual way:

    import moose
    help(moose)


MOOSE classes have built-in documentation that can be accessed via
the `doc()` function -

    moose.doc(classname)

This will give the full documentation for the class including the fields
available.

    `moose.doc(classname.fieldname)` 

will give you information about a particular field in a class.

Complete MOOSE Documentation can be found at - 
http://moose.ncbs.res.in/content/view/5/6/
