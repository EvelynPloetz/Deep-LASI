.. |br| raw:: html

   <br />

-----------------------------------------------

Starting Deep-LASI
~~~~~~~~~~~~~~~~~
To evaluate your experimental data with *Deep-LASI*, please open the program from the MATLAB command window by typing in :code:`>> DeepLASI`. It will open the core program responsible for data import, trace extraction, as well as manual selection and sorting. After a couple of seconds, the Start-GUI of the program will open as shown in :numref:`open-program`.

.. figure:: ./../figures/documents/Fig_2_Tracer_FirstPage.png
   :width: 650
   :alt: Open Deep-LASI
   :align: center
   :name: open-program

   The Main-GUI of *Deep-LASI* has six sub-windows for data processing and analysis.

*Deep-LASI* shows one empty Main-GUI together with six integrated sub-windows for analyzing the data and one menubar for handling the data reading, the settings of the program, the simulation of single-molecule data, and training (new) neural networks.

-----------------------------------------------

Menu Bar
~~~~~~~~~~~~~~~~~
Basic functionalities of *Deep-LASI*, such as data handling, program settings, or the training of new neural networks for data analysis, are controlled via the *Menu Bar*. It has the following five drop-down menus

..  csv-table:: Menu Bar Entries
   :widths: 15, 200

   *File*,   "Functions for loading, mapping, processing, saving, importing and exporting data"
   *Settings*,"Access to Camera Settings"
   *View*,   "Appearance of the GUI, Graphs and Data representation"
   *Tools*,  "Programs for accessing/simulating single-molecule data, and training Neural Networks"
   *Help*,   "Direct link to the Documentation in case of problems"
   *Reset*,  "Restart of *Deep-LASI* and clearance of all variable of the program"

**Dropdown Menu File.** |br|
The dropdown menu *File* (:numref:`file-menu`) controls all steps, starting from loading the experimental data, over mapping and background correction, to trace extraction and saving of traces. Moreover, it facilitates data import and export in different formats, as described in the :ref:`data-format` section. The dropdown menu hosts seven sub-routines:

#. The sub-routines in **Mapping** are used to match the corresponding image pixels between up to four different cameras. They allow the user to generate, save and reload maps containing the transformation matrices between the channels. A description of how to map the detection channels is given below in the :ref:`mapping` section.

#. **Load Image Data** facilitates the read-in of data files per detection channels. The data needs to be read in consecutively, starting with Channel 1 being the most 'blue'-shifted detection channel and Channel 4 being the most 'red'-shifted detection channel. Data loading is possible for a single file per channel, but also for multiple files at once. Please make sure: (1) that the numbers of loaded files per detection channel match and (2) that the files have consecutive numbering so that corresponding movies are loaded.

#. Using the **Load Traces/State** routine, previously extracted and potentially already evaluated traces can be reloaded into *Deep-LASI*.

#. The **Add Traces/State** routine allows the addition of further extracted traces to already loaded traces. This function is especially useful for merging trajectories from various measurements. Please note that only traces with identical experimental settings (e.g., number of frames, exposure time, or laser excitation) can be merged.

#. **Save Traces/State** to save desired changes on traces, for example, if you have already carried out all analysis steps.

#. The **Import** function allows loading data sets from other single-molecule measurements (as described in the :ref:`data-format` section above). The imported traces are only loaded and not further modified by *Deep-LASI*.

#. **Export** allows for transferring extracted traces to a former analysis software used by the hosting group and to save and export traces and enables the saving of single trajectories in graphic formats.

#. **Quit** terminates the program.

.. figure:: ./../figures/documents/DeepLASI_file_Menu.png
   :width: 400
   :alt: Open file menu
   :align: center
   :name: file-menu

   *Deep-LASI* file menu

