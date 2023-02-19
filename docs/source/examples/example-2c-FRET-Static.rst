.. |br| raw:: html

   <br />

.. _static_2c:

Static 2c FRET Data
=====

The following section describes the workflow, when analyzing static, 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data.
Deep-LASI provides a modular workflow for analysing the data, either manually or automatically. The analysis starts with the co-localization of fluorescent molecules between both channels and trace extraction , the categorization process, the determination of correction factors, the selection of time windows to be analyzed per single time trace, the kinetic analysis, and ends with a summary of the analyzed traces by calculating the distribution of the correction factors, the FRET and stoichiometry values.

We describe how to use *Deep-LASI* for two examples: (1) a publicly available example data set published by `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_, which was recorded on a split camera, and (2) a static two-color DNA origami sample, which was recorded on two separate cameras.
Further sample data sets can be found, e.g., in `Wanninger et al., BioArxiv (2023) <https://doi.org/10.1101/2023.01.31.526220>`_.

.. We discuss two examples for publicly available sample data from `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_ and `Götz et al., Nat. Meth (2022) <https://www.nature.com/articles/s41467-022-33023-3>`_.

Overview - Example 1
------------------
- :ref:`example-data1`
- :ref:`data-prep1`
- :ref:`localization1`
- :ref:`extraction1`
- :ref:`manual1`
- :ref:`automatic1`
- :ref:`summary1`

--------------------------------------------------------------------

..  _example_no1:
Example 1
-----------

..  _example-data1:
Sample Design: Static Double-Stranded DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first data set are chosen from a multi-laboratory `benchmark study <https://www.nature.com/articles/s41592-018-0085-0>`_. It contains two single-molecule data sets of double-labeled DNA molecules. The two samples feature a low (:numref:`fig_DNA`, left) and intermediate FRET efficiency (:numref:`fig_DNA`, right) by design, with the attached fluorophore pairs being separated by 23 and 15 base pairs, respectively.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 700
   :alt: Static 2c DNA 
   :align: center
   :name: fig_DNA
   
   Double-Stranded DNA labeled with the donor dye Atto550 and acceptor dye Atto647N in 23 bp distance (left) and 15 bp separation (right).


.. _data-prep1:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The DNA molecules were recorded on a TIRF microscope with dual-view inset and alternating laser excitation at an exposure time of 250 ms (:numref:`dualview`). To analyse the data, we downloaded the raw data from `Zenodo <https://zenodo.org/record/1249497#.Y_D1bnaZPmk>`_ and saved the raw tif-files for (1) the calibration measurement, (2) the low FRET sample and (2) the intermediate FRET sample.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_Alternation.png
   :width: 700
   :alt: Determination of alternation cycle and mapping when using a dualview inset in the detection path.
   :align: center
   :name: dualview

   Alternation cycle and position of the two detection channels on the camera when using a dualview inset.

In the first step, we need to identify the detection channels, i.e., their position on the camera and the applied laser excitation schemes (:numref:`dualview`). For this we can, for example, use ImageJ to load any of the downloaded movies encoding the single-molecule data of the two DNA constructs.
When looking at the tiff-stack with alternating laser excitation on a frame-to-frame basis, we can identify the detection channels best during the red excitation period: frames with red excitation show emission on the left half of the camera (acceptor emission after acceptor excitation), while no emission signal is observed on the right half of the camera (Donor emission after acceptor excitation) due to the mission excitation of the donor molecule. This means, the donor emission after donor excitation (DD) is detected on the right half of the camera, while the acceptor emission after donor excitation (DA) or direction excitation (AA) is recorded on the left half of the camera. Furthermore, we can identify an ALEX cycle RG starting with red excitation R followed by yellow excitation Y for 1 frame each (:numref:`dualview`).


.. _localization1:
Co-Localizion of Molecules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we need to know, where double-labeled DNA molecules are detected on the two field of views of the camera, i.e., which pixel on the red channel corresponds to a pixel on the yellow detection channel (:numref:`fig_mapping`). While differences in magnification will not be observed on a single camera, there can be still a slight tilt or shift between the two images due to the alignment of dual-view inset.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_Map.png
   :width: 250
   :alt: 2c FRET data recorded with ALEX on a split camera
   :align: center
   :name: fig_mapping

   Determination of the transformation matrix by mapping the donor on the acceptor channel.

To retrieve the transformation matrix, which translates single molecule localizations in one channel onto the other, we first used *Deep-LASI* to generate a map. For this, we loaded the calibration file *calib20140402_0.tif* into the software. |br|
In the first step (:numref:`calibration`, A), we read in the data from the **yellow** channel (which is on the right half of the movie) into the first channel. For this we loaded the movie via :code:`Open File > Mapping > Create New Map > 1st channel`. *Deep-LASI* can handel input data with full and halved field of views. We choose the right half of the camera for the yellow data and confirm.  In the second step (:numref:`calibration`, B), we load the data for the red channel via :code:`Open File > Mapping > Create New Map > 2nd channel` and choose the left half of the camera.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_DL_Map.png
   :width: 700
   :alt: Workflow to create a map between both channels
   :align: center
   :name: calibration

    Workflow to create a map between both detection channels

After loading the data, *Deep-LASI* shows the averaged image for each detection channel separately and automatically detects single emitters (:numref:`calibration`, C). Using the slider the below the two images, the numbers of localization and potential mis-localizations can be adopted. We chose Channel 2 (red camera) as reference, i.e., *Deep-LASI* warps the image from the *yellow* channel onto the *red* detection channel.
The results is afterwards shown in a side-by-side image, which depict the overlay of both channels before and after the mapping (:numref:`calibration`, D). Lastly, we're left with saving the generated map via :code:`Open File > Mapping > Save Map`.

.. _extraction1:
Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_DL_Extraction.png
   :width: 700
   :alt: Settings for extracting the different emission channels depending on the excitation cycle
   :align: center
   :name: fig_extraction

.. _manual1:
Manual data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _automatic1:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _summary1:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


-----------------------------------------------------

Overview - Example 2
------------------
- :ref:`example-data2`
- :ref:`data-prep2`
- :ref:`extraction2`
- :ref:`automatic2`
- :ref:`manual2`
- :ref:`summary2`

..  _example_no2:
Example 2
-----------

