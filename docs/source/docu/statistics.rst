.. |br| raw:: html

   <br />


Selected traces and categories
~~~~~~~~~~~~~~~~~~~~

DeepLASI also provides statistical information about single molecule measurements. By moving on to the **Statistics** tab (:numref:`statistics_tab`), right after choosing any category from the category(s) table, one can obtain information about the data quality with several histogrmas and corresponding fitting results.

As you can see on :numref:`categories_in_selector_table`, the whole GUI is devided into four columns, each representing a detection channel. For each channel, five panels are provided to report the number of events for several criteria including: *Total signal*, *Mean BG and Signal*, *Countrate*, *Signal to Noise*, and *Bleaching time*.
After having the traces categorized, you can choose the desired category from the same sorting table as you defined earlier. for an example see the zoomed-in panel on the right side of :numref:`categories_in_selector_table`. Then the program will show the columns related to the number of channels which was previously defined, and updates histograms with fitting results. For example, for a two-channel measurement, only the first and second columns appear with histograms. With clicking on any other category, DeepLASI will immediately update the whole panels. 

.. figure:: ./../figures/documents/PA_statistics_tab.png
   :width: 500
   :alt: statistics tab
   :align: center
   :name: statistics_tab

   Statistics tab on the main-GUI

.. figure:: ./../figures/documents/PA_statistics_selector_table.png
   :width: 700
   :alt: categories_selector_table
   :align: center
   :name: categories_in_selector_table

   Statistics environment with subpanels for all channels with the same categories table

.. figure:: ./../figures/documents/EP_Figure_Statistics.png
   :width: 300
   :alt: histograms showing measurement statistics
   :align: center
   :name: histograms_measurement_details

   Histograms showing measurement statistics with fitting results

The fitting results are provided in a table on the right side.

.. figure:: ./../figures/documents/PA_statistics_fit_results.png
   :width: 600
   :alt: fitting results for measurement statistics
   :align: center
   :name: measurement_statistics_fit_result

   Fitting results table to report the details about a specific category statistics


Then you can move on to the **FRET** tab, and again choose the desired category by clicking on the plus sign beside the list.

.. figure:: ./../figures/documents/PA_Fig_25_FRET_Tab.png
   :width: 300
   :alt: FRET tab
   :align: center
   :name: FRET tab

   FRET tab on the GUI

.. figure:: ./../figures/documents/PA_Fig_26_FRET_Tab_Categories.png
   :width: 500
   :alt: FRET tab categories
   :align: center
   :name: choosing categories on FRET tab

   Choosing desired category(ies) on *FRET* tab

After choosing the category, you can select from the **Plot Mode** which plot to get. In the example shown on figure 26, you get the histogram of apparent FRET efficiency, like the one in figure 27.

.. figure:: ./../figures/documents/PA_Fig_27_Result_Histogram.png
   :width: 400
   :alt: apparent FRET histogram
   :align: center
   :name: apparent FRET histogram

   An exemplary histogram of apparent FRET efficiency with two populations

There are options in **Display Settings** (see figure 28) to make the frame-wise and/or molecule-wise plot visible, normalize them, and also to fit them by choosing the best fitting method. If sometimes fitting seems so wrong, you can manually insert some values based on what you roughly see on the plot, fix them and fit again. By playing around the fitting gets better, then you can uncheck the fixing boxes and let the program find the best fitting values. You can also change the color of your plot(s) by clicking on the colored rectangle and choose a desired color.

.. figure:: ./../figures/documents/PA_Fig_28_Fitting_Histogram.png
   :width: 500
   :alt: display settings
   :align: center
   :name: result display settings

   Display settings for the resulting plots