**Dropdown Menu Settings.** |br|
The dropdown menu *Settings* (:numref:`settings-menu`) opens a sub-window for entering the camera hardware settings chosen in the experimental setup. The routine asks for the EM Gain factor, the camera baseline in dark counts, and the number of photons per camera count for each camera. With this, *Deep-LASI* can convert/display the determined intensity instead of arbitrary units in Counts per second, i.e., in Hertz.

.. figure:: ./../figures/documents/camera_settings.png
   :width: 600
   :alt: Open settings menu
   :align: center
   :name: settings-menu

   *Deep-LASI* settings menu

**Dropdown Menu View.** |br|
The third dropdown menu *View* controls the appearance and settings of the graphical interfaces on the different GUI sub-windows of *Deep-LASI*. |br|
The sub-tab *Colormap* changes the color palette in 3D plots, e.g., on the Trace GUI surface (which shows small zoomed-in areas of 24x24 pixels) or the Extraction GUI surface (which shows the average projection of localized molecules). In both cases, localized molecules are highlighted. The default colormap is *jet*, which can be exchanged by other standard color maps from MATLAB. |br|
The *Plot Units* sub-tab controls the y-axis of the intensity and FRET panels for individual single-molecule trajectories. Checking/unchecking the different sub-tabs immediately updates the graphical interface and the way how a single-molecule trace is displayed. The sub-tab **Plot Units** provides the following four different settings for displaying intensities and FRET trajectories:

..  csv-table:: Plot Units Entries
   :widths: 15, 200

   *Photons (Cam. calibrated)*,   "Intensity is shown as the absolute number of photons"
   *Mean across Particle Mask*,  "Intensity is shown as mean intensity within the detection mask"
   *Raw Trace (no BG subtr.)*,    "Intensity without background correction"
   *Corrected FRET*,              "Display of accurate FRET instead of apparent FRET"

#.  The first sub-tab, **Photons (Cam.calibrated)**, converts the intensity axis into the absolute number of photons being detected by the individual cameras during a particular excitation cycle. It updates the intensity axis of extracted single-molecule traces on the *Traces GUI* window.
#.  The second sub-tab, **Mean Across Particle Mask**, shows the mean emission intensity of the particle within the detection mask after trace extraction on the y-axis of the single-molecule traces on the *Traces GUI* window.
#.  The penultimate sub-tab, **Raw Trace (no BG subtr.)**, activates the display of uncorrected, raw intensity traces, i.e., without background subtraction.
#.  If the last option, **Corrected FRET**, is selected, *Deep-LASI* shows Accurate FRET efficiencies for each single-molecule trajectory in case the FRET correction factors have already been determined. Otherwise, the displayed FRET values between Accurate and Apparent FRET are identical.

**Dropdown Menu Tools.** |br|
The fourth dropdown menu *Tools* opens the sub-panels for simulating single-molecule traces and training neural networks. A detailed description of its functionalities, workflow, and usage is given in the :doc:`sim` Chapter.

**Dropdown Menu Help.** |br|
In the case of problems or errors, help can be found in the dropdown menu *Help*, which provides a direct link opening this Online documentation of *Deep-LASI*.

**Dropdown Menu Reset.** |br|
When finishing the analysis of one data set, a change to a new data set can create errors, in particular, if they differ with respect to laser alternation, imaging modalities, or the number of emitters. In this case, please reload the program via the *Reset* button. DeepLASI will reset all temporal variables in the background, refresh the graphical interface and restart the program.

-----------------------------------------------

Main-GUI
~~~~~~~~~~~~~~~~~
Data analysis with *Deep-LASI* involves consecutive working steps (:numref:`main-workflow`), which are accommodated in six different sub-GUIs, as shown in :numref:`open-program`. The Starting-GUI incorporates single molecule data at different levels. First of all, it reads movies from emCCD or sCMOS cameras, as usually acquired using a wide-field total internal reflection fluorescence (TIRF) microscope, and maps corresponding pixels between cameras onto each other (see the section on :ref:`mapping`). Next, it extracts the intensity information of single and co-localizing molecules depending on the excitation scheme and assay and saves the extracted traces afterward, as described in more detail in the section :ref:`extraction_doc`. For already recorded intensity time traces from confocal microscopy and localization microscopy, *Deep-LASI* imports the trajectories as formerly saved without additional correction. Equally, already extracted traces can be loaded into *Deep-LASI* for further data analysis.

