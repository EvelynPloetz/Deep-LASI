.. |br| raw:: html

   <br />

.. _dynamic-2c:

Dynamic 2c FRET Data
=====

Here you can see how to use DeepLASI to analyze dynamic 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data measured with alternating laser excitation (ALEX). DeepLASI provides you with the options of analyzing your data either automatically using the deep learning neural network or manually. The analysis usually starts with detecting the co-localized FRET pairs within the field of view from both cameras and extracting their intensity traces, followed by sorting the traces into helpful categories, and determining the correction factors. Afterwards, you can continue the analysis steps for the kinetics of the sample system and visualize the whole data on various plots and histograms.   

The following part shows all the steps to analyze dynamic 2C smFRET data from L-shaped DNA origami structures with three FRET states. The example data together with further data sets are accessible in `Wanninger et al., BioArxiv (2023) <https://doi.org/10.1101/2023.01.31.526220>`_.

Overview - Example
------------------
- :ref:`example-data`
- :ref:`data-prep`
- :ref:`localization`
- :ref:`extraction`
- :ref:`manual`
- :ref:`automatic`
- :ref:`summary`

--------------------------------------------------------------------

Example
-----------

..  _example-data:
Sample Design: Dynamic L-Shaped DNA Origami
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The described data set is from smTIRF measurement with DNA origami structure as you can see on :numref:`dyn-2c-origami-3state`. The origami is labeled with Cy3B (donor) and Atto647N (acceptor).The donor is attached to the flexible tether with a 7.5 nt overhang binding freely among three single-stranded binding sites.The energy transfer is expected between a high FRET State 1 (12 o'clock), a low FRET State 3 (6 o'clock), and an intermediate FRET State 2 (9 o'clock).   

.. figure:: ./../../figures/examples/PA1-Dynamic_2c_Origami.png
   :width: 400
   :alt: 2c-origami-3state
   :align: center
   :name: dyn-2c-origami-3state
   
   L-shaped DNA origami structure labeled with Atto647N and Cy3B. The donor is attached to a tether that can freely bind to any of the three binding strands.  

.. _data-prep:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The origami structures were measured on a smTIRF microscope with two separate EMCCD cameras, one for the donor and one for the acceptor. ALEX was used to excite the donor and acceptor fluorophores alternatively at an exposure time of 50 ms, and the frame transfer on the cameras was set to 2.2 ms. The resulting data would then be videos of consecutive frames from each channel with *.tif* file format. You can find a couple of example raw data on `Zenodo <https://zenodo.org/record/1249497#.Y_D1bnaZPmk>`_. 

*(Maybe a figure here similar to what we have for static 2C to show the two cameras and excitation scheme, GR)*

.. _localization:
Co-Localization of Molecules 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using two separate detection paths, there might be the chance of some discrepancy between the cameras regarding to chromatic and spherical aberrations or cameras misalignment like shifts, rotatoin, or magnification. To make sure that double-labeled species are detected, a correct linking of same molecule emitters accross the detection channels is needed. DeepLASI uses makes a coordinate transformation map to get rid of any potential difference. For more details about mapping, please refer to the section :doc:`./docs/source/examples/example-2c-FRET-Static` 

..  _extraction:
Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  _manual:
Manual data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  _automatic:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  _summary:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
