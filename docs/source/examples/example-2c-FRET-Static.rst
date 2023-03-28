.. |br| raw:: html

   <br />

.. _static_2c:

Static 2c FRET Data
=====

The following section describes the workflow when analyzing static, 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data.
Deep-LASI provides a modular workflow for analyzing the data, either manually or automatically. The analysis starts with the co-localization of fluorescent molecules between both channels and trace extraction, the categorization process, the determination of correction factors, the selection of time windows to be analyzed per single time trace, the kinetic analysis, and ends with a summary of the analyzed traces by calculating the distribution of the correction factors, the FRET and stoichiometry values.

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

Example 1
-----------

..  _example-data1:
Sample Design: Static Double-Stranded DNA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first data sets are chosen from a multi-laboratory `benchmark study <https://www.nature.com/articles/s41592-018-0085-0>`_. It contains two single-molecule data sets of double-labeled DNA molecules. The two samples feature a low (:numref:`fig_DNA`, left) and intermediate FRET efficiency (:numref:`fig_DNA`, right) by design, with the attached fluorophore pairs being separated by 23 and 15 base pairs, respectively.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_1.png
   :width: 700
   :alt: Static 2c DNA 
   :align: center
   :name: fig_DNA
   
   Double-Stranded DNA labeled with the donor dye Atto550 and acceptor dye Atto647N in 23 bp distance (left) and 15 bp separation (right).


.. _data-prep1:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The DNA molecules were recorded on a TIRF microscope with dual-view inset and alternating laser excitation at an exposure time of 200 ms (:numref:`dualview`). To analyze the data, we downloaded the raw data from `Zenodo <https://zenodo.org/record/1249497#.Y_D1bnaZPmk>`_ and saved the raw *.tif* files for (1) the calibration measurement, (2) the low FRET sample and (2) the intermediate FRET sample.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_Alternation.png
   :width: 700
   :alt: Determination of alternation cycle and mapping when using a dualview inset in the detection path.
   :align: center
   :name: dualview

   Alternation cycle and position of the two detection channels on the camera when using a dualview inset.

In the first step, we need to identify the detection channels, i.e., their position on the camera and the applied laser excitation schemes (:numref:`dualview`). For this, we can, for example, use ImageJ to load any of the downloaded movies encoding the single-molecule data of the two DNA constructs.
When looking at the tiff-stack with alternating laser excitation on a frame-to-frame basis, we can identify the detection channels best during the red excitation period: frames with red excitation show emission on the left half of the camera (acceptor emission after acceptor excitation), while no emission signal is observed on the right half of the camera (Donor emission after acceptor excitation) due to the missing excitation of the donor molecule. This means the donor emission after donor excitation (DD) is detected on the right half of the camera, while the acceptor emission after donor excitation (DA) or direct excitation (AA) is recorded on the left half of the camera. Furthermore, we can identify an ALEX cycle RG starting with red excitation R followed by yellow excitation Y for 1 frame each (:numref:`dualview`).


.. _localization1:
Co-Localization of Molecules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we need to know where double-labeled DNA molecules are detected on the two field-of-views (FOV) of the camera, i.e., which pixel on the red channel corresponds to a pixel on the yellow detection channel (:numref:`fig_mapping`). While differences in magnification will not be observed on a single camera, there can be still a slight tilt or shift between the two images due to the alignment of dual-view inset.

.. figure:: ./../../figures/examples/Static_Twoc_Sub_Figure_2_Hellekamp_Map.png
   :width: 250
   :alt: 2c FRET data recorded with ALEX on a split camera
   :align: center
   :name: fig_mapping

   Determination of the transformation matrix by mapping the donor on the acceptor channel.

To retrieve the transformation matrix, which translates single molecule localizations in one channel onto the other, we first used *Deep-LASI* to generate a map. For this, we loaded the calibration file *calib20140402_0.tif* into the software. In the first step (:numref:`calib`, A), we read in the data from the **red** channel (which is on the left half of the movie) into the first channel. For this, we loaded the movie via :code:`File > Mapping > Create New Map > 1st channel`. *Deep-LASI* can handle input data with full or halved field-of-view. We chose the left half of the camera for the red data and confirmed. In the second step (:numref:`calib`, B), we loaded the data for the **yellow** channel via :code:`File > Mapping > Create New Map > 2nd channel` and chose the right half of the camera.

