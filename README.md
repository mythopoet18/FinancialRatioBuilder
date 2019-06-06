# FinancialRatioBuilder
The current version generates estimated current ratios using Twitter tweets.

You can find specific instruction in the JupyterNotebook
 * `Build Financial Analysis From Scratch-Deliver.ipynb`
 * Required packages are located in the `requirements` file. You can install the first three packages, `scrapy` `mongodb` and `mysql-connector` by running the cell in the above notebook.

The files in the folders are described as follows:
* `Build Financial Analysis From Scratch-Deliver.ipynb` -- Interactive Jupyter Notebook to make prediction
   * `Structured.py` -- supporting functions to construct structured features for prediction
   * `ParseTweet.py` -- supporting functions to parse tweets to unstructured features for prediction
   * `SelectInput.py` -- generate ipywidget to take input
   * `country_dict.pickle` -- translate country name to two letter ISO code
   * `us_state_list.pickle` -- list of two letter US state names
   * `canada_state_list.pickle` -- list of two letter Canada state names
   * `sic_reg.pickle` -- translate division and industry to four digit sic code 
   * `datax_header.pickle` -- regulate structured data
   * `ridgemodel.pickle` -- first part of the pre-trained model using mean estimator
   * `sentimentmodel.pickle` -- second part of the pre-trained model using sentiment analysis
   
The following files are included to support TweeterScraper App:
* `TweeterScraperReadMe.md`, no need to read and do not need to follow its instruction
* `LICENSE`, license of the app
* `scrapy.cfg` and folder `TweetScraper` are part of the App. They should not be removed.
* Temporary folder `Data` and temporary file `get_tweet.sh` will be generated to collect tweets