.. figure:: ./../figures/documents/Fig_5_Main_GUIs-Flow.png
   :width: 800
   :alt: Main GUIs
   :align: center
   :name: main-workflow

   Workflow summarizing the generic data formats used by *Deep-LASI*, as well as supported data formats for trace import.

The main data handling is carried out on the *Traces* GUI (:numref:`main-workflow`). Here, you can choose between manual or automated data analysis. Conventional data analysis includes sorting, categorization, and trace preparation (as described in the section :ref:`manual_analysis`) before handing over the preselected traces for Hidden-Markov modeling on the *HMM* GUI followed by dwell time analysis and TDPs. The sub-window *Histograms* allows for summarizing the analyzed data via histograms with respect to, e.g., frame-, molecule-, and state-wise histograms, or the global FRET correction factors (:numref:`main-workflow`). The sub-window *Statistics* on selected molecule groups with respect to, e.g., average brightness, background, SNR, etc. |br|
The automated data analysis is carried out on the *Traces* GUI, which includes an automated selection, sorting, and categorization process prior to an automated kinetics analysis based on deep learning. The data is afterward automatically summarized by state-of-the-art dwell-time analysis and TDPs.

-----------------------------------------------

..  _mapping:
Mapping
~~~~~~~~~~~~~~~~~
Before loading data into *Deep-LASI*, one needs to consider the experimental requirements. In the case that single-color data has been acquired, the data can be directly loaded into the software, and single-channel traces can be extracted, as described in :ref:`extraction_doc`. In the case that more than one detection channel has been employed, we need to know where the emission of labeled molecules is detected on the different field-of-views (FOV) of the cameras, i.e., which pixels on one channel correspond to pixels on the other (:numref:`mapping_idea`).

.. figure:: ./../figures/documents/Fig_6_Main_GUI_Mapping.png
   :width: 500
   :alt: Mapping
   :align: center
   :name: mapping_idea

   Mapping between multiple detection channels copes with differences between the FOV due to translation, rotation, and magnification.

For mapping the different channels onto each other, please go to the dropdown menu *File* and choose
:code:`> File > Mapping > Create New Map` and load the reference data stepwise into *Deep-LASI* by clicking on :code:`> 1st channel`. The first channel refers to the FOV with the most blue-shifted emission, e.g., blue emission in a BGR ALEX excitation scheme. In the case that you use a split camera for two detection channels, you need to load the movie twice for the two corresponding channels separately and select the corresponding halves of the FOV in a consecutive step.

Next, the program will ask you to choose a file which could be an image or a series of images as a video file. This reference data should contain structures or emitters with multiple co-localization on the various cameras. This could be, for example, a cover slide with multi-colored beads or DNA origami structures with multiple labels. The emitters should be dense (but well separated) and widely spread over the entire FOV, such that aberrations in all areas of the FOV can be correctly translated between the different detection channels.

.. figure:: ./../figures/documents/map_image_uploading.png
   :width: 450
   :alt: map uploading
   :align: center
   :name: map_image_upload

   Uploading first mapping image

After choosing the calibration file, *Deep-LASI* opens a window (:numref:`map_image_upload`), which allows you to determine the correct position of the detection channel. You can use the **Channel Layout** to select the correct half of the camera or the full width of the camera. **Rotation** and **Flip** allow you to take into account if your camera image is flipped or rotated compared to your reference channel. After the selection, please confirm **OK** to open the image on the mapping tab, as shown in :numref:`mapping_gui`.