.. figure:: ./../../figures/examples/PA_Hellenkamp_mapping_steps.png
   :width: 700
   :alt: Workflow to create a map between both channels
   :align: center
   :name: calib

   Workflow to create a map between both detection channels

After loading the file, *Deep-LASI* shows the averaged image for each detection channel separately and automatically detects single emitters (:numref:`calib`, C). The numbers of localization and potential mislocalization can be adopted using the slider below the two images. We chose Channel 1 (red camera) as a reference, i.e., *Deep-LASI* warps the image from the *yellow* channel onto the *red* detection channel.
The result is afterwards shown in a side-by-side image that depicts the overlay of both channels before and after the mapping (:numref:`calib`, D). Lastly, we saved the generated map via :code:`File > Mapping > Save Map`.


.. _extraction1:
Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After generating the transformation matrix via mapping or reloading the already generated map via :code:`File > Mapping > Load Prev. Map (Ctrl + M)`, we can load the actual single-molecule data in the next step. To obtain the trajectories of individual molecules depending on the laser excitation, *Deep-LASI* can detect and extract traces on a single file basis. For this, it can read single *.tif* files and save the extracted traces in separate *.mat* files, which can be added file-by-file afterwards for further analysis. However, *Deep-LASI* also permits extracting traces from raw data files with consecutive numbering. In the presented example, we proceeded by reading in all raw *.tif* files per experiment at once, i.e., the data files *FSII1a_g30r84t200_0.tif* until *..._6.tif* or *FSII1b_g30r84t200_0.tif* until *..._6.tif* for the 'low-FRET' and 'intermediate-FRET' sample, respectively. We loaded the data of the first channel (as specified during the mapping process) via :code:`File > Load Image Data > 1st channel` for the red channel and selected the files.

.. figure:: ./../../figures/examples/PA_Hellenkamp_measurement_parameters.png
   :width: 750
   :alt: Settings for extracting the different emission channels depending on the excitation cycle
   :align: center
   :name: static_2c_extraction

   Settings for extracting the different emission channels depending on the excitation cycle.

Next, we specified the experimental settings for *Deep-LASI* (:numref:`static_2c_extraction`, A). We provided the interframe time of 200 ms, given by the exposure time and frame time together. Next, we specified the excitation cycle 'RG' by typing in the ALEX sequence.

.. note:: Due to coding reasons, *Deep-LASI* recognizes the letters B, G, R, and I as input for the laser excitation in the ALEX cycle. They are required for the correct selection of laser excitation cycle and visualization in multi-color experiments, later. Yellow excitation is also referred to as 'green' (G) excitation and infrared excitation is abbreviated with (I).

The ALEX sequence activates a slider that allows one to switch between the specified number of excitation sources and to observe in the image on the left whether the correct slider position is set. We chose the red excitation cycle by selecting the left position of the slider. *Previously defined frame range* is set automatically to the whole number of frames during the meaurement, and *Limit particle detection, image frame range* allows for omitting frames (at the beginning or the end) in case of measurement errors or other experimental settings. For reading in ALEX data in this example, we can read in all frames - ranging from 1 to the total number of frames, which is 1000 in the case of the 'low-FRET' sample and 1600 in the case of the 'intermediate-FRET' sample. Selecting the fluorophore in this study is optional and will provide additional metadata to the saved file containing the extracted traces. We finished the read-in process by selecting the red detection channel by pressing the *R* button (:numref:`static_2c_extraction`, A).

.. note:: While in 4-color FRET experiments, the channel order from 1 to 4 directly matches the detection channels, in 3-color or 2-color FRET experiments, in particular, there are different combinations of excitation and detection channels (BG, GR, RIR, BR, BIR, GIR) that will lead to an identical extraction of the single-molecule data as long as the corresponding ALEX sequence is given and matching the detection channels. The only difference is that *Deep-LASI* will choose different colors when displaying the traces afterwards. *Deep-LASI* will interpret the detection channels in the order of channels presented during the mapping process. For color consistency, we chose yellow/red excitation.

