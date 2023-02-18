Static 2c FRET Data
=====

.. _static_2c:

The following section describes the workflow, when analyzing static, 2-color smFRET (single-molecule Förster Resonance Energy Tranfer) data.
Deep-LASI provides a modular workflow for analysing the data, either manually or automatically. The analysis starts with the co-localization of fluorescent molecules between both channels and trace extraction , the categorization process, the determination of correction factors, the selection of time windows to be analyzed per single time trace, the kinetic analysis, and ends with a summary of the analyzed traces by calculating the distribution of the correction factors, the FRET and stoichiometry values.

The example below describes the workflow for a `mix of two double stranded DNAs <https://doi.org/10.1101/2023.01.31.526220>`_. 
Additional, publicly available sample data sets can be found, e.g., in `Wanninger et al., BioArxiv (2023) <https://doi.org/10.1101/2023.01.31.526220>`_. 

Overview
------------------
- :ref:`example-data`
- :ref:`data-prep`
- :ref:`extraction`
- :ref:`automatic`
- :ref:`manual`
- :ref:`summary`

--------------------------------------------------------------------

..  _example-data:
Sample Design: Static Double-Stranded DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first data set chosen in the multi-laboraory `benchmark study <https://www.nature.com/articles/s41592-018-0085-0>`_, enclode double-labeled DNA molecules. Two different samples with low (:numref:`fig_DNA` (left)) and intermediated FRET (:numref:`fig_DNA` (right)) were designed, where the attached fluorophore pairs are separated by 23 and 15 base pairs, respectively. 

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 700
   :alt: Static 2c DNA 
   :align: center
   :name: fig_DNA
   
   Double-Stranded DNA labeled with the donor dye Atto550 and acceptor dye Atto647N in 23 bp distance (left) and 15 bp separation (right).

.. _data-prep:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _extraction:
Co-Localize Molecules / Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _automatic:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _manual:
Manual data analysis and dorrection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _summary:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
