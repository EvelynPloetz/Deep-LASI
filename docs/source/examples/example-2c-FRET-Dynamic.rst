.. |br| raw:: html

   <br />

.. _dynamic-2c:

Dynamic 2c FRET Data
=====

Here you can see how to use DeepLASI to analyze dynamic 2-color smFRET (single-molecule Förster Resonance Energy Transfer) data measured with alternating laser excitation (ALEX). DeepLASI provides you with the options of analyzing your data either manually or automatically using the deep learning neural network. The analysis usually starts with detecting the co-localized FRET pairs within the field of view from both cameras and extracting their intensity traces, followed by sorting the traces into helpful categories, and determining the correction factors. Afterwards, you can continue the analysis steps for the kinetics of the sample system and visualize the whole data on various plots and histograms.   

The following part shows all the steps to analyze dynamic 2C smFRET data from L-shaped DNA origami structures with two FRET states. The example data together with further data sets are accessible in `Wanninger et al., BioArxiv (2023) <https://doi.org/10.1101/2023.01.31.526220>`_.

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

The described data set is from smTIRF measurement with DNA origami structure as you can see on :numref:`dyn-2c-origami-3state`. The origami is labeled with Cy3B (donor) and Atto647N (acceptor).The donor is attached to the flexible tether with a 8 nt, 1 mismatch overhang binding freely between single-stranded binding sites. The energy transfer is expected between a high FRET State 1 (12 o'clock) and a low FRET State 2 (6 o'clock).   

.. warning:: We need a 2c 2state sample image here.  

.. figure:: ./../../figures/examples/PA1-Dynamic_2c_Origami.png
   :width: 400
   :alt: 2c-origami-3state
   :align: center
   :name: dyn-2c-origami-3state
   
   L-shaped DNA origami structure labeled with Atto647N and Cy3B. The donor is attached to a tether that can freely bind to any of the two binding strands.

.. _data-prep:
Data preparation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The origami structures were measured on a smTIRF microscope with two separate EMCCD cameras, one for the donor and one for the acceptor. ALEX was used to excite the donor and acceptor fluorophores alternatively at an exposure time of 50 ms, also the frame transfer time of the cameras was set to 2.2 ms. The resulting data would then be videos of consecutive frames from each channel with *.tif* file format. You can find a couple of example raw data on `Zenodo <https://zenodo.org/record/1249497#.Y_D1bnaZPmk>`_. 

.. warning:: Maybe a figure here similar to what we have for static 2C to show the two cameras and excitation scheme, GR.

.. _localization:
Co-Localization of Molecules 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using two separate detection paths like the present example, there might be the chance of some discrepancy between the cameras' fields of view resulting from chromatic and spherical aberrations or cameras misalignment regarding to shifts, rotatoin, or magnification difference. To make sure that double-labeled species are detected, a correct linking of same molecule emitters accross the detection channels is needed. DeepLASI makes a coordinate transformation map to get rid of any potential difference. For more details about mapping, please refer to the section :doc:`./examples/example-2c-FRET-Static` 

To perform the mapping step, we used zero-mode waveguide (ZMW) as a calibration pattern which was illuminated by the wide-field lamp on the microscope. The ZMW was then imaged on both channels and with the steps shown on :numref:`mapping menu`, we opened the images one by one and used them to calibrate both channels. You can take the same steps as we did with the following instructions.  

From *file* menu, go to *Mapping*, and *Create New Map*, then click on *1st channel*. With the opened window, you can open the zmw image saved from the first channel which in our case is the *.tif* file from the donor or green camera.

.. figure:: ./../../figures/examples/PA1_mapping_menu.png
   :width: 550
   :alt: mapping menu
   :align: center
   :name: mapping menu
   
   Mapping steps on DeepLASI

On the *Channel Position* pop-up window, you can see a preview of the loaded ZMW image. Like the case on :numref:`mapping menu`, we clicked on *Full* to load the whole field of view, and then clicked on *OK*. 

.. figure:: ./../../figures/examples/PA2_map_image_loading.png
   :width: 500
   :alt: map image load
   :align: center
   :name: map image loading

.. figure:: ./../../figures/examples/PA3_map_image_loaded.png
   :width: 500
   :alt: map image loaded
   :align: center
   :name: map image loaded

.. figure:: ./../../figures/examples/PA4_map_image_loading1.png
   :width: 500
   :alt: map image loading
   :align: center
   :name: second map image loading

.. figure:: ./../../figures/examples/PA5_map_image_flipping.png
   :width: 500
   :alt: map image flip
   :align: center
   :name: map image flipping

.. figure:: ./../../figures/examples/PA6_start_mapping.png
   :width: 500
   :alt: start mapping
   :align: center
   :name: start mapping

.. figure:: ./../../figures/examples/PA7_before_after_map.png
   :width: 600
   :alt: check mapping
   :align: center
   :name: befor_after mapping

.. figure:: ./../../figures/examples/PA8_save_map.png
   :width: 400
   :alt: save map
   :align: center
   :name: save map
 
