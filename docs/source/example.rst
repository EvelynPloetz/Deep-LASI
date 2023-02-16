Example Galleries
=====

.. _example:

Deep-LASI can be employed for different single-molecule assays. In this gallery, we provide a short intro on how to get started and
use Deep-LASI for the different single-molecule assays. Eample data are provided together with each show case.
Please **click on the different images** or follow the respective links to visit the corresponding example pages. 

.. One-color assays
.. ------------------

.. Single-color bleaching step analysis
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Proteins are frequently functioning as oligomers. Photobleaching step analysis allows for investigating the stoichiometry of a particular protein of interest in a molecular assembly, or determining the labeling efficiency of a single protein. Deep-LASI localizes the biomolecule, extract the fluroescence trajectory, analyzes potential bleaching steps by an automated step finding algorithm and determins the number of itensity levels, their brightness and time spend in the different states.

.. .. image:: ./../figures/examples/Steps_Figure.png
   :target: ./examples/example-steps.rst
   :width: 800
   :alt: Bleaching Step Analysis
   :align: center

.. PAINT: Dwell time analysis
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. In DNA-PAINT, fluorescently labeled *imager strands* transiently bind to complementary *docking strands* on a target structure.
.. Besides sequence-based multiplexing, variation of binding time and binding frequency allow for visualizing multiple distinct molecular species within a single sample via DNA-PAINT. Deep-LASI allows for extracting time traces and fluorescence characteristics, to determine the ON- and OFF-times associated with time the imager strand spends in the bound state τ :sub:`b` or diffusing τ :sub:`d` in solution according to the chosen DNA sequence.

.. .. image:: ./../figures/examples/PAINT_Figure.png
   :target: https://deep-lasi-tutorial.readthedocs.io/en/latest/examples/example-paint.html
   :width: 500
   :alt: PAINT assay
   :align: center

.. --------------------------------------------------------------------

Two-color assays
------------------

Static 2c FRET
~~~~~~~~~~~~~~~~

The following example on :doc:`./examples/example-2c-FRET-Static` describes how to analyse single-molecule FRET occurring between a donor and an acceptor, which are positioned at two fixed distances apart using alternating laser excitation (ALEX).

.. We discuss two examples for publicly available sample data from `Hellenkamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_ and `Götz et al., Nat. Meth (2022) <https://www.nature.com/articles/s41467-022-33023-3>`_.

.. image:: ./../figures/examples/Static_Twoc_ALEX.png
   :target: https://deep-lasi-tutorial.readthedocs.io/en/latest/examples/example-2c-FRET-Static.html
   :width: 500
   :alt: Static 2c FRET Analysis with ALEX
   :align: center

|

Dynamic 2c FRET
~~~~~~~~~~~~~~~~~

The following section describes how to analyse dynamic 2c FRET data using Deep-LASI for alternating laser excitation (ALEX). 

.. image:: ./../figures/examples/Dynamic_2c_ALEX.png
   :target: https://deep-lasi-tutorial.readthedocs.io/en/latest/examples/example-2c-FRET-Dynamic.html
   :width: 800
   :alt: Dynamic 2c FRET Analysis with ALEX
   :align: center

|

--------------------------------------------------------------------

Three-color assays
--------------------

Dynamic 3c FRET
~~~~~~~~~~~~~~~~~
In this example, we show how to analyse dynamic 3c FRET data using Deep-LASI for alternating laser excitation (ALEX). As example we investigate an dynamic DNA origami structure, that is labeled with three fluorophores and coordinated changes in the three inter-dye distances.

.. image:: ./../figures/examples/Dynamic_2c_ALEX.png
   :target: https://deep-lasi-tutorial.readthedocs.io/en/latest/examples/example-3c-FRET-Dynamic.html
   :width: 800
   :alt: Dynamic 3c FRET Analysis with ALEX
   :align: center

|

.. Co-Localization analysis
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Co-localization of differently labeled biomolecules can provide valulable information on molecular interactions.
.. The following workflow describes how to use Deep-LASI for standard colocalization experiments with up to three detection channels.

.. .. image:: ./../figures/examples/Co-Localization.png
   :target: https://deep-lasi-tutorial.readthedocs.io/en/latest/examples/example-Colocalization.html
   :width: 250
   :alt: Collocalization between up to three binding partners
   :align: center

|

.. --------------------------------------------------------------------
.. 
.. 3D Tracking of fluorescent particles
.. --------------------------------------
..
.. ... coming soon ...
.. 
.. Workflow for extracking and analyzing fluorescent traces and FRET signatures of diffusing particles from 3D-Orbital Tracking microscopy. (Mieskes et al., 2023, Small)

.. toctree::
   :hidden:
   :titlesonly:

   ./examples/example-steps
   ./examples/example-paint
   ./examples/example-2c-FRET-Static
   ./examples/example-2c-FRET-Dynamic
   ./examples/example-Colocalization