.. figure:: ./../figures/documents/map_image_detecting.png
   :width: 500
   :alt: map detection
   :align: center
   :name: mapping_gui

   Selection of recognized emitters in the first detection channel by *Deep-LASI*

After loading, use the threshold bar below the loaded image to make sure that enough points are detected (indicated by the white circle) by *Deep-LASI*. Next, continue opening the following images from other detectors by selecting the :code:`> 2nd channel`, etc., via the same procedure as shown in :numref:`map_image_upload` and :numref:`mapping_gui`.

Once you have loaded all mapping images to assign the detection windows, please select afterward which channel you prefer to be the reference channel, as shown in :numref:`mapping_start`. In most cases, the first channel is taken as the reference unless you have a special mapping plan. In the case that you experience a lot of photo-bleaching, mapping onto the channels with the most emitters might be advisable.

.. figure:: ./../figures/documents/mapping_starting.png
   :width: 800
   :alt: start mapping
   :align: center
   :name: mapping_start

   Performing the mapping step

Once you confirm your selection by clicking on **Start Mapping**, *Deep-LASI* aligns the different channels compared to the chosen reference channel and warps the presented images. *Deep-LASI* describes this mapping process by an affine transformation matrix, taking translation, rotation, and scaling into account.

.. figure:: ./../figures/documents/Fig_10_Map_Before_After.png
   :width: 500
   :alt: check mapping
   :align: center
   :name: before_after

   Mapping result showing the channels overlay before and after mapping

After a successful mapping process, the Extraction-GUI opens automatically. The mapping process itself is fast and visualizes the mapping results as a comparison of image overlays before and after the mapping procedure (:numref:`before_after`). To save the transformation matrix, i.e., the mapping result for any trace extraction later on, finally save the generated map (stored in the memory of *Deep-LASI* at this point) by clicking on :code:`> File > Mapping > Save Map`. It is recommended to check the quality of mapping. In some cases, you might have to rerun the mapping process by choosing (1) a different reference channel (e.g., if too many localizations in the different FOVs obscure the mapping process) or (2) a new data set of images (e.g., if too little localizations impede a representative mapping of aberrant images).

-----------------------------------------------

..  _extraction_doc:
Trace extraction
~~~~~~~~~~~~~

While single-color data can be directly loaded into *Deep-LASI*, multi-color assays require a mapping procedure first. Once this map is available and saved, you can start extracting experimental data anytime. As shown in :numref:`extraction_idea`, *Deep-LASI* will match the fluorescence signature from your single fluorophores during different excitation cycles and detection channels (once you have specified the single-molecule assay) and allows you to select which labeled molecules you actually want to evaluate. For this, you first need to step-wise read-in the experimental data, as described in the :ref:`loading_doc` section. Next, *Deep-LASI* will generate a projection for each channel, i.e., the corresponding *.tif-file*, showing the maximum intensity per pixel in the FOV. *Deep-LASI* will localize single emitters in each of the selected channels and superimpose the three maps afterward, showing the localized molecules in the individual channels. In the last step of the extraction process, *Deep-LASI* allows you to select whether you want to export all traces (i.e., the trajectories of single-, double- or triple-labeled molecules), traces of only co-localizing molecules (i.e., molecules having the maximum number of traces) or molecules that have a specific label in a reference a channel. After a successful extraction process, you are directly forwarded to the third sub-GUI **Traces**, where you need to save the extracted traces first before continuing with any data analysis.

.. figure:: ./../figures/documents/Fig_11_Trace_Extraction.png
   :width: 500
   :alt: Extraction
   :align: center
   :name: extraction_idea

   Trace extraction of molecules with one, two, or three labels and selection of whether trajectories for all molecules, co-localizing molecules only, or molecules that show emission in a specific channel shall be generated.