In the second step, we loaded the data of the yellow detection channel via :code:`File > Load Image Data > 2nd channel` and selected the files. Next, we provided the experimental settings for the yellow channel (:numref:`static_2c_extraction`, B) leaving the specified interframe time of 200 ms and the excitation cycle of 'RG' unchanged.
We chose the yellow excitation cycle by selecting the right position of the slider and confirmed all frames 1-1000 (1-1600 in the case of the 'intermediate-FRET' sample). Having specified the fluorophore, we finished the read-in process by selecting the yellow detection channel by pressing the *G* button (:numref:`static_2c_extraction`, B).

In the following, *Deep-LASI* automatically reads the raw data file-by-file, localizes molecules in the acceptor channel, identifies molecules in the donor channel by mapping, and extracts the trajectories of every molecule found depending on the excitation cycle. This process is carried out iteratively for the number of files specified and can last several minutes. The progress of the extraction process is shown in the left corner of the GUI and allows one to guesstimate the waiting time. Once the extraction process is finished, the extracted traces would be saved in the data folder by the program, and in any later time the user can save the traces via :code:`File > Save Traces / State (Ctrl + S)` to keep all the changes updated on the file. 

.. note:: In case an error occurs, try to save the extracted traces anyhow. For some Windows installations test sofar, we encounter a GUI error at the end of the extraction process, which has no influence on the prior extraction process.

With the threshold settings that we used, we got in total 855 traces from the 7 data files for the 'low-FRET' DNA sample. The manual and automatic analysis steps and results are explained in the following section.

.. _manual1:
Manual data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By using the Navigation slider we clicked through all the traces one by one to check their individual features and attribute them to one or several categories created in the *Classification* chart. You can see the result of manual trace sorting on :numref:`Hellenkamp_categorized_manual`. For a detailed description of manual analysis steps please see the section **Manual data analysis and correction, 2c-FRET-Dynamic, linking**.

.. figure:: ./../../figures/examples/PA_Hellenkamp_manual_sorted.png
   :width: 400
   :alt: Hellenkamp_categorized
   :align: center
   :name: Hellenkamp_categorized_manual
   
   Categories manually created for the static two-color 'low-FRET' DNA sample

After categorization, we moved on to the *Histograms* tab to plot the results especially the apparent and corrected FRET efficiencies to compare them with the published results. For this, we first plotted and fitted correction factors as you can see on :numref:`Hellenkamp_manual_corr_factors`. For each of the plots, we chose the corresponding categoy from the *Data Selection* panel by clicking on the plus sign beside its name, followed by selecting the desired correction factor from the *Plot Mode*. So, we first chose the category *G Alpha* and then on the *Plot Mode*, we clicked on *Direct Excitation Factor (Alpha)*. For the *Fit Method*, we chose *Gauss1*, and clicking on *Fit Plots*, we got the plot with fitting results (:numref:`Hellenkamp_manual_corr_factors`, left). We took similar steps for the other two correction factors. So, we chose the category *RR Beta* for plotting *Spectral crosstalk corr. factor (Beta)*, and *RR Gamma* for *Detection efficiency corr. factor (Gamma)* respectively. You can see the resulting plots and values for correction factors on the middle and right panels of :numref:`Hellenkamp_manual_corr_factors`.   

.. figure:: ./../../figures/examples/PA_Hellenkamp_manual_corr_factors.png
   :width: 700
   :alt: Hellenkamp_corr_factors
   :align: center
   :name: Hellenkamp_manual_corr_factors
   
   Correction factors plotted and fitted after manual categorization and region selecting. From left to right, direct excitation, spectral crosstalk, and detection efficiency correction factors.

The values we obtained for correction factors for this published data set through manual analysis are 0.064 for the direct excitation, 0.077 for the spectral crosstalk, and 0.792 for detection efficiency.

