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

As shown on :numref:`Histograms_tab_GUI`, the provided tab consists of several panels. The panel *Plots* displays any created graph(s), and in case of fitting them, also fitting results attached to the plot(s). The panel *Data Selection* shows the same categories created before with the number of traces on each category. On the section *Plot Mode*, you can choose the desired parameter to be plotted. The provided list of parameters includes apparent and corrected FRET efficiencies, detection efficiency correction factor (gamma), spectral crosstalk and direct excitation correction factors, and stoichiometry in the both apparent and corrected FRET efficiency cases. All the options provided on this whole GUI can be updated or changed any time later while handling and fitting the plots.   

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

With all the settings, you can click on *Fit Plots* and get the fitting results on the allocated panel as you can see on :numref:`Histograms_tab_GUI` at the bottom. Sometimes fitting does not happen successfully at first, meaning that the software might fail to fit on the first attempt. In such a case, based on the fitting method and the approximate values visible on the plot, we can guide the fitting results to get closer to the correct values, and then let Deep-LASI do it more exactly. As an example, suppose we had chosen *Gauss1* as the fitting method, then a table like :numref:`fitting-parameters-table` would be produced to report the fitting results. In case the fitting fails, you will get a message as *Fit failed*, and you can try to fix this issue manually. Meaning that you enter a rough value for a and b with having them fixed by checking on the box beside each of them. This rough values you can get by just checking the maximum value on your y axis, and estimate the corresponding x value for a and b respectively. Now if you click on *Fit Plots* again, you will get a fitting with the fixed values you entered. Then, one can uncheck the fixing boxes, click on *Fit Plots* once more, and get the more precise fitting performed by the program. The fitting results will be updated on both the current box and on the plot panel. In case of choosing other fitting methods, the parameters assigned to a, b or c might change, and the user should usually have a slight idea what each parameter would mean in the applied fitting function.   

.. figure:: ./../figures/documents/PA_fitting_result_table.png
   :width: 300
   :alt: fitting parameters
   :align: center
   :name: fitting-parameters-table

   The fitting results table at the bottom of the histograms tab main-GUI

When you create a plot, the table *Plot Settings* on the left bottom of the window (:numref:`plot-settings-table`) also gets updated. It shows any category that you selected for plotting from which you can choose to be on the plot by checking or unchecking the filtering box on the left side. The third column is to show the number of traces in the present category. The fourth column is to determine the desired color for each plot. By clicking on the colored box, you can set the color as you wish.  

.. figure:: ./../figures/documents/PA_plot_settings_table.png
   :width: 500
   :alt: plot settings
   :align: center
   :name: plot-settings-table

   The table for adjusting plot settings 

Clicking on the colored box, opens a window like the left one on :numref:`plot-color_settings`, letting the user choose a color from the standard ones offered by the program. The recently used colors and a preview of the current choice are also displayed. In case one likes to set a color different from the provided ones, by clicking on the top right corner, the window for custom colors will open with various options. You can use any of the two sliders to choose a desired region of colors. There is also a drop-down menu with four options including: RGB with the scale 0 to 1 which is the default, RGB with the scale 0 to 255, Hex, and HSV. In each selected case, the user has the freedom to set different coloring values or codes.  

.. figure:: ./../figures/documents/PA_plot_color.png
   :width: 450
   :alt: plot color
   :align: center
   :name: plot-color_settings

   The GUI for setting the desired colors for plotting
   
