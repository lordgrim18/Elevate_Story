# Elevate Story

This repository contains the Gen-AI model developed for the Elevate app. The model is hosted on the Hugging Face model hub: [lordgrim18/llama2-elevate-story-3](https://huggingface.co/lordgrim18/llama2-elevate-story-3/tree/main)

## Repository Contents

### Data Extraction

- `scraper.py`: Python script for scraping stories from [Archive of Our Own](https://archiveofourown.org/).
- `data.csv`: CSV file containing extracted stories including its url, title.

### Data Manipulation

#### Initial Cleaning

- `initial_cleaning.ipynb`: Jupyter Notebook for initial data cleaning.
- `cleaned_data.csv`: CSV file containing cleaned data after the initial cleaning process.

#### Data Augmentation

- `Basic_llama_working.ipynb`: Jupyter Notebook demonstrating basic usage of the Llama model.
- `data_augmentation.ipynb`: Jupyter Notebook for data augmentation using the Llama model.
- `output.csv`: CSV file containing augmented data.

#### Final Data

- `final_touches.ipynb`: Jupyter Notebook for final data preparation which is uploaded into huggingface - [lordgrim18/story-2](https://huggingface.co/datasets/lordgrim18/story-2) .
- `train.csv`: CSV file containing the final training data which is in the form that is used to fine tune the - [NousResearch/Llama-2-7b-hf](https://huggingface.co/NousResearch/Llama-2-7b-hf).

### Model Development

#### Training and Saving

- `training_saving.ipynb`: Jupyter Notebook for training the Gen-AI model and saving the trained model.

#### Testing

- `testing.ipynb`: Jupyter Notebook for testing the Gen-AI model.

## Usage

You can use this repository to explore and understand the development and deployment, from obtaining the data and creating a dataset to saving and testing the Gen-AI model for the Elevate app.