..  _extraction_modes:
Extraction modes
~~~~~~~~~~~~~
To start the extraction process, reload the earlier derived map via :code:`> File > Mapping > Open Map`. Once the map is successfully loaded, you are directly forwarded to the sub-GUI **Extraction** showing a detection mask created like the one shown on the top right part of :numref:`screenshot_extraction`. Alternatively, you were directly forwarded after the :ref:`mapping` process (please don't forget to save the generated map in this case before proceeding with the extraction).

.. figure:: ./../figures/documents/Fig_11_Map_Saving.png
   :width: 800
   :alt: Extraction GUI Screenshot
   :align: center
   :name: screenshot_extraction

   The mask created after mapping with adjustment options

Before data loading and trace extraction, you first need to consider which kind of experiment has been carried out. *Deep-LASI* supports the following types of measurement modes:

#. multi-color measurements with alternating laser excitation
#. multi-color measurements with constant laser excitation for a fixed number of frames

*ALEX excitation* |br|
In the case of ALEX excitation, load the data files after mapping the channels, as described in detail in the :doc:`example` section. Select one *.tif-file* or multiple files via :code:`> File > Load Image Data > Channel 1` and let *Deep-LASI* read the data.

Next, specify the measurement parameters of the ALEX experiment (:numref:`doc_measurement_parameters`), such as the inter-frame time and alternation cycle. The inter-frame time should include the exposure time and frame transfer time, e.g., when measuring a frame transfer time of 2.2 ms and exposure time of 50 ms by the emCCD camera, the total inter-frame time amounts to 52.2 ms.

.. figure:: ./../figures/documents/Fig_12_Measurement_Parameters.png
   :width: 500
   :alt: inserting measurement parameters
   :align: center
   :name: doc_measurement_parameters

   The window for specifying measurement parameters and excitation scheme

Please specify the sequence of the laser excitation using the letters B (blue), G (green/yellow), R (red), and I (infrared) for the four excitation channels. Different excitation schemes of up to three lasers can be entered here, such as RGB, RG, GB, etc. In the case of ALEX excitation, all channels are shown in the preview according to the created map, and the selected channel for data read-in is highlighted by a rectangle. Move the slider to choose the start frames of your entered excitation scheme and load it into the corresponding detection channel. This slider serves for movies where the starting point of data acquisition varies with laser excitation. For a varying acquisition, every single *tif.-file* needs to be loaded separately to select the correct alternation sequence / starting frame. The slider has 2 positions for a 2c-ALEX experiment. It automatically shows 3 positions in the case of a specified 3c-ALEX experiment.

Next, please choose which frames you want to load on the program using the **Load frame range** box. Depending on the experiment, you can choose the range of desired frames for detecting the particles and extracting their intensity traces. *Deep-LASI* takes all the frames by default. You can further limit the particle detection to a certain frame range, e.g., for a colocalization assay in which you used one excitation wavelength for the first 100 frames and continued with a second excitation wavelength for the rest of the measurement. As the last step here, click on the corresponding channel color from the four options to confirm the detection channel. *Deep-LASI* will open the first data file from the files being selected, as shown in :numref:`doc_particles_detection`, and display the cumulative sum of the movie for particle detection.

.. figure:: ./../figures/documents/Fig_13_Detecting_Particles.png
   :width: 500
   :alt: first channel detection
   :align: center
   :name: doc_particles_detection

   Particle detection for the first channel data

The sliders below the image allow for adjusting the brightness/contrast settings, the detection threshold to register particles, and to change between detection channels during the later extraction steps. Set the slides such that you maximize the number of detected molecules. Localized particles are marked by triangles superimposed on the image, and their localization number is shown in the black box aside from the image on the top right position.

In the next steps, please repeat loading the recorded data of the other detection channels by selecting the corresponding *.tif-files* or set of files via :code:`> File > Load Image Data > Channel 2`, etc. Each time you load image files, the pop-up window will ask you about the detection channel color to extract the data in the correct order.

.. figure:: ./../figures/documents/Fig_14_Measurement_Parameters_Second_Chan.png
   :width: 500
   :alt: inserting second measurement parameters
   :align: center
   :name: doc_second_channel

   Updating measurement parameters for the next channel

As shown in :numref:`doc_second_channel`, put the slider on the second half of the slider position to indicate the second channel (the same procedure works for the third channel by putting the slider in the right position). The reasoning behind this step is again to provide the freedom to select the correct excitation. Afterward, click on the red button labeled with 'R' (as specified in the alternation cycle box to confirm the acceptor channel. After a short time the average imaging of the specified loaded frames of the second channel overlays on the image from the first one.

.. figure:: ./../figures/documents/Fig_15_Detecting_Colocal.png
   :width: 500
   :alt: detection of co-localization
   :align: center
   :name: doc_find_co-localization

   Detection of particles and their co-localization

Once all desired channels are loaded and all detection channels have been identified, you can specify how you want to extract traces and which frame range. In the **Mask setting** panel, you can choose how the background and intensity of the single emitters shall be extracted. In the Mask popup menu you can choose between Manual and Autocorr. PSF. Depending on the chosen Mask the following three parameters **PSF**, **BG inner** and **BG outer** have different meanings. For the Manual Mask, the editable values specify the diameter of the **PSF**, the **BG inner** ring and **BG outer** ring as a ratio of the total cut out radius (19 pixels). The pixels between the inner and outer BG ring will be used for the background calculation. Choosing the autocorr. PSF will use the Fourier transform of the loaded image to determine the particle shape. Here the **PSF**, **BG inner** and **BG outer** values are used as a threshold in fourier space to determine the corresponding radii.

Next, specify which methods for particle detection shall be employed:

#. **Wavelet** detection (see for example `Messer et al. <https://iopscience.iop.org/article/10.1088/1367-2630/ac4ad5>`_ or `Ganjalizadeh et al. <https://www.nature.com/articles/s41467-022-28703-z>`_)
#. **Intensity Thresholding** (spatial bandpass denoising and extraction of centroids based on intensity)
#. **Regional Maxima** (intensity thresholding with additional radial center refinement using the in-built imregionalmax function)

All particle detection methods undergo a center offset refinement using gaussian filtering with a 3 pixel tolerance.
Lastly, specify in the **Trace selection** panel which traces you wish to extract. As indicated by the colors of the triangles (:numref:`doc_find_co-localization`) for each corresponding channel, you can extract either (1) all detected emitters independent of the detection channels (e.g., donor only, acceptor only, and FRET pairs) or (2) only co-localizing molecules as indicated by the white circles (e.g., only FRET species) or (3) extract the intensity in reference to a selected channel, which could be donor only species together with FRET species. The panel **Frame selection** allows for setting the frame range in which traces shall be extracted. In the case, you wish to export the mapped single-molecule image displayed in the *Extraction* GUI before you finally extract the traces, press the *Export the Warped Image* button on the left at the bottom of the GUI. For trace extraction itself, click on the right button *Extract Traces*. *DeepLASI* will now automatically extract traces movie-by-movie-wise for the file(s) you selected earlier. This process can last several moments but is fully automatically carried out. Once the extraction process is finished, the traces are saved automatically to last used directory. You can change all following analysis states via :code:`> File > Save Traces / State`

.. figure:: ./../figures/documents/Fig_16_Extraction_Settings.png
   :width: 450
   :alt: start extraction
   :align: center
   :name: doc_extraction_settings

   Starting the extraction of intensity traces

.. note:: In the case that an error occurs at the end of the data extraction, try to save the extracted traces anyway. Errors were reported for certain Windows installations that we are currently investigating to solve the problem.

*Constant excitation* |br|
In the case of constant laser excitation, we must consider different experimental schemes again. When multiple detection channels have been employed during constant excitation with one laser source, ...

.. tip:: @Simon: Please describe here, what you implemented, and how/what we need to fill in, in order to extract traces with constant laser excitaion with different lasers for fixed frame ranges!
