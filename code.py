{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2T32Y3sPVB46"
   },
   "source": [
    "Importing the libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "CnLLjXJQU7tb"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import statsmodels.api as sm\n",
    "import pylab as py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "P9_1nNpvVP6A"
   },
   "source": [
    "**Importing the dataset**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "KD_4x7NbLsEB"
   },
   "outputs": [],
   "source": [
    "dataset=pd.read_csv('DATA FOR PROJECT (2).csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 235
    },
    "id": "oPHv7nWOLvRG",
    "outputId": "c557295b-afa8-48ee-c553-462bfb5a7ad2"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aes</th>\n",
       "      <th>wmo</th>\n",
       "      <th>temp</th>\n",
       "      <th>td</th>\n",
       "      <th>rh</th>\n",
       "      <th>ws</th>\n",
       "      <th>wg</th>\n",
       "      <th>wdir</th>\n",
       "      <th>pres</th>\n",
       "      <th>vis</th>\n",
       "      <th>...</th>\n",
       "      <th>rndays</th>\n",
       "      <th>sog</th>\n",
       "      <th>ffmc</th>\n",
       "      <th>dmc</th>\n",
       "      <th>dc</th>\n",
       "      <th>bui</th>\n",
       "      <th>isi</th>\n",
       "      <th>fwi</th>\n",
       "      <th>dsr</th>\n",
       "      <th>Fire/Not Fire</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1012475</td>\n",
       "      <td>71031</td>\n",
       "      <td>9.5</td>\n",
       "      <td>8.6</td>\n",
       "      <td>94.0</td>\n",
       "      <td>8.6</td>\n",
       "      <td>23.2</td>\n",
       "      <td>261</td>\n",
       "      <td>1007.7</td>\n",
       "      <td>24.5</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>8.9</td>\n",
       "      <td>0.1</td>\n",
       "      <td>85.6</td>\n",
       "      <td>0.1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1012710</td>\n",
       "      <td>71798</td>\n",
       "      <td>10.2</td>\n",
       "      <td>6.2</td>\n",
       "      <td>76.0</td>\n",
       "      <td>35.8</td>\n",
       "      <td>45.7</td>\n",
       "      <td>252</td>\n",
       "      <td>1007.8</td>\n",
       "      <td>24.7</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>35.6</td>\n",
       "      <td>0.3</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1014820</td>\n",
       "      <td>71774</td>\n",
       "      <td>9.4</td>\n",
       "      <td>5.5</td>\n",
       "      <td>76.9</td>\n",
       "      <td>23.4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>255</td>\n",
       "      <td>1006.6</td>\n",
       "      <td>39.6</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1015630</td>\n",
       "      <td>71927</td>\n",
       "      <td>11.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>61.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>24.1</td>\n",
       "      <td>257</td>\n",
       "      <td>1007.0</td>\n",
       "      <td>39.8</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>36.9</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1.8</td>\n",
       "      <td>0.6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1016640</td>\n",
       "      <td>71778</td>\n",
       "      <td>9.2</td>\n",
       "      <td>6.9</td>\n",
       "      <td>85.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>54.0</td>\n",
       "      <td>259</td>\n",
       "      <td>1008.8</td>\n",
       "      <td>26.6</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>28.8</td>\n",
       "      <td>0.2</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       aes    wmo  temp   td    rh    ws    wg  wdir    pres   vis  ...  \\\n",
       "0  1012475  71031   9.5  8.6  94.0   8.6  23.2   261  1007.7  24.5  ...   \n",
       "1  1012710  71798  10.2  6.2  76.0  35.8  45.7   252  1007.8  24.7  ...   \n",
       "2  1014820  71774   9.4  5.5  76.9  23.4   NaN   255  1006.6  39.6  ...   \n",
       "3  1015630  71927  11.6  4.4  61.0  12.0  24.1   257  1007.0  39.8  ...   \n",
       "4  1016640  71778   9.2  6.9  85.0  45.0  54.0   259  1008.8  26.6  ...   \n",
       "\n",
       "   rndays  sog  ffmc  dmc    dc  bui  isi  fwi  dsr  Fire/Not Fire  \n",
       "0       0  0.0   8.9  0.1  85.6  0.1  0.0  0.0  0.0            0.0  \n",
       "1       0  0.0  35.6  0.3   1.5  0.4  0.1  0.0  0.0            0.0  \n",
       "2       0  0.0   NaN  NaN   NaN  NaN  NaN  NaN  NaN            NaN  \n",
       "3       0  0.0  36.9  0.5   1.8  0.6  0.0  0.0  0.0            0.0  \n",
       "4       0  0.0  28.8  0.2   1.4  0.2  0.0  0.0  0.0            0.0  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 279
    },
    "id": "YdLr9zwyRPn4",
    "outputId": "5bfa70a3-5d15-41d2-a135-531c29a70896"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aes</th>\n",
       "      <th>wmo</th>\n",
       "      <th>temp</th>\n",
       "      <th>td</th>\n",
       "      <th>rh</th>\n",
       "      <th>ws</th>\n",
       "      <th>wg</th>\n",
       "      <th>wdir</th>\n",
       "      <th>pres</th>\n",
       "      <th>vis</th>\n",
       "      <th>...</th>\n",
       "      <th>rndays</th>\n",
       "      <th>sog</th>\n",
       "      <th>ffmc</th>\n",
       "      <th>dmc</th>\n",
       "      <th>dc</th>\n",
       "      <th>bui</th>\n",
       "      <th>isi</th>\n",
       "      <th>fwi</th>\n",
       "      <th>dsr</th>\n",
       "      <th>Fire/Not Fire</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>754607</th>\n",
       "      <td>8502580</td>\n",
       "      <td>718143</td>\n",
       "      <td>21.5</td>\n",
       "      <td>13.1</td>\n",
       "      <td>58.0</td>\n",
       "      <td>34.6</td>\n",
       "      <td>NaN</td>\n",
       "      <td>230</td>\n",
       "      <td>1009.00</td>\n",
       "      <td>19.5</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754608</th>\n",
       "      <td>8502592</td>\n",
       "      <td>71339</td>\n",
       "      <td>21.6</td>\n",
       "      <td>9.7</td>\n",
       "      <td>46.0</td>\n",
       "      <td>35.3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>219</td>\n",
       "      <td>1015.50</td>\n",
       "      <td>16.1</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>81.7</td>\n",
       "      <td>8.6</td>\n",
       "      <td>53.5</td>\n",
       "      <td>12.3</td>\n",
       "      <td>8.2</td>\n",
       "      <td>9.4</td>\n",
       "      <td>1.4</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754609</th>\n",
       "      <td>8502801</td>\n",
       "      <td>71902</td>\n",
       "      <td>18.3</td>\n",
       "      <td>12.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>291</td>\n",
       "      <td>1006.40</td>\n",
       "      <td>17.7</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>67.1</td>\n",
       "      <td>4.9</td>\n",
       "      <td>28.4</td>\n",
       "      <td>6.8</td>\n",
       "      <td>2.7</td>\n",
       "      <td>2.1</td>\n",
       "      <td>0.1</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754610</th>\n",
       "      <td>8503249</td>\n",
       "      <td>71335</td>\n",
       "      <td>15.9</td>\n",
       "      <td>11.6</td>\n",
       "      <td>75.7</td>\n",
       "      <td>24.1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>290</td>\n",
       "      <td>1008.65</td>\n",
       "      <td>17.2</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754611</th>\n",
       "      <td>8504175</td>\n",
       "      <td>71825</td>\n",
       "      <td>12.1</td>\n",
       "      <td>11.4</td>\n",
       "      <td>96.0</td>\n",
       "      <td>7.6</td>\n",
       "      <td>NaN</td>\n",
       "      <td>250</td>\n",
       "      <td>1013.70</td>\n",
       "      <td>9.7</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10.4</td>\n",
       "      <td>3.1</td>\n",
       "      <td>63.4</td>\n",
       "      <td>5.6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            aes     wmo  temp    td    rh    ws  wg  wdir     pres   vis  ...  \\\n",
       "754607  8502580  718143  21.5  13.1  58.0  34.6 NaN   230  1009.00  19.5  ...   \n",
       "754608  8502592   71339  21.6   9.7  46.0  35.3 NaN   219  1015.50  16.1  ...   \n",
       "754609  8502801   71902  18.3  12.0  66.0  31.0 NaN   291  1006.40  17.7  ...   \n",
       "754610  8503249   71335  15.9  11.6  75.7  24.1 NaN   290  1008.65  17.2  ...   \n",
       "754611  8504175   71825  12.1  11.4  96.0   7.6 NaN   250  1013.70   9.7  ...   \n",
       "\n",
       "        rndays  sog  ffmc  dmc    dc   bui  isi  fwi  dsr  Fire/Not Fire  \n",
       "754607       0  0.0   NaN  NaN   NaN   NaN  NaN  NaN  NaN            NaN  \n",
       "754608       0  0.0  81.7  8.6  53.5  12.3  8.2  9.4  1.4            1.0  \n",
       "754609       0  0.0  67.1  4.9  28.4   6.8  2.7  2.1  0.1            0.0  \n",
       "754610       0  0.0   NaN  NaN   NaN   NaN  NaN  NaN  NaN            NaN  \n",
       "754611       0  0.0  10.4  3.1  63.4   5.6  0.0  0.0  0.0            0.0  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "HnVkYhq4RToc",
    "outputId": "9ab25f6c-8677-44a8-d38f-717d2effbfc0"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(754612, 21)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Kp8tGnXMRcNM",
    "outputId": "c1393371-81d3-441a-f797-d1912addbad4"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "aes               object\n",
       "wmo                int64\n",
       "temp             float64\n",
       "td               float64\n",
       "rh               float64\n",
       "ws               float64\n",
       "wg               float64\n",
       "wdir               int64\n",
       "pres             float64\n",
       "vis              float64\n",
       "precip           float64\n",
       "rndays             int64\n",
       "sog              float64\n",
       "ffmc             float64\n",
       "dmc              float64\n",
       "dc               float64\n",
       "bui              float64\n",
       "isi              float64\n",
       "fwi              float64\n",
       "dsr              float64\n",
       "Fire/Not Fire    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "_zqx-LPCTrTb",
    "outputId": "9b1c16c5-3be8-492b-89bf-1bb905c57a87"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "aes              754612\n",
       "wmo              754612\n",
       "temp             754612\n",
       "td               753395\n",
       "rh               754297\n",
       "ws               754612\n",
       "wg               505324\n",
       "wdir             754612\n",
       "pres             754612\n",
       "vis              754612\n",
       "precip           754606\n",
       "rndays           754612\n",
       "sog              754211\n",
       "ffmc             356350\n",
       "dmc              356350\n",
       "dc               356350\n",
       "bui              331513\n",
       "isi              331513\n",
       "fwi              331511\n",
       "dsr              331513\n",
       "Fire/Not Fire    331171\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 382
    },
    "id": "evvQZ-mOTz6l",
    "outputId": "ea1dcbc9-c35d-40db-8191-aab040ce1450"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>wmo</th>\n",
       "      <th>temp</th>\n",
       "      <th>td</th>\n",
       "      <th>rh</th>\n",
       "      <th>ws</th>\n",
       "      <th>wg</th>\n",
       "      <th>wdir</th>\n",
       "      <th>pres</th>\n",
       "      <th>vis</th>\n",
       "      <th>precip</th>\n",
       "      <th>rndays</th>\n",
       "      <th>sog</th>\n",
       "      <th>ffmc</th>\n",
       "      <th>dmc</th>\n",
       "      <th>dc</th>\n",
       "      <th>bui</th>\n",
       "      <th>isi</th>\n",
       "      <th>fwi</th>\n",
       "      <th>dsr</th>\n",
       "      <th>Fire/Not Fire</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>754612.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>753395.000000</td>\n",
       "      <td>754297.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>505324.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>754606.000000</td>\n",
       "      <td>754612.000000</td>\n",
       "      <td>754211.000000</td>\n",
       "      <td>356350.000000</td>\n",
       "      <td>356350.000000</td>\n",
       "      <td>356350.000000</td>\n",
       "      <td>331513.000000</td>\n",
       "      <td>331513.000000</td>\n",
       "      <td>331511.000000</td>\n",
       "      <td>331513.000000</td>\n",
       "      <td>331171.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>124242.705284</td>\n",
       "      <td>4.312816</td>\n",
       "      <td>-2.683438</td>\n",
       "      <td>64.691775</td>\n",
       "      <td>15.509444</td>\n",
       "      <td>21.874862</td>\n",
       "      <td>202.346402</td>\n",
       "      <td>1013.862838</td>\n",
       "      <td>22.221685</td>\n",
       "      <td>2.045405</td>\n",
       "      <td>2.388090</td>\n",
       "      <td>6.866321</td>\n",
       "      <td>71.858225</td>\n",
       "      <td>24.751470</td>\n",
       "      <td>234.138806</td>\n",
       "      <td>37.201989</td>\n",
       "      <td>5.046056</td>\n",
       "      <td>10.537483</td>\n",
       "      <td>3.672935</td>\n",
       "      <td>0.501309</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>176422.137155</td>\n",
       "      <td>14.341734</td>\n",
       "      <td>12.562019</td>\n",
       "      <td>20.058945</td>\n",
       "      <td>10.295933</td>\n",
       "      <td>13.711197</td>\n",
       "      <td>99.249900</td>\n",
       "      <td>36.451693</td>\n",
       "      <td>11.174547</td>\n",
       "      <td>6.864991</td>\n",
       "      <td>12.043255</td>\n",
       "      <td>16.885212</td>\n",
       "      <td>21.487024</td>\n",
       "      <td>28.841217</td>\n",
       "      <td>198.661422</td>\n",
       "      <td>39.147795</td>\n",
       "      <td>7.166045</td>\n",
       "      <td>13.979376</td>\n",
       "      <td>8.937813</td>\n",
       "      <td>0.499999</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>71001.000000</td>\n",
       "      <td>-53.600000</td>\n",
       "      <td>-55.400000</td>\n",
       "      <td>-77.400000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-7.690000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-99.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>71276.000000</td>\n",
       "      <td>-4.000000</td>\n",
       "      <td>-9.500000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>7.800000</td>\n",
       "      <td>11.400000</td>\n",
       "      <td>126.000000</td>\n",
       "      <td>1009.200000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>61.100000</td>\n",
       "      <td>5.700000</td>\n",
       "      <td>67.500000</td>\n",
       "      <td>9.700000</td>\n",
       "      <td>0.900000</td>\n",
       "      <td>0.600000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>71514.000000</td>\n",
       "      <td>5.700000</td>\n",
       "      <td>-1.200000</td>\n",
       "      <td>67.000000</td>\n",
       "      <td>13.400000</td>\n",
       "      <td>19.200000</td>\n",
       "      <td>219.000000</td>\n",
       "      <td>1015.150000</td>\n",
       "      <td>20.700000</td>\n",
       "      <td>0.010000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>81.200000</td>\n",
       "      <td>15.200000</td>\n",
       "      <td>191.600000</td>\n",
       "      <td>24.500000</td>\n",
       "      <td>2.900000</td>\n",
       "      <td>5.300000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>71793.000000</td>\n",
       "      <td>15.200000</td>\n",
       "      <td>6.500000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>20.600000</td>\n",
       "      <td>29.600000</td>\n",
       "      <td>285.000000</td>\n",
       "      <td>1021.200000</td>\n",
       "      <td>24.400000</td>\n",
       "      <td>1.200000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>87.500000</td>\n",
       "      <td>33.300000</td>\n",
       "      <td>354.475000</td>\n",
       "      <td>51.300000</td>\n",
       "      <td>6.700000</td>\n",
       "      <td>15.300000</td>\n",
       "      <td>3.400000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>719179.000000</td>\n",
       "      <td>43.500000</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>149.900000</td>\n",
       "      <td>149.500000</td>\n",
       "      <td>360.000000</td>\n",
       "      <td>1067.400000</td>\n",
       "      <td>96.500000</td>\n",
       "      <td>497.500000</td>\n",
       "      <td>666.000000</td>\n",
       "      <td>236.000000</td>\n",
       "      <td>98.900000</td>\n",
       "      <td>359.700000</td>\n",
       "      <td>1197.900000</td>\n",
       "      <td>380.700000</td>\n",
       "      <td>363.800000</td>\n",
       "      <td>203.500000</td>\n",
       "      <td>331.600000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 wmo           temp             td             rh  \\\n",
       "count  754612.000000  754612.000000  753395.000000  754297.000000   \n",
       "mean   124242.705284       4.312816      -2.683438      64.691775   \n",
       "std    176422.137155      14.341734      12.562019      20.058945   \n",
       "min     71001.000000     -53.600000     -55.400000     -77.400000   \n",
       "25%     71276.000000      -4.000000      -9.500000      50.000000   \n",
       "50%     71514.000000       5.700000      -1.200000      67.000000   \n",
       "75%     71793.000000      15.200000       6.500000      80.000000   \n",
       "max    719179.000000      43.500000      29.000000     100.000000   \n",
       "\n",
       "                  ws             wg           wdir           pres  \\\n",
       "count  754612.000000  505324.000000  754612.000000  754612.000000   \n",
       "mean       15.509444      21.874862     202.346402    1013.862838   \n",
       "std        10.295933      13.711197      99.249900      36.451693   \n",
       "min         0.000000       0.000000       0.000000       0.000000   \n",
       "25%         7.800000      11.400000     126.000000    1009.200000   \n",
       "50%        13.400000      19.200000     219.000000    1015.150000   \n",
       "75%        20.600000      29.600000     285.000000    1021.200000   \n",
       "max       149.900000     149.500000     360.000000    1067.400000   \n",
       "\n",
       "                 vis         precip         rndays            sog  \\\n",
       "count  754612.000000  754606.000000  754612.000000  754211.000000   \n",
       "mean       22.221685       2.045405       2.388090       6.866321   \n",
       "std        11.174547       6.864991      12.043255      16.885212   \n",
       "min         0.000000       0.000000       0.000000      -7.690000   \n",
       "25%        16.000000       0.000000       0.000000       0.000000   \n",
       "50%        20.700000       0.010000       1.000000       0.000000   \n",
       "75%        24.400000       1.200000       3.000000       2.000000   \n",
       "max        96.500000     497.500000     666.000000     236.000000   \n",
       "\n",
       "                ffmc            dmc             dc            bui  \\\n",
       "count  356350.000000  356350.000000  356350.000000  331513.000000   \n",
       "mean       71.858225      24.751470     234.138806      37.201989   \n",
       "std        21.487024      28.841217     198.661422      39.147795   \n",
       "min         0.000000       0.000000     -99.000000       0.000000   \n",
       "25%        61.100000       5.700000      67.500000       9.700000   \n",
       "50%        81.200000      15.200000     191.600000      24.500000   \n",
       "75%        87.500000      33.300000     354.475000      51.300000   \n",
       "max        98.900000     359.700000    1197.900000     380.700000   \n",
       "\n",
       "                 isi            fwi            dsr  Fire/Not Fire  \n",
       "count  331513.000000  331511.000000  331513.000000  331171.000000  \n",
       "mean        5.046056      10.537483       3.672935       0.501309  \n",
       "std         7.166045      13.979376       8.937813       0.499999  \n",
       "min         0.000000       0.000000       0.000000       0.000000  \n",
       "25%         0.900000       0.600000       0.000000       0.000000  \n",
       "50%         2.900000       5.300000       0.500000       1.000000  \n",
       "75%         6.700000      15.300000       3.400000       1.000000  \n",
       "max       363.800000     203.500000     331.600000       1.000000  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lRh5ueqsT5h5",
    "outputId": "62f55d62-c168-4ff0-a502-ee1f8eafe835"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 754612 entries, 0 to 754611\n",
      "Data columns (total 21 columns):\n",
      " #   Column         Non-Null Count   Dtype  \n",
      "---  ------         --------------   -----  \n",
      " 0   aes            754612 non-null  object \n",
      " 1   wmo            754612 non-null  int64  \n",
      " 2   temp           754612 non-null  float64\n",
      " 3   td             753395 non-null  float64\n",
      " 4   rh             754297 non-null  float64\n",
      " 5   ws             754612 non-null  float64\n",
      " 6   wg             505324 non-null  float64\n",
      " 7   wdir           754612 non-null  int64  \n",
      " 8   pres           754612 non-null  float64\n",
      " 9   vis            754612 non-null  float64\n",
      " 10  precip         754606 non-null  float64\n",
      " 11  rndays         754612 non-null  int64  \n",
      " 12  sog            754211 non-null  float64\n",
      " 13  ffmc           356350 non-null  float64\n",
      " 14  dmc            356350 non-null  float64\n",
      " 15  dc             356350 non-null  float64\n",
      " 16  bui            331513 non-null  float64\n",
      " 17  isi            331513 non-null  float64\n",
      " 18  fwi            331511 non-null  float64\n",
      " 19  dsr            331513 non-null  float64\n",
      " 20  Fire/Not Fire  331171 non-null  float64\n",
      "dtypes: float64(17), int64(3), object(1)\n",
      "memory usage: 120.9+ MB\n"
     ]
    }
   ],
   "source": [
    "dataset.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 485
    },
    "id": "Fgt7r7OYT7k1",
    "outputId": "2625c980-e7d8-4857-ef86-e81081c7f06a"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aes</th>\n",
       "      <th>wmo</th>\n",
       "      <th>temp</th>\n",
       "      <th>td</th>\n",
       "      <th>rh</th>\n",
       "      <th>ws</th>\n",
       "      <th>wg</th>\n",
       "      <th>wdir</th>\n",
       "      <th>pres</th>\n",
       "      <th>vis</th>\n",
       "      <th>...</th>\n",
       "      <th>rndays</th>\n",
       "      <th>sog</th>\n",
       "      <th>ffmc</th>\n",
       "      <th>dmc</th>\n",
       "      <th>dc</th>\n",
       "      <th>bui</th>\n",
       "      <th>isi</th>\n",
       "      <th>fwi</th>\n",
       "      <th>dsr</th>\n",
       "      <th>Fire/Not Fire</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754607</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754608</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754609</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754610</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754611</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>754612 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          aes    wmo   temp     td     rh     ws     wg   wdir   pres    vis  \\\n",
       "0       False  False  False  False  False  False  False  False  False  False   \n",
       "1       False  False  False  False  False  False  False  False  False  False   \n",
       "2       False  False  False  False  False  False   True  False  False  False   \n",
       "3       False  False  False  False  False  False  False  False  False  False   \n",
       "4       False  False  False  False  False  False  False  False  False  False   \n",
       "...       ...    ...    ...    ...    ...    ...    ...    ...    ...    ...   \n",
       "754607  False  False  False  False  False  False   True  False  False  False   \n",
       "754608  False  False  False  False  False  False   True  False  False  False   \n",
       "754609  False  False  False  False  False  False   True  False  False  False   \n",
       "754610  False  False  False  False  False  False   True  False  False  False   \n",
       "754611  False  False  False  False  False  False   True  False  False  False   \n",
       "\n",
       "        ...  rndays    sog   ffmc    dmc     dc    bui    isi    fwi    dsr  \\\n",
       "0       ...   False  False  False  False  False  False  False  False  False   \n",
       "1       ...   False  False  False  False  False  False  False  False  False   \n",
       "2       ...   False  False   True   True   True   True   True   True   True   \n",
       "3       ...   False  False  False  False  False  False  False  False  False   \n",
       "4       ...   False  False  False  False  False  False  False  False  False   \n",
       "...     ...     ...    ...    ...    ...    ...    ...    ...    ...    ...   \n",
       "754607  ...   False  False   True   True   True   True   True   True   True   \n",
       "754608  ...   False  False  False  False  False  False  False  False  False   \n",
       "754609  ...   False  False  False  False  False  False  False  False  False   \n",
       "754610  ...   False  False   True   True   True   True   True   True   True   \n",
       "754611  ...   False  False  False  False  False  False  False  False  False   \n",
       "\n",
       "        Fire/Not Fire  \n",
       "0               False  \n",
       "1               False  \n",
       "2                True  \n",
       "3               False  \n",
       "4               False  \n",
       "...               ...  \n",
       "754607           True  \n",
       "754608          False  \n",
       "754609          False  \n",
       "754610           True  \n",
       "754611          False  \n",
       "\n",
       "[754612 rows x 21 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 536
    },
    "id": "7FG4e2wPXn4p",
    "outputId": "d5f6e817-a099-4a36-bdef-52b830bf6965"
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'missingno'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_19736/4084429800.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmissingno\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mmsno\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mmsno\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbar\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdataset\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mcolor\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'pink'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'missingno'"
     ]
    }
   ],
   "source": [
    "import missingno as msno\n",
    "msno.bar(dataset,color='pink')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ji6eoCHtZ33l"
   },
   "source": [
    "Finding the locations of the missing value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 500
    },
    "id": "wMtS3-_VZ3Bd",
    "outputId": "60c6aea8-6368-4ba6-b1e5-6809fb6cf60e"
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'msno' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_19736/3575253498.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmsno\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmatrix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdataset\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'msno' is not defined"
     ]
    }
   ],
   "source": [
    "msno.matrix(dataset)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "bfsiNcMlT-br",
    "outputId": "db2339de-82cf-43da-b2cb-e8da7fdf9891"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "aes              0.000000\n",
       "wmo              0.000000\n",
       "temp             0.000000\n",
       "td               0.001613\n",
       "rh               0.000417\n",
       "ws               0.000000\n",
       "wg               0.330353\n",
       "wdir             0.000000\n",
       "pres             0.000000\n",
       "vis              0.000000\n",
       "precip           0.000008\n",
       "rndays           0.000000\n",
       "sog              0.000531\n",
       "ffmc             0.527771\n",
       "dmc              0.527771\n",
       "dc               0.527771\n",
       "bui              0.560684\n",
       "isi              0.560684\n",
       "fwi              0.560687\n",
       "dsr              0.560684\n",
       "Fire/Not Fire    0.561137\n",
       "dtype: float64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isna().sum()/dataset.shape[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zlQE0C5YVoCZ"
   },
   "source": [
    "Dropping rows and columns corresponding to missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "jn81ty-EFirz",
    "outputId": "70326b1f-6759-470d-c448-0f2c50affad5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            aes     wmo  temp    td    rh    ws    wg  wdir     pres   vis  \\\n",
      "0       1012475   71031   9.5   8.6  94.0   8.6  23.2   261  1007.70  24.5   \n",
      "1       1012710   71798  10.2   6.2  76.0  35.8  45.7   252  1007.80  24.7   \n",
      "2       1014820   71774   9.4   5.5  76.9  23.4   NaN   255  1006.60  39.6   \n",
      "3       1015630   71927  11.6   4.4  61.0  12.0  24.1   257  1007.00  39.8   \n",
      "4       1016640   71778   9.2   6.9  85.0  45.0  54.0   259  1008.80  26.6   \n",
      "...         ...     ...   ...   ...   ...   ...   ...   ...      ...   ...   \n",
      "754607  8502580  718143  21.5  13.1  58.0  34.6   NaN   230  1009.00  19.5   \n",
      "754608  8502592   71339  21.6   9.7  46.0  35.3   NaN   219  1015.50  16.1   \n",
      "754609  8502801   71902  18.3  12.0  66.0  31.0   NaN   291  1006.40  17.7   \n",
      "754610  8503249   71335  15.9  11.6  75.7  24.1   NaN   290  1008.65  17.2   \n",
      "754611  8504175   71825  12.1  11.4  96.0   7.6   NaN   250  1013.70   9.7   \n",
      "\n",
      "        ...  rndays  sog  ffmc  dmc    dc   bui  isi  fwi  dsr  Fire/Not Fire  \n",
      "0       ...       0  0.0   8.9  0.1  85.6   0.1  0.0  0.0  0.0            0.0  \n",
      "1       ...       0  0.0  35.6  0.3   1.5   0.4  0.1  0.0  0.0            0.0  \n",
      "2       ...       0  0.0   NaN  NaN   NaN   NaN  NaN  NaN  NaN            NaN  \n",
      "3       ...       0  0.0  36.9  0.5   1.8   0.6  0.0  0.0  0.0            0.0  \n",
      "4       ...       0  0.0  28.8  0.2   1.4   0.2  0.0  0.0  0.0            0.0  \n",
      "...     ...     ...  ...   ...  ...   ...   ...  ...  ...  ...            ...  \n",
      "754607  ...       0  0.0   NaN  NaN   NaN   NaN  NaN  NaN  NaN            NaN  \n",
      "754608  ...       0  0.0  81.7  8.6  53.5  12.3  8.2  9.4  1.4            1.0  \n",
      "754609  ...       0  0.0  67.1  4.9  28.4   6.8  2.7  2.1  0.1            0.0  \n",
      "754610  ...       0  0.0   NaN  NaN   NaN   NaN  NaN  NaN  NaN            NaN  \n",
      "754611  ...       0  0.0  10.4  3.1  63.4   5.6  0.0  0.0  0.0            0.0  \n",
      "\n",
      "[754612 rows x 21 columns]\n"
     ]
    }
   ],
   "source": [
    "print(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "yoQwTFuMbcKq"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "gkI93G1pWhNo"
   },
   "outputs": [],
   "source": [
    "df=dataset.drop(columns=['aes','ffmc','dmc','dc','bui','isi','fwi','dsr','wmo'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "vgifFsLArHIW",
    "outputId": "6e656178-ca5b-4f19-e03f-8529f4d0b586"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        temp    td    rh    ws    wg  wdir    pres   vis  precip  rndays  sog  \\\n",
      "0        9.5   8.6  94.0   8.6  23.2   261  1007.7  24.5   20.52       0  0.0   \n",
      "1       10.2   6.2  76.0  35.8  45.7   252  1007.8  24.7   23.80       0  0.0   \n",
      "3       11.6   4.4  61.0  12.0  24.1   257  1007.0  39.8    6.20       0  0.0   \n",
      "4        9.2   6.9  85.0  45.0  54.0   259  1008.8  26.6   21.42       0  0.0   \n",
      "6       12.8   5.7  62.0  19.4  24.3   215  1007.4  28.2    6.00       0  0.0   \n",
      "...      ...   ...   ...   ...   ...   ...     ...   ...     ...     ...  ...   \n",
      "754605  16.9  12.4  75.0  21.7   NaN   219  1013.1  24.1    3.00       0  0.0   \n",
      "754606  20.6  13.9  66.0  29.1   NaN   239  1007.1  19.0    3.80       0  0.0   \n",
      "754608  21.6   9.7  46.0  35.3   NaN   219  1015.5  16.1    0.50       0  0.0   \n",
      "754609  18.3  12.0  66.0  31.0   NaN   291  1006.4  17.7    4.61       0  0.0   \n",
      "754611  12.1  11.4  96.0   7.6   NaN   250  1013.7   9.7   11.10       0  0.0   \n",
      "\n",
      "        Fire/Not Fire  \n",
      "0                 0.0  \n",
      "1                 0.0  \n",
      "3                 0.0  \n",
      "4                 0.0  \n",
      "6                 0.0  \n",
      "...               ...  \n",
      "754605            0.0  \n",
      "754606            0.0  \n",
      "754608            1.0  \n",
      "754609            0.0  \n",
      "754611            0.0  \n",
      "\n",
      "[331171 rows x 12 columns]\n"
     ]
    }
   ],
   "source": [
    "df.dropna(subset=[\"Fire/Not Fire\"],axis=0, inplace=True)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Fkcegr7NakgM",
    "outputId": "37deff72-97e2-4857-9836-0d1593a83c17"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "temp             331171\n",
       "td               331023\n",
       "rh               331128\n",
       "ws               331171\n",
       "wg               231642\n",
       "wdir             331171\n",
       "pres             331171\n",
       "vis              331171\n",
       "precip           331165\n",
       "rndays           331171\n",
       "sog              330813\n",
       "Fire/Not Fire    331171\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "yaaOfeGe0ihE"
   },
   "outputs": [],
   "source": [
    "x=df.iloc[:,:-1].values\n",
    "y=df.iloc[:,-1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lAluOXUL-FmC",
    "outputId": "506e6b78-7c03-48ce-d16f-1971dff56956"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "temp              -0.191087\n",
       "td                -0.319334\n",
       "rh                 0.063509\n",
       "ws                 1.304666\n",
       "wg                 1.100895\n",
       "wdir              -0.359293\n",
       "pres             -44.164837\n",
       "vis                2.122527\n",
       "precip             9.345478\n",
       "rndays            47.560751\n",
       "sog              281.729884\n",
       "Fire/Not Fire     -0.005236\n",
       "dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import skew\n",
    "df.skew(axis = 0, skipna = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "id": "aXxeIL4wGgZB"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "IterativeImputer()"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.experimental import enable_iterative_imputer # noqa\n",
    "# now you can import normally from sklearn.impute\n",
    "from sklearn.impute import IterativeImputer\n",
    "imp = IterativeImputer()\n",
    "# Fit to the dataset containing missing values\n",
    "imp.fit(x)\n",
    "# Transform the dataset containing missing values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9.5 ,  8.6 , 94.  , ..., 20.52,  0.  ,  0.  ],\n",
       "       [10.2 ,  6.2 , 76.  , ..., 23.8 ,  0.  ,  0.  ],\n",
       "       [11.6 ,  4.4 , 61.  , ...,  6.2 ,  0.  ,  0.  ],\n",
       "       ...,\n",
       "       [21.6 ,  9.7 , 46.  , ...,  0.5 ,  0.  ,  0.  ],\n",
       "       [18.3 , 12.  , 66.  , ...,  4.61,  0.  ,  0.  ],\n",
       "       [12.1 , 11.4 , 96.  , ..., 11.1 ,  0.  ,  0.  ]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "9qkyqeIHu5vs",
    "outputId": "88d4d4b0-3505-487e-d221-01408c9232fe"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "temp      331171\n",
       "td        331171\n",
       "rh        331171\n",
       "ws        331171\n",
       "wg        331171\n",
       "wdir      331171\n",
       "pres      331171\n",
       "vis       331171\n",
       "precip    331171\n",
       "rndays    331171\n",
       "sog       331171\n",
       "dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=pd.DataFrame(x,columns=[\"temp\",\"td\",\"rh\",\"ws\",\"wg\",\"wdir\",\"pres\",\"vis\",\"precip\",\"rndays\",\"sog\"])\n",
    "x.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "1bY147EZvBSa",
    "outputId": "d41b42a5-4fd3-48a3-d95b-42cced266caf"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        temp    td    rh    ws    wg   wdir    pres   vis  precip  rndays  sog\n",
      "0        9.5   8.6  94.0   8.6  23.2  261.0  1007.7  24.5   20.52     0.0  0.0\n",
      "1       10.2   6.2  76.0  35.8  45.7  252.0  1007.8  24.7   23.80     0.0  0.0\n",
      "2       11.6   4.4  61.0  12.0  24.1  257.0  1007.0  39.8    6.20     0.0  0.0\n",
      "3        9.2   6.9  85.0  45.0  54.0  259.0  1008.8  26.6   21.42     0.0  0.0\n",
      "4       12.8   5.7  62.0  19.4  24.3  215.0  1007.4  28.2    6.00     0.0  0.0\n",
      "...      ...   ...   ...   ...   ...    ...     ...   ...     ...     ...  ...\n",
      "331166  16.9  12.4  75.0  21.7  19.5  219.0  1013.1  24.1    3.00     0.0  0.0\n",
      "331167  20.6  13.9  66.0  29.1  19.5  239.0  1007.1  19.0    3.80     0.0  0.0\n",
      "331168  21.6   9.7  46.0  35.3  19.5  219.0  1015.5  16.1    0.50     0.0  0.0\n",
      "331169  18.3  12.0  66.0  31.0  19.5  291.0  1006.4  17.7    4.61     0.0  0.0\n",
      "331170  12.1  11.4  96.0   7.6  19.5  250.0  1013.7   9.7   11.10     0.0  0.0\n",
      "\n",
      "[331171 rows x 11 columns]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kVwuvNbkvGYY",
    "outputId": "7f37605e-868b-4ad2-d019-c14d0aaefaa2"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Fire/Not Fire    331171\n",
       "dtype: int64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y=pd.DataFrame(y,columns=[\"Fire/Not Fire\"])\n",
    "y.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "BDA96dcZveKw",
    "outputId": "547971c0-f45a-4abf-c661-fd62a541ff9f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        temp    td    rh    ws    wg   wdir    pres   vis  precip  rndays  \\\n",
      "0        9.5   8.6  94.0   8.6  23.2  261.0  1007.7  24.5   20.52     0.0   \n",
      "1       10.2   6.2  76.0  35.8  45.7  252.0  1007.8  24.7   23.80     0.0   \n",
      "2       11.6   4.4  61.0  12.0  24.1  257.0  1007.0  39.8    6.20     0.0   \n",
      "3        9.2   6.9  85.0  45.0  54.0  259.0  1008.8  26.6   21.42     0.0   \n",
      "4       12.8   5.7  62.0  19.4  24.3  215.0  1007.4  28.2    6.00     0.0   \n",
      "...      ...   ...   ...   ...   ...    ...     ...   ...     ...     ...   \n",
      "331166  16.9  12.4  75.0  21.7  19.5  219.0  1013.1  24.1    3.00     0.0   \n",
      "331167  20.6  13.9  66.0  29.1  19.5  239.0  1007.1  19.0    3.80     0.0   \n",
      "331168  21.6   9.7  46.0  35.3  19.5  219.0  1015.5  16.1    0.50     0.0   \n",
      "331169  18.3  12.0  66.0  31.0  19.5  291.0  1006.4  17.7    4.61     0.0   \n",
      "331170  12.1  11.4  96.0   7.6  19.5  250.0  1013.7   9.7   11.10     0.0   \n",
      "\n",
      "        sog  Fire/Not Fire  \n",
      "0       0.0            0.0  \n",
      "1       0.0            0.0  \n",
      "2       0.0            0.0  \n",
      "3       0.0            0.0  \n",
      "4       0.0            0.0  \n",
      "...     ...            ...  \n",
      "331166  0.0            0.0  \n",
      "331167  0.0            0.0  \n",
      "331168  0.0            1.0  \n",
      "331169  0.0            0.0  \n",
      "331170  0.0            0.0  \n",
      "\n",
      "[331171 rows x 12 columns]\n"
     ]
    }
   ],
   "source": [
    "df1 = pd.concat([x,y], axis=1)\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "E0I9VLuHEY36"
   },
   "source": [
    "Preprocessing of Data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gFfIgKzU4tfW",
    "outputId": "b4e0a461-014f-43ff-c19b-c0efabd7e4b4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        temp    td    rh    ws    wg   wdir    pres   vis  precip  rndays  sog\n",
      "0        9.5   8.6  94.0   8.6  23.2  261.0  1007.7  24.5   20.52     0.0  0.0\n",
      "1       10.2   6.2  76.0  35.8  45.7  252.0  1007.8  24.7   23.80     0.0  0.0\n",
      "2       11.6   4.4  61.0  12.0  24.1  257.0  1007.0  39.8    6.20     0.0  0.0\n",
      "3        9.2   6.9  85.0  45.0  54.0  259.0  1008.8  26.6   21.42     0.0  0.0\n",
      "4       12.8   5.7  62.0  19.4  24.3  215.0  1007.4  28.2    6.00     0.0  0.0\n",
      "...      ...   ...   ...   ...   ...    ...     ...   ...     ...     ...  ...\n",
      "331166  16.9  12.4  75.0  21.7  19.5  219.0  1013.1  24.1    3.00     0.0  0.0\n",
      "331167  20.6  13.9  66.0  29.1  19.5  239.0  1007.1  19.0    3.80     0.0  0.0\n",
      "331168  21.6   9.7  46.0  35.3  19.5  219.0  1015.5  16.1    0.50     0.0  0.0\n",
      "331169  18.3  12.0  66.0  31.0  19.5  291.0  1006.4  17.7    4.61     0.0  0.0\n",
      "331170  12.1  11.4  96.0   7.6  19.5  250.0  1013.7   9.7   11.10     0.0  0.0\n",
      "\n",
      "[331171 rows x 11 columns]\n",
      "        Fire/Not Fire\n",
      "0                 0.0\n",
      "1                 0.0\n",
      "2                 0.0\n",
      "3                 0.0\n",
      "4                 0.0\n",
      "...               ...\n",
      "331166            0.0\n",
      "331167            0.0\n",
      "331168            1.0\n",
      "331169            0.0\n",
      "331170            0.0\n",
      "\n",
      "[331171 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "print(x)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "oKdkoPVwhRbg"
   },
   "source": [
    "VISUALIZATION OF THE CLEAN DATA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 295
    },
    "id": "ujBYyWJDe0PB",
    "outputId": "38c0f19b-8e8a-4f34-9aa4-cff9e4d70ad4"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Fire/Not Fire',data=df)\n",
    "plt.xlabel('Fire Detection')\n",
    "plt.ylabel('Number of Observations')\n",
    "plt.title('Bar Chart for Fire Detection')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "NR7jSirioReW"
   },
   "source": [
    "PIE-CHART"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 273
    },
    "id": "f5JKhlprv4wc",
    "outputId": "6da9d93f-66bb-43df-b55a-782760996563"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "values=df1['Fire/Not Fire'].value_counts()\n",
    "labels=['Fire','No-Fire']\n",
    "plt.pie(values,labels=labels,radius = 1,explode = (0.1, 0),shadow=True,startangle=120,autopct='%1.1f%%') \n",
    "plt.title('Forest Fire Detection',fontsize=25)\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 447
    },
    "id": "5UQtss1WlXvK",
    "outputId": "a9e2b302-99cf-4dcc-b8ae-901dd6bd45d0"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16, 6))\n",
    "heatmap = sns.heatmap(dataset.corr(), vmin=-1, vmax=1, annot=False)\n",
    "heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':13}, pad=13)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "plLuIWVloJQq"
   },
   "source": [
    "Splitting dataset into training and test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "id": "U9Vc6wyDnNFf"
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "0Gi4bcthB_te",
    "outputId": "d92237a5-7317-4495-faab-c50586171813"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        temp    td    rh    ws    wg   wdir     pres   vis  precip  rndays  \\\n",
      "275185   9.6  -2.8  42.0  20.4  25.3  300.0  1017.50  19.7    0.37     0.0   \n",
      "47013   29.4  15.1  41.8   5.6   7.8  130.0  1017.70  20.9    0.00     2.0   \n",
      "27188   14.0   8.8  71.0   8.0  10.2   80.0  1007.70  30.5    1.00     0.0   \n",
      "323964  23.3  12.3  50.0   7.7  16.5  296.0  1014.70  21.2    0.00     2.0   \n",
      "258566  18.0  11.4  65.0  26.1  36.8  224.0  1029.50  32.2    0.00     5.0   \n",
      "...      ...   ...   ...   ...   ...    ...      ...   ...     ...     ...   \n",
      "122579   7.9   1.5  64.5  16.5  19.5  353.0  1014.14  21.5    0.29     0.0   \n",
      "304137  13.9  -3.6  30.0  14.1  19.5  176.0  1018.04  42.6    0.40     0.0   \n",
      "152315  15.2   0.4  36.7  13.0  19.6  330.0  1022.20  19.7    0.00     1.0   \n",
      "117952  21.0  19.0  88.4  31.5  50.0  220.0  1011.30  24.1   38.41     0.0   \n",
      "305711  13.4  -2.1  34.0  12.5  21.5  311.0  1012.10  23.8    2.60     0.0   \n",
      "\n",
      "        sog  \n",
      "275185  0.0  \n",
      "47013   0.0  \n",
      "27188   0.0  \n",
      "323964  0.0  \n",
      "258566  0.0  \n",
      "...     ...  \n",
      "122579  0.0  \n",
      "304137  0.0  \n",
      "152315  0.0  \n",
      "117952  0.0  \n",
      "305711  0.0  \n",
      "\n",
      "[248378 rows x 11 columns]\n",
      "        temp    td    rh    ws    wg   wdir    pres   vis  precip  rndays  sog\n",
      "6961    13.0   6.0  62.7  16.7  16.7  110.0  1017.4  48.3    0.96     0.0  0.0\n",
      "277319  10.1   4.5  68.0  25.6  19.5  304.0  1016.3  17.9    1.15     0.0  0.0\n",
      "66598   25.6  12.0  43.0   2.1   6.9  204.0  1014.3  32.7    0.00    13.0  0.0\n",
      "68484   24.3  12.4  48.0   4.8  10.7  116.0  1023.2  17.4    0.20     0.0  0.0\n",
      "146064  17.2   8.9  58.0  10.7  19.5  209.0   997.5  15.3    7.70     0.0  0.0\n",
      "...      ...   ...   ...   ...   ...    ...     ...   ...     ...     ...  ...\n",
      "192865  33.3  12.2  28.0  25.3  19.5  152.0  1014.6  21.1    0.00    10.0  0.0\n",
      "304263  13.0  -2.8  33.5  13.0  25.9  250.0  1021.6  19.8    0.00     3.0  0.0\n",
      "236757  18.0  10.0  59.7  13.0  13.0   40.0  1011.0  24.1    0.01     5.0  0.0\n",
      "46700   11.7  -3.6  34.0  10.5  16.9  267.0  1017.3  39.9    0.00     1.0  0.0\n",
      "233476  27.0  16.0  51.0   0.0   0.0    0.0  1015.5  24.1    0.00     1.0  0.0\n",
      "\n",
      "[82793 rows x 11 columns]\n",
      "        Fire/Not Fire\n",
      "275185            1.0\n",
      "47013             1.0\n",
      "27188             0.0\n",
      "323964            1.0\n",
      "258566            1.0\n",
      "...               ...\n",
      "122579            0.0\n",
      "304137            1.0\n",
      "152315            1.0\n",
      "117952            0.0\n",
      "305711            0.0\n",
      "\n",
      "[248378 rows x 1 columns]\n",
      "        Fire/Not Fire\n",
      "6961              0.0\n",
      "277319            0.0\n",
      "66598             1.0\n",
      "68484             1.0\n",
      "146064            0.0\n",
      "...               ...\n",
      "192865            1.0\n",
      "304263            1.0\n",
      "236757            1.0\n",
      "46700             0.0\n",
      "233476            0.0\n",
      "\n",
      "[82793 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "print(x_train)\n",
    "print(x_test)\n",
    "print(y_train)\n",
    "print(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "id": "chA8p-dgCe0F"
   },
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "sc=StandardScaler()\n",
    "x_train=sc.fit_transform(x_train)\n",
    "x_test=sc.transform(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PSsYYLquNeQ9"
   },
   "source": [
    "LASSO\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lxxpBF4oUEiN",
    "outputId": "afe156db-298d-4105-a678-44a452235d6e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.13934725455648522\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error\n",
    "lin_reg = LinearRegression()\n",
    "lin_reg.fit(x_train, y_train)\n",
    "lin_reg_y_pred = lin_reg.predict(x_test)\n",
    "mse = mean_squared_error(y_test, lin_reg_y_pred)\n",
    "print(mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "YjPs24pwUTDB",
    "outputId": "cb3b16c4-5b01-4b52-c65d-b7833c121869"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.15583395, -0.04326682, -0.18124525,  0.10709555, -0.02373431,\n",
       "        -0.01458532,  0.00350362, -0.00628201, -0.08407111,  0.0517345 ,\n",
       "        -0.00233667]])"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lin_reg.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "DrcZA04CAtku",
    "outputId": "9a06fe55-273c-4cd7-e8b7-060972fc5ae1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.2499963647739667\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import Lasso\n",
    "from sklearn.metrics import mean_squared_error\n",
    "lasso = Lasso()\n",
    "lasso.fit(x_train, y_train)\n",
    "y_pred_lasso = lasso.predict(x_test)\n",
    "mse = mean_squared_error(y_test, y_pred_lasso, squared=True)\n",
    "print(mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Jy7gOE-DMo3o",
    "outputId": "8f9d420f-62af-4a3a-81f0-fdeb5b063fc4"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0., -0., -0.,  0.,  0.,  0.,  0.,  0., -0.,  0., -0.])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lasso.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "VCUozsofDHUW",
    "outputId": "bcc4bf50-7128-45de-b16f-3b79fe127f03"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.13934725224292854\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import Ridge\n",
    "ridge = Ridge()\n",
    "ridge.fit(x_train, y_train)\n",
    "y_pred_ridge = ridge.predict(x_test)\n",
    "mse = mean_squared_error(y_test, y_pred_ridge,squared=True)\n",
    "print(mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "DHS2XuDGyOWH",
    "outputId": "4a2b4042-6902-4150-e9c5-5abcd4a5dc5b"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.15582913, -0.0432623 , -0.18124843,  0.1070943 , -0.02373324,\n",
       "        -0.0145852 ,  0.0035039 , -0.00628179, -0.08407087,  0.05173443,\n",
       "        -0.00233666]])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ridge.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 330
    },
    "id": "3voyF9QwQ9-k",
    "outputId": "833466ed-f31d-4354-ddfc-215c0892368e"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\AppData\\Local\\Temp/ipykernel_19736/3576512410.py:29: UserWarning: FixedFormatter should only be used together with FixedLocator\n",
      "  axes.set_xticklabels(['Lasso', 'Ridge'])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[Text(0, 0, 'Lasso'), Text(1, 0, 'Ridge'), Text(2, 0, '')]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2160x432 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(30,6))\n",
    "z = [ 'Lasso', 'linear','Ridge']\n",
    "y1 = np.array([-0.,0.15582913,0.15582913])\n",
    "y2 = np.array([0., -0.0432623,-0.0432623])\n",
    "y3 = np.array([0., -0.18124843,-0.18124843])\n",
    "y4 = np.array([0.,0.1070943,0.1070943])\n",
    "y5 = np.array([0., -0.02373324,-0.02373324])\n",
    "y6 = np.array([0.,-0.0145852,-0.0145852 ])\n",
    "y7 = np.array([0., 0.0035039,0.0035039])\n",
    "y8 = np.array([0.,-0.00628179,-0.00628179 ])\n",
    "y9 = np.array([0.,-0.08407087,-0.08407087 ])\n",
    "y10 = np.array([0.,0.05173443,0.05173443 ])\n",
    "y11 = np.array([0., -0.00233666, -0.00233666])\n",
    "fig, axes = plt.subplots(ncols=1, nrows=1)\n",
    "plt.bar(z, y1, color = 'black')\n",
    "plt.bar(z, y2, bottom=y1, color='b')\n",
    "plt.bar(z, y3, bottom=y1+y2, color='g')\n",
    "plt.bar(z, y4, bottom=y1+y2+y3, color='r')\n",
    "plt.bar(z, y5, bottom=y1+y2+y3+y4, color='magenta')\n",
    "plt.bar(z, y6, bottom=y1+y2+y3+y4+y5, color='brown')\n",
    "plt.bar(z, y7, bottom=y1+y2+y3+y4+y5+y6, color='cyan')\n",
    "plt.bar(z, y8, bottom=y1+y2+y3+y4+y5+y6+y7, color='yellow')\n",
    "plt.bar(z, y9, bottom=y1+y2+y3+y4+y5+y6+y7+y8, color='pink')\n",
    "plt.bar(z, y10, bottom=y1+y2+y3+y4+y5+y6+y7+y8+y9, color='grey')\n",
    "plt.bar(z, y11, bottom=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10, color='orange')\n",
    "plt.xlabel(\"Models\")\n",
    "plt.ylabel(\"Coefficients\")\n",
    "plt.title(\"Comparing coefficients of different models\")\n",
    "axes.set_xticklabels(['Lasso', 'Ridge'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "-k8BU79s07Bd",
    "outputId": "90f037ec-0945-4e8d-dfae-72ed4fb74450"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LassoCV(cv=5, max_iter=10000, random_state=0)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LassoCV\n",
    "\n",
    "# Lasso with 5 fold cross-validation\n",
    "model = LassoCV(cv=5, random_state=0, max_iter=10000)\n",
    "\n",
    "# Fit model\n",
    "model.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "PrGszL0z23Kr",
    "outputId": "bbeb3842-67a3-4067-d0ac-089a130f3c54"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0002921445739349054"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.alpha_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 488
    },
    "id": "I9rR_LL57iEY",
    "outputId": "afe68d5d-1bdd-4eeb-9344-0e110dcc724f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "training score: 0.0\n",
      "test score:  -3.710820178848273e-05\n",
      "number of features used:  0\n",
      "training score for alpha=0.01: 0.44538388870845913\n",
      "test score for alpha =0.01:  0.44259530732743924\n",
      "number of features used: for alpha =0.01: 11\n",
      "training score for alpha=0.00029214457393486354: 0.44483559703252407\n",
      "test score for alpha =0.0.00029214457393486354:  0.4422136622933458\n",
      "number of features used: for alpha =0.00029214457393486354: 10\n",
      "LR training score: 0.4453852556009684\n",
      "LR test score:  0.4425821927109982\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "lasso = Lasso()\n",
    "lasso.fit(x_train,y_train)\n",
    "train_score=lasso.score(x_train,y_train)\n",
    "test_score=lasso.score(x_test,y_test)\n",
    "coeff_used = np.sum(lasso.coef_!=0)\n",
    "print (\"training score:\", train_score)\n",
    "print (\"test score: \", test_score)\n",
    "print (\"number of features used: \", coeff_used)\n",
    "lasso001 = Lasso(alpha=0.0001, max_iter=10e5)\n",
    "lasso001.fit(x_train,y_train)\n",
    "train_score001=lasso001.score(x_train,y_train)\n",
    "test_score001=lasso001.score(x_test,y_test)\n",
    "coeff_used001 = np.sum(lasso001.coef_!=0)\n",
    "print( \"training score for alpha=0.01:\", train_score001 )\n",
    "print (\"test score for alpha =0.01: \", test_score001)\n",
    "print (\"number of features used: for alpha =0.01:\", coeff_used001)\n",
    "lasso2 = Lasso(alpha=0.002, max_iter=10e5)\n",
    "lasso2.fit(x_train,y_train)\n",
    "train_score2=lasso2.score(x_train,y_train)\n",
    "test_score2=lasso2.score(x_test,y_test)\n",
    "coeff_used02 = np.sum(lasso2.coef_!=0)\n",
    "print (\"training score for alpha=0.00029214457393486354:\", train_score2 )\n",
    "print (\"test score for alpha =0.0.00029214457393486354: \", test_score2)\n",
    "print (\"number of features used: for alpha =0.00029214457393486354:\", coeff_used02)\n",
    "lr = LinearRegression()\n",
    "lr.fit(x_train,y_train)\n",
    "lr_train_score=lr.score(x_train,y_train)\n",
    "lr_test_score=lr.score(x_test,y_test)\n",
    "print( \"LR training score:\", lr_train_score )\n",
    "print( \"LR test score: \", lr_test_score)\n",
    "plt.subplot(1,2,1)\n",
    "plt.plot(lasso.coef_,alpha=0.7,linestyle='none',marker='*',markersize=5,color='red',label=r'Lasso; $\\alpha = 1$',zorder=7) # alpha here is for transparency\n",
    "plt.plot(lasso001.coef_,alpha=0.5,linestyle='none',marker='d',markersize=6,color='blue',label=r'Lasso; $\\alpha = 0.01$') # alpha here is for transparency\n",
    "\n",
    "plt.xlabel('Coefficient Index',fontsize=16)\n",
    "plt.ylabel('Coefficient Magnitude',fontsize=16)\n",
    "plt.legend(fontsize=13,loc=4)\n",
    "plt.subplot(1,2,2)\n",
    "plt.plot(lasso.coef_,alpha=0.7,linestyle='none',marker='*',markersize=5,color='red',label=r'Lasso; $\\alpha = 1$',zorder=7) # alpha here is for transparency\n",
    "plt.plot(lasso001.coef_,alpha=0.5,linestyle='none',marker='d',markersize=6,color='blue',label=r'Lasso; $\\alpha = 0.0001$') # alpha here is for transparency\n",
    "plt.plot(lasso2.coef_,alpha=0.8,linestyle='none',marker='v',markersize=6,color='black',label=r'Lasso; $\\alpha = 0.00029214457393486354$') # alpha here is for transparency\n",
    "plt.plot(lr.coef_,alpha=0.7,linestyle='none',marker='o',markersize=5,color='green',label='Linear Regression',zorder=2)\n",
    "plt.xlabel('Coefficient Index',fontsize=16)\n",
    "plt.ylabel('Coefficient Magnitude',fontsize=16)\n",
    "plt.legend(fontsize=13,loc=4)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CRparTzqJch8"
   },
   "source": [
    "PCA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kPGc5XhpE38K",
    "outputId": "5880c842-bdbf-4839-dc10-a90b8055663f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.17681773, 0.16136824, 0.13840814, 0.09245174, 0.09090023,\n",
       "       0.08867356, 0.08504576, 0.07783968, 0.06649326])"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.decomposition import PCA\n",
    "pca=PCA(n_components=9)\n",
    "x_train=pca.fit_transform(x_train)\n",
    "x_test=pca.transform(x_test)\n",
    "pca.explained_variance_ratio_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "_TZRrYQqGWit",
    "outputId": "135674c2-fbdb-4fd1-c2ae-0d5a3f73f99f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.17681773, 0.33818597, 0.47659411, 0.56904585, 0.65994608,\n",
       "       0.74861963, 0.83366539, 0.91150507, 0.97799833])"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cumsum(pca.explained_variance_ratio_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 295
    },
    "id": "0VXaxPChKKJb",
    "outputId": "509331b5-981c-46e4-906a-50aa4485fbf7"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pca=PCA().fit(x_train)\n",
    "x=np.arange(1,10,step=1)\n",
    "y = np.cumsum(pca.explained_variance_ratio_)\n",
    "plt.plot(x,y,linestyle=\"--\",marker=\"o\",color=\"blue\")\n",
    "plt.grid()\n",
    "plt.axhline(y=0.95,linestyle='dashdot',color=\"red\")\n",
    "plt.xlabel(\"Number of components\")\n",
    "plt.ylabel(\"Cumulative Variance Explained\")\n",
    "plt.title(\"The optimal number of components to explain a specified variance\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "i8bkYi5DbVdW"
   },
   "source": [
    "LOGISTIC REGRESSION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "j5ojsmAhFavy",
    "outputId": "f55dc73c-ba97-4dfd-818f-58891e22badd"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "classifier=LogisticRegression()\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "UtEUG8H8FX0V",
    "outputId": "ddbb4c3d-96b1-4834-91c4-a351de1c8d5e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[34221  6878]\n",
      " [ 5618 36076]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.8490693657676374"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred=classifier.predict(x_test)\n",
    "cm_lg=confusion_matrix(y_test,y_pred)\n",
    "print(cm_lg)\n",
    "accuracy_score(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "3k7BMtW-Ygim"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "id": "NKOZcHJ3VzUV"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 84.91 %\n",
      "Standard Deviation: 0.15 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qLNv2mUfdZAZ"
   },
   "source": [
    "K nearest neighbours"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "KfO20IMvJpIg"
   },
   "source": [
    "ELbow method "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "id": "f86Gs9laMMeJ"
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Expected 2D array, got 1D array instead:\narray=[1. 2. 3. 4. 5. 6. 7. 8. 9.].\nReshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_19736/3295469306.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m   \u001b[0mkmeans\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mKMeans\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn_clusters\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0minit\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'k-means++'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mrandom_state\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m42\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m   \u001b[0mkmeans\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m   \u001b[0mWCSS\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mKMeans\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minertia_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mWCSS\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\cluster\\_kmeans.py\u001b[0m in \u001b[0;36mfit\u001b[1;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[0;32m    977\u001b[0m             \u001b[0mFitted\u001b[0m \u001b[0mestimator\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    978\u001b[0m         \"\"\"\n\u001b[1;32m--> 979\u001b[1;33m         X = self._validate_data(X, accept_sparse='csr',\n\u001b[0m\u001b[0;32m    980\u001b[0m                                 \u001b[0mdtype\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfloat64\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfloat32\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    981\u001b[0m                                 \u001b[0morder\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'C'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcopy\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcopy_x\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\base.py\u001b[0m in \u001b[0;36m_validate_data\u001b[1;34m(self, X, y, reset, validate_separately, **check_params)\u001b[0m\n\u001b[0;32m    419\u001b[0m             \u001b[0mout\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mX\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    420\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0my\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'no_validation'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 421\u001b[1;33m             \u001b[0mX\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcheck_array\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcheck_params\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    422\u001b[0m             \u001b[0mout\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mX\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    423\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36minner_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     61\u001b[0m             \u001b[0mextra_args\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m-\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mall_args\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     62\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mextra_args\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 63\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     64\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     65\u001b[0m             \u001b[1;31m# extra_args > 0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36mcheck_array\u001b[1;34m(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator)\u001b[0m\n\u001b[0;32m    692\u001b[0m             \u001b[1;31m# If input is 1D raise error\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    693\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0marray\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 694\u001b[1;33m                 raise ValueError(\n\u001b[0m\u001b[0;32m    695\u001b[0m                     \u001b[1;34m\"Expected 2D array, got 1D array instead:\\narray={}.\\n\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    696\u001b[0m                     \u001b[1;34m\"Reshape your data either using array.reshape(-1, 1) if \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Expected 2D array, got 1D array instead:\narray=[1. 2. 3. 4. 5. 6. 7. 8. 9.].\nReshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample."
     ]
    }
   ],
   "source": [
    "from sklearn.cluster import KMeans\n",
    "WCSS=[]\n",
    "for i in range(1,20):\n",
    "  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)\n",
    "  kmeans.fit(x)\n",
    "  WCSS.append(KMeans.inertia_)\n",
    "plt.plot(range(1,20),WCSS)\n",
    "plt.title(\"the elbow method\")\n",
    "plt.xlabel(\"number of clusters\")\n",
    "plt.ylabel(\"WCSS\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "hhLiYps0dbay",
    "outputId": "e316030d-3f40-4c01-a924-cfd1e41f8996"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\neighbors\\_classification.py:179: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  return self._fit(X, y)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "peaP4XBDc7Vb",
    "outputId": "4ed312ee-2b24-4c24-a818-aebd350b617a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[34515  6584]\n",
      " [ 6526 35168]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.8416532798666554"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred1=classifier.predict(x_test)\n",
    "cm_KN=confusion_matrix(y_test,y_pred1)\n",
    "print(cm_KN)\n",
    "accuracy_score(y_test,y_pred1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "id": "yMq7K5wsVgQS"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 63.50 %\n",
      "Standard Deviation: 1.19 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OsqpkUtuekmF"
   },
   "source": [
    "Naive Bayes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "9e_kiuqNefJy",
    "outputId": "c8d06389-7fc4-45b5-9cb4-5285e87bd7bd"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "GaussianNB()"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "classifier=GaussianNB()\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "27i8K7NteXUn",
    "outputId": "a6015662-028d-48f1-9d1a-e5e16131f031"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[12159 28940]\n",
      " [ 1099 40595]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.6371794716944669"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred2=classifier.predict(x_test)\n",
    "cm_NB=confusion_matrix(y_test,y_pred2)\n",
    "print(cm_NB)\n",
    "accuracy_score(y_test,y_pred2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "id": "DjKBL5KYViW-"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 63.50 %\n",
      "Standard Deviation: 1.19 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "llILiQi4fApX"
   },
   "source": [
    "Decision Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "8wWqcjT7fEXk",
    "outputId": "0a640027-a00c-432f-fdea-70c67c70259f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(criterion='entropy', random_state=0)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "d8JM2YbBfXWT",
    "outputId": "65d24d38-87a7-4087-a56f-2a5290fd9287"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[32890  8209]\n",
      " [ 8010 33684]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.8041017960455594"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred3=classifier.predict(x_test)\n",
    "cm_DT=confusion_matrix(y_test,y_pred3)\n",
    "print(cm_DT)\n",
    "accuracy_score(y_test,y_pred3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "id": "wxHYeasyVjmH"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 80.46 %\n",
      "Standard Deviation: 0.20 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0ItiJGlziQaR"
   },
   "source": [
    "**Random Forest Classifier**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "GRhrCrvxfmkY",
    "outputId": "075aa991-d457-47ea-f378-85f7a63456bb"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\AppData\\Local\\Temp/ipykernel_19736/415059052.py:3: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  classifier.fit(x_train,y_train)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=0)"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "classifier=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Q53KgV0wf86F",
    "outputId": "1726e9fa-66a9-44dd-d1e4-1fd5ec8df282"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[35953  5146]\n",
      " [ 7544 34150]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0.8467261725025063"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred4=classifier.predict(x_test)\n",
    "cm_RF=confusion_matrix(y_test,y_pred4)\n",
    "print(cm_RF)\n",
    "accuracy_score(y_test,y_pred4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "id": "QvJA_TjRVlDe"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n",
      "C:\\Users\\tripa\\anaconda3\\lib\\site-packages\\sklearn\\model_selection\\_validation.py:598: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  estimator.fit(X_train, y_train, **fit_params)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 84.60 %\n",
      "Standard Deviation: 0.19 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DVlgvUkFfhV8"
   },
   "source": [
    "**SVM Classifier**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "C5wmGNQLhpE3"
   },
   "source": [
    "from sklearn.svm import SVC\n",
    "classifier=SVC(kernel='rbf',random_state=0)\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qcDTw3WqgY7-"
   },
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred5=classifier.predict(x_test)\n",
    "cm_svm=confusion_matrix(y_test,y_pred5)\n",
    "print(cm_svm)\n",
    "accuracy_score(y_test,y_pred5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q9PPunMsNf9K"
   },
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "accuracies = cross_val_score(estimator = classifier, X= x_train, y= y_train, cv = 10)\n",
    "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
    "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "XGBOOST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from xgboost import XGBClassifier\n",
    "classifier= XGBClassifier()\n",
    "classifier.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix ,accuracy_score\n",
    "y_pred5=classifier.predict(x_test)\n",
    "cm_xg=confusion_matrix(y_test,y_pred5)\n",
    "print(cm_xg)\n",
    "accuracy_score(y_test,y_pred5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
