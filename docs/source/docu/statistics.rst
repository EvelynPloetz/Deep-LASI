.. |br| raw:: html

   <br />


Selected traces and categories
~~~~~~~~~~~~~~~~~~~~

To get more information about the system under study, DeepLASI provides statistical information about single molecule measurements. When having traces loaded to the program, by moving on to the **Statistics** tab (:numref:`statistics_tab`), and selecting any category from the table, one can obtain information about the data quality with several histograms and corresponding fitting results, regarding to flourophores brightness, their photo-activity time range, and signal to noise ratio.

As you can see on :numref:`categories_in_selector_table`, the whole GUI is devided into four columns, each representing a detection channel. For each channel, five panels are provided to report the number of events for several criteria including: *Total signal*, *Mean BG and Signal*, *Countrate*, *Signal to Noise*, and *Bleaching time*.

After having the traces loaded to DeepLASI, the *Selector Table* on the right side of the GUI gets updated showing the same sorting table as the user has defined earlier, for an example see the zoomed-in panel on the right side of :numref:`categories_in_selector_table`. Also, the number of columns on the left panel, gets updated depending on the number of channels used for the experiment. For example, for a two-channel measurement, only the first and second columns show histograms, the other two columns will disappear automatically.

.. figure:: ./../figures/documents/PA_statistics_tab.png
   :width: 500
   :alt: statistics tab
   :align: center
   :name: statistics_tab

   Statistics tab on the main-GUI of DeepLASI

.. figure:: ./../figures/documents/PA_statistics_selector_table.png
   :width: 700
   :alt: categories_selector_table
   :align: center
   :name: categories_in_selector_table

   Statistics environment with subpanels for all channels with the same categories table

You can now choose the desired category to see the histograms for each channel, and obtain the fitting results in the table *Fit Results* on the bottom right position. The fitting results table will also be devided in separate columns depending on the number of used channels. With clicking on any other category, DeepLASI will immediately update the whole panels with the fitting results. 

An example of created histograms and corresponding fits under the *Statistics* tab is depicted on :numref:`histograms_measurement_details`. The plots on each column represent the detection channel color, for example :numref:`histograms_measurement_details` shows the histograms in green, so the reported plots and values are from the data on green channel. 

.. figure:: ./../figures/documents/EP_Figure_Statistics.png
   :width: 250
   :alt: histograms showing measurement statistics
   :align: center
   :name: histograms_measurement_details

   Histograms showing measurement statistics for green channel

The *fit Results* table provided on the right side of the statistics GUI, includes measurement criteria listed on :numref:`Fit Results table`.

.. .. figure:: ./../figures/documents/PA_statistics_fit_results.png
..   :width: 600
..   :alt: fitting results for measurement statistics
..   :align: center
..   :name: measurement_statistics_fit_result

..  Fitting results table to report the details about a specific category statistics

.. list-table:: Fit Results
   :widths: 35 160
   :header-rows: 1
   :name: Fit Results table

   * - *Fit Result*
     - Definition
   * - *File Name*
     - The data file name given by the user
   * - :math:`N_{files}`
     - The number of data files saved in the measurement folder
   * - *Filters*
     - ???
   * - :math:`N_{traces}[Total]`
     - The total number of extracted traces
   * - :math:`N_{traces}[filtered]`
     - The number of traces in the selected category
   * - :math:`t_{frame}[ms]`
     - The sum of exposure and interframe time
   * - :math:`A_{sig}`
     - The number of events of the total signal
   * - :math:`A_{1/2}`
     - The total count rate on the channel???
   * - :math:`\mu_{sig}[A.U.]`
     - The mean value of signal
   * - :math:`\sigma_{sig}[A.U.]`
     - The standard deviation of signal
   * - :math:`\mu_{BG}[A.U.]`
     - The mean value of background
   * - :math:`\sigma_{BG}[A.U.]`
     - The standard deviation of background
   * - :math:`\mu_{CR}[kHz]`
     - The mean value of count rate
   * - :math:`\sigma_{CR}[kHz]`
     - The standard deviation of count rate
   * - :math:`\mu_{SNR}`
     - The mean value of signal to noise ratio
   * - :math:`\sigma_{SNR}`
     - The standard deviation of signal to noise ratio
   * - :math:`A_{bleach}`
     - The number of events of observed bleaching times
   * - :math:`t_{bleach,1/2}[s]`
     - The time interval before the flourophore photo-bleaching
     
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
