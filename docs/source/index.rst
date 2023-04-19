Welcome to Deep-LASI's documentation!
===================================

**Deep-LASI** (/dēp'lā-zē/) is a MATLAB program using Python libraries
for automatized, multi-color single-molecule intensity trajectory analysis.

**Deep-LASI** – *Deep-Learning Assisted Single-molecule Imaging* analysis provides a tool 
for image processing and automated, unbiased analysis of single-molecule data.
Deep-LASI comprises a collection of methods to characterize single molecule data 
with up to 3 channels in an automated fashion. The algorithms provided are routinely 
used to analyze data arising from multi-color single-molecule fluorescence experiments using TIRF or Confocal microscopy. 
Deep-LASI is based on the program TRacer, dedicated to finding single molecules, 
colocalizing molecules between different imaging channels, extracting their fluorescence 
signatures depending on the excitation and detection scheme and correcting the intensities for background signal depending on user-selected masks. The downstream analysis of 
single-molecule traces can be carried out manually as well as automatically using advanced 
deep-learning-assisted methods. Deep-LASI allows the determination of correction factors required for 
accurate FRET measurements and concomitantly distances between 2 or 3 fluorophores.
Moreover, it identifies underlying conformational states and kinetics. 
Deep-LASI provides an architecture to process the initial raw data and summarize the analyzed 
data in final plots based on MATLAB and libraries using Python. Please cite the following 
papers if you use Deep-LASI in your own work, so we can continue development and support:

::

   S Wanninger, P Asadiatouei, J Bohlen, CB Salem, P Tinnefeld, E Ploetzº and DC Lambº.
   Deep-Learning Assisted, Single-molecule Imaging analysis (Deep-LASI) of multi-color 
   DNA Origami structures. (2023) DOI: https://doi.org/10.1101/2023.01.31.526220

Deep-LASI pulls data from the `Repository <https://gitlab.com/simon71/deeplasi>`_
and offers a *simple* and *intuitive* API.

To get started with Deep-LASI, please take a look at the :doc:`installation` guide and :doc:`starter` section. 
Additional :doc:`example` and reference material are provided in the :doc:`documentation` section. 

If you have any questions or problems, if you want to provide feedback about your experience 
with Deep-LASI or if you have any suggestions on how to further improve the program, please get in touch with us via the `Forum <https://gitlab.com/simon71/deeplasi/-/issues>`_ or by Email.

.. note::

   This project is under active development.

.. Contents
.. --------

.. toctree::
   :maxdepth:1
   :hidden:

   starter
   installation
   documentation
   example
   sim
   about
.. tutorials

   about
   
Deep-LASI has its documentation hosted on Read the Docs.
