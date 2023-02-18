.. _static_2c:

Static 2c FRET Data
=====

The following section describes the workflow, when analyzing static, 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data.
Deep-LASI provides a modular workflow for analysing the data, either manually or automatically. The analysis starts with the co-localization of fluorescent molecules between both channels and trace extraction , the categorization process, the determination of correction factors, the selection of time windows to be analyzed per single time trace, the kinetic analysis, and ends with a summary of the analyzed traces by calculating the distribution of the correction factors, the FRET and stoichiometry values.

We describe how to use *Deep-LASI* for two examples: (1) a publicly available example data set published by by `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_, which was recorded on a split camera, and (2) a static two-color DNA origami sample, which was recorded on two separate cameras.
Further sample data sets can be found, e.g., in `Wanninger et al., BioArxiv (2023) <https://doi.org/10.1101/2023.01.31.526220>`_.

.. We discuss two examples for publicly available sample data from `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_ and `Götz et al., Nat. Meth (2022) <https://www.nature.com/articles/s41467-022-33023-3>`_.

Overview - Example 1
------------------
- :ref:`example-data`
- :ref:`data-prep`
- :ref:`extraction`
- :ref:`automatic`
- :ref:`manual`
- :ref:`summary`

Overview - Example 2
------------------
- :ref:`example-data2`
- :ref:`data-prep2`
- :ref:`extraction2`
- :ref:`automatic2`
- :ref:`manual2`
- :ref:`summary2`

--------------------------------------------------------------------

..  _example_no1:
Example 1
-----------

..  _example-data1:
Sample Design: Static Double-Stranded DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first data set is chosen from a multi-laboratory `benchmark study <https://www.nature.com/articles/s41592-018-0085-0>`_. It contains a mix of two single-molecule data sets of double-labeled DNA molecules. The two samples feature a low (:numref:`fig_DNA` (left)) and intermediate FRET efficiency(:numref:`fig_DNA` (right)) by design, with the attached fluorophore pairs being separated by 23 and 15 base pairs, respectively.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 700
   :alt: Static 2c DNA 
   :align: center
   :name: fig_DNA
   
   Double-Stranded DNA labeled with the donor dye Atto550 and acceptor dye Atto647N in 23 bp distance (left) and 15 bp separation (right).

.. _data-prep1:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The DNA molecules were recorded on a TIRF microscope with dual-view inset and alternating laser excitation (:numref:`fig_dualview`). Due to the split camera image, the donor emission after donor excitation (DD) is detected on the left half of the camera, while the acceptor emission after donor excitation (DA) or direction excitation (AA) are recorded on the right half of the camera. To analyse the data, download the raw data from `Zenodo <https://zenodo.org/record/1249497#.Y_D1bnaZPmk>`_ and save the raw tif-files for (1) the calibration measurement, (2) the low FRET sample and (2) the intermediate FRET sample.

 downloaded tif-files
.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 700
   :alt: 2c FRET data recorded with ALEX on a split camera
   :align: center
   :name: fig_dualview

In the next step, we generated a map which co-localizes donor-molecules with the FRET partnes in the second half of the camera. For this, we opened the

.. _extraction1:
Co-Localize Molecules / Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _automatic1:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _manual1:
Manual data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _summary1:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


-----------------------------------------------------

..  _example_no2:
Example 2
-----------

