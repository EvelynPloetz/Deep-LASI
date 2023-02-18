.. |br| raw:: html

   <br />

.. _dynamic-2c:

Dynamic 2c FRET Data
=====

The following part shows how to use DeepLASI to analyze dynamic 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data measured with alternating laser excitation (ALEX). DeepLASI provides you with the options of analyzing your data either automatically using the deep learning neural network or manually. The analysis usually starts with detecting the co-localized FRET pairs within the field of view from both cameras and extracting their intensity traces, followed by sorting the traces into helpful categories, and determining the correction factors. Afterwards, you can continue the analysis steps for the kinetics of the sample system and visualize the whole data on various plots and histograms.   

The following part shows all the steps to analyze dynamic 2C smFRET data from L-shaped DNA origami structures with three FRET states as you can see on :numref:`dyn-2c-origami-3state`.   

.. figure:: ./../../figures/examples/PA1-Dynamic_2c_Origami.png
   :width: 400
   :alt: 2c-origami-3state
   :align: center
   :name: dyn-2c-origami-3state
   
   L-shaped DNA origami structure labeled with Atto647N and Cy3B. The donor is attached to the flexible tether with a 7.5 nt overhang between the pointer and three single-stranded binding sites. The energy transfer is expected between a high FRET State 1 (12 o'clock), a low FRET State 3 (6 o'clock), and an intermediate FRET State 2 (9 o'clock).  