Next, we plotted the FRET Efficiency histograms to get the final value for corrected FRET efficiency and calculate the distance between the two fluorophores. For this we selected the category *Manual Selection* which consists of all the traces with high enough quality for final analysis. Then we plotted apparent and corrected framewise *FRET Efficiency* on the *Plot Mode* respectively, and fitted the plots in each case. As you can see on :numref:`Hellenkamp_manual_app_corr_fret`, the apparent and corrected FRET efficiencies obtained via manual analysis are 0.22 and 0.18 respectively. Based on `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_, the corrected FRET efficiency is expected to be 0.15 ± 0.02, and the value of 0.18 that we got from the manual analysis is close enough considering the quality of traces. Using the reported :math:`R_{0}` value of 62.6  A\ :sup:`o`\, we calculated the distance to be 80.6 A\ :sup:`o`\.

.. figure:: ./../../figures/examples/PA_Hellenkamp_manual_app_corr_fret.png
   :width: 550
   :alt: Hellenkamp_manual_fret
   :align: center
   :name: Hellenkamp_manual_app_corr_fret
   
   Apparent and corrected FRET efficiency histograms with the fitting result after manual categorization and region selecting 
   
.. _automatic1:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following section you will see the automatic analysis results for the static two-color ‘low-FRET’ DNA sample. For a detailed description of automatic analysis steps please see the section **Automatic data analysis and correction, 2c-FRET-Dynamic, linking**. We first need to have the traces loaded on the program, then from the *Deep Learning* tab, we clicked on *Magic Button*. The traces were categorized by the program as shown on :numref:`Hellenkamp_autocategorized`. The resulting histograms and FRET efficiencies are reported on the following section. 

.. figure:: ./../../figures/examples/PA_Hellenkamp_DL_categories.png
   :width: 400
   :alt: Hellenkamp_autocategorized
   :align: center
   :name: Hellenkamp_autocategorized

   Categories created by DeepLASI for the static two-color 'low-FRET' DNA sample

.. _summary1:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first two plots created by Deep-LASI are the confidence level distribution for determining the number of states and states prediction with a tracewise manner resulting from the state classifier(:numref:`Hellenkamp_autom_state_prediction`).

.. figure:: ./../../figures/examples/PA_Hellenkamp_tracewise_state_prediction.png
   :width: 500
   :alt: Hellenkamp_autom_states
   :align: center
   :name: Hellenkamp_autom_state_prediction

   The Deep-LASI confidence level for determining the number of states and state values on traces
   
.. figure:: ./../../figures/examples/PA_Hellenkamp_autom_fret_hist.png
   :width: 500
   :alt: Hellenkamp_autom_fret
   :align: center
   :name: Hellenkamp_autom_fret_histogram

   The histogram of apparent FRET efficiency averaged for each state

.. figure:: ./../../figures/examples/PA_Hellenkamp_de_ct.png
   :width: 600
   :alt: Hellenkamp_autocorrection_de_ct
   :align: center
   :name: Hellenkamp_autocorr_de_ct

   The histograms of direct excitation and spectral crosstalk correction factors reported with statistics

.. figure:: ./../../figures/examples/PA_Hellenkamp_gamma.png
   :width: 500
   :alt: Hellenkamp_autocorrection_gamma
   :align: center
   :name: Hellenkamp_autocorr_gamma

   The histograms of detection efficiency correction factor reported with statistics   
   
.. -----------------------------------------------------

.. Overview - Example 2
.. ------------------
.. - :ref:`example-data2`
.. - :ref:`data-prep2`
.. - :ref:`extraction2`
.. - :ref:`automatic2`
.. - :ref:`manual2`
.. - :ref:`summary2`

.. -----------------------------------------------------

.. Example 2
.. -----------

..  _example-data2:
Sample Design: Static L-Shaped DNA Origami
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/PA_BR_mapping_steps.png
   :width: 600
   :alt: Workflow_mapping_BR
   :align: center
   :name: Workflow_mapping_BR_data

   Workflow to create a map between both blue and red detection channels 
   
   
