.. |br| raw:: html

   <br />


Plotting and fitting the results
~~~~~~~~~~~~~~~~~~~~
After having traces categorized with selected regions on each trace, in order to plot various parameters and fitting the distributions, you can move on to the *Histograms* tab on the main GUI (:numref:`Histograms_tab`). 

.. figure:: ./../figures/documents/PA_histogram_tab.png
   :width: 500
   :alt: histogram tab
   :align: center
   :name: Histograms_tab

   The *Histograms* tab on the main-GUI of DeepLASI

As shown on :numref:`Histograms_tab_GUI`, the provided tab consists of several panels. The panel *Plots* displays any created graph(s), and in case of fitting them, also fitting results attached to the plot(s). The panel *Data Selection* shows the same categories created before with the number of traces on each category. On the section *Plot Mode*, you can choose the desired parameter to be plotted. The provided list of parameters includes apparent and corrected FRET efficiencies, detection efficiency correction factor (gamma), spectral crosstalk and direct excitation correction factors, and stoichiometry in the both apparent and corrected FRET efficiency cases. All the options provided on this whole GUI can be updated any time later while handling and fitting the plots.   

.. figure:: ./../figures/documents/PA_histogram_GUI.png
   :width: 600
   :alt: histogram tab GUI
   :align: center
   :name: Histograms_tab_GUI

   The *Histogram*-GUI of Deep-LASI has several sub-windows for plotting data and fitting

On the panel *Display Settings* one can choose how to show the results considering the various options provided for plotting and fitting (:numref:`display-settings`). When creating a plot including the FRET efficiency, you can choose the histogram type from a drop-down menu to be framewise, moleculewise, or both at the same time. A framewise histogram consists of all the FRET efficiencies observed from all the detected molecules on each frame gathered from the whole measured frames, whereas a moleculewise histogram shows the distribution of average FRET efficiencies for each molecule during all the measured frames. Comparing these two types of graphs can give a hint about the presence of conformational changes in the system under study. 

.. figure:: ./../figures/documents/PA_display_settings.png
   :width: 600
   :alt: histogram settings
   :align: center
   :name: display-settings

   Various options for plotting and fitting histograms on the panel *Display Settings*

The second drop-down menu on :numref:`display-settings` includes options about plot normalization. Depending on your purpose of data visualization, you can decide on showing the *Y* axis without any change, so reporting the number of occurrences without normalization as the default option. You could also normalize the histogram in two different modes. With normalization regarding to probability, the sum of all the possible occurrences is set to one, and we get a probability distribution for the measured values. On the other hand, with the *Unary* normalization, the highest occurrence will be set to one, and the rest of the values will be shown proportionate to that maximum one. 

On the *Fit Method* drop-down menu, a long list of fitting options is provided to cover a wide range of distribution functions and describe the measured system more precisely. The default is always set to *No fit*, and the first option is to fit the histogram with a Gaussian function up to three populations. Single and double exponential functions, polynomial function up to five degrees, Weibull distribution, and also first and second power functions are the other fitting options provided (:numref:`display-settings`).

When you have the fitting method selected, the next step is to set the *Fit Interval*, which you can usually use the default range set to infinite numbers unless you have a particular range of values in mind. Finally, you can change the number of bins for plotted histogram(s) depending on the statistics you get. 

With all the settings, you can click on *Fit Plots* and get the fitting results on the allocated panel as you can see on :numref:`Histograms_tab_GUI` on the bottom. Sometimes fitting does not happen successfully at first, meaning that the software might fail to fit on the first attempt. In such a case, based on the fitting method and the approximate values visible on the plot, we can guide the fitting closer to the correct values, and then let Deep-LASI do it more exactly. As an example, if you had chosen *Gauss1*, a table like :numref:`Histograms_tab_GUI` would be produced to report the fitting results. In case fitting was not performed, you will get a message as *Fit failed*, and you can try to fix this issue manually.