.. figure:: ./../../figures/examples/PA9_data_image_upload.png
   :width: 500
   :alt: data upload
   :align: center
   :name: first channel data upload

.. figure:: ./../../figures/examples/PA10_measurement_parameters.png
   :width: 500
   :alt: measurement_parameters
   :align: center
   :name: measurement_parameters

.. figure:: ./../../figures/examples/PA11_particle_detection.png
   :width: 500
   :alt: particle detection
   :align: center
   :name: particle detection

.. figure:: ./../../figures/examples/PA12_data_image_load1.png
   :width: 500
   :alt: data upload1
   :align: center
   :name: second channel data upload
 
.. figure:: ./../../figures/examples/PA13_measurement_parameter1.png
   :width: 500
   :alt: second measurement parameters
   :align: center
   :name: second measurement parameters

.. figure:: ./../../figures/examples/PA14_colocal_detection.png
   :width: 500
   :alt: colocal particles
   :align: center
   :name: colocalized particles

..  _extraction:
Trace Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/PA15_mask_and_start_extract.png
   :width: 500
   :alt: extracting
   :align: center
   :name: extraction begin

.. figure:: ./../../figures/examples/PA16_trace_look.png
   :width: 600
   :alt: 2c trace
   :align: center
   :name: 2c trace look
   
..  _manual:
Manual data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/PA17_categorization.png
   :width: 400
   :alt: categorize
   :align: center
   :name: categorization

.. figure:: ./../../figures/examples/PA18_mask_checking.png
   :width: 400
   :alt: mask check
   :align: center
   :name: mask checking

.. figure:: ./../../figures/examples/PA19_dye_active_region.png
   :width: 600
   :alt: region
   :align: center
   :name: region selection

.. figure:: ./../../figures/examples/PA20_correction_factor_box.png
   :width: 550
   :alt: correction factors
   :align: center
   :name: correction factors calculation

.. figure:: ./../../figures/examples/PA21_manually_categorized.png
   :width: 450
   :alt: manual categorize
   :align: center
   :name: manually categorized
   
.. figure:: ./../../figures/examples/PA22_app_FRET.png
   :width: 500
   :alt: app FRET
   :align: center
   :name: apparent FRET

.. figure:: ./../../figures/examples/PA23_correction_factors_fit.png
   :width: 650
   :alt: factors
   :align: center
   :name: correction factors

.. figure:: ./../../figures/examples/PA24_corr_FRET.png
   :width: 400
   :alt: corr FRET
   :align: center
   :name: corrected FRET

.. figure:: ./../../figures/examples/PA25_HMM_run.png
   :width: 500
   :alt: HMM satrt
   :align: center
   :name: HMM starting

.. figure:: ./../../figures/examples/PA26_TDP_dwell_time.png
   :width: 600
   :alt: HMM results
   :align: center
   :name: HMM resulting graphs
   
..  _automatic:
Automatic data analysis and correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/1_MainGUI.png
   :width: 550
   :alt: mainGUI
   :align: center
   :name: mainGUI

.. figure:: ./../../figures/examples/2_DeepLearningTab.png
   :width: 550
   :alt: DeepLearning_tab
   :align: center
   :name: DeepLearning_tab

.. figure:: ./../../figures/examples/3_TraceCategorization_ModelSelection.png
   :width: 300
   :alt: ModelSelection_for_categorization
   :align: center
   :name: ModelSelection_for_categorization

.. figure:: ./../../figures/examples/4_CategorizedTraces.png
   :width: 600
   :alt: after_categorization
   :align: center
   :name: categorized_traces

.. figure:: ./../../figures/examples/5_StateTransitions_ModelSelection.png
   :width: 300
   :alt: model_and_input
   :align: center
   :name: StateTransition_ModelSelection
   
..  _summary:
Plotting and Summary of Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./../../figures/examples/6_StateConfidence_Histogram.png
   :width: 350
   :alt: state-confidence-histogram
   :align: center
   :name: tracewise_state_confidence_histogram
  
.. figure:: ./../../figures/examples/7_Statewise_MeanFRET.png
   :width: 350
   :alt: statewise-meanFRET
   :align: center
   :name: statewise-meanFRET_histogram

.. figure:: ./../../figures/examples/8_TDP_Input.png
   :width: 350
   :alt: TDP_input
   :align: center
   :name: TDP_input
   
.. figure:: ./../../figures/examples/9_TDP_generated.png
   :width: 400
   :alt: TDP_generated
   :align: center
   :name: TDP_generated
   
.. figure:: ./../../figures/examples/10_TDP_PopulationSelection_and_LiveFit.png
   :width: 400
   :alt: TDP_selection_and_fit
   :align: center
   :name: TDP_selection_and_livefit
   
.. figure:: ./../../figures/examples/11_DataCorrection_DirEx_Crosstalk.png
   :width: 500
   :alt: de_and_ct
   :align: center
   :name: correction_factors_DE_and_CT   

.. figure:: ./../../figures/examples/12_DataCorrection_Gamma.png
   :width: 500
   :alt: gamma_factor
   :align: center
   :name: correction_factor_gamma_factor
   
