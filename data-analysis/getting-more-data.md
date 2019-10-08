# Weather data

What if we collected a lot af data.. fast forward to 10 years from now.. then we could analyse it..
After you collected some data you could do all the things in our [time series tutorial](https://github.com/pyladieshamburg/getting-started-raspberry-pi/tree/master/analysis).

Additionally we can also get different data from the Hamburg university, the [ICDC Data Center](https://icdc.cen.uni-hamburg.de/1/daten/atmosphere/dwd-station.html).

## Setup instructions

First create the environment and setup the environment locally, by running:

- `conda env create -f environment.yaml` will create the conda environemnt used for mlflow runs
- `activate weather` will activate the environment .. hopefully
- `pyenv local miniconda3-latest/envs/weather` might work if miniconda3-latest installed with pyenv

To get jupyter lab to be plotly friendly you can install some stuff from [here](https://plot.ly/python/getting-started/) .. but it takes a while.

For dabbing into data series we will follow this [tutorial on time series](https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b)
