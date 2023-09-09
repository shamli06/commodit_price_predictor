# commodity-price-predictor
![coverage](https://img.shields.io/badge/Python-3.10.9-purple) ![coverage](https://img.shields.io/badge/Framework-Streamlit-orange)

# How to run Project

1. Clone the repository and run laptop-price-predictor.ipynb & mobile-price-predictor.ipynb on jupyter notebook.
2. There are two csv file laptop_data.csv & mobile_data.csv download them.
3. Create PyCharm project
4. Add App.py file
5. Also add pickle files generated from laptop-price-predictor.ipynb & mobile-price-predictor.ipynb
6. Run command "streamlit run App.py" in the terminal.

# Project Overview

- It is a Web-based application that predicts the price of the laptop and mobile according to the configuration input by user.
- For Laptop, model predicts a price on the basis of Company,	TypeName,	Ram,	Weight,	TouchScreen,	IPS,	ppi,	Cpu brand,	HDD,	SSD,	Gpu_brand, os.
- For Mobile, model predicts a price on the basis of	RAM,	ROM,	Mobile_Size,	Primary_Cam,	Selfi_Cam, Battery_Power.
- For Laptop, kaggle dataset is used containing 1303 laptops.
- For Mobile, dataset used from webscraping of ecommerce website containing 836 mobiles.

  ## Laptop's actual price and predicted price


<img width="1023" alt="Screenshot 2023-09-09 at 1 06 00 PM" src="https://github.com/shamli06/commodity_price_predictor/assets/66312689/fa52d2d3-86c1-4ee9-b9d5-19a5d90fb747">

<img width="597" alt="Screenshot 2023-09-09 at 1 36 05 PM" src="https://github.com/shamli06/commodity_price_predictor/assets/66312689/5c117336-07a7-4daa-8ddc-94c1eba3f506">



## Mobile's actual price and predicted price

<img width="1023" alt="Screenshot 2023-09-09 at 1 10 34 PM" src="https://github.com/shamli06/commodity_price_predictor/assets/66312689/056358f5-dbbe-4dc4-895d-43aabc797087">

<img width="597" alt="Screenshot 2023-09-09 at 1 32 51 PM" src="https://github.com/shamli06/commodity_price_predictor/assets/66312689/fd0d2276-99bc-4661-8eff-849d8daf206c">









