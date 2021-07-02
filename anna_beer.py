{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Homework 6, Part One: Lots and lots of questions about beer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Do your importing and your setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read in the file `craftcans.csv`, and look at the first first rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.50%</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maggie's Leap</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.90%</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.80%</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Pumpion</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>38.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Stronghold</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American Porter</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Beer            Brewery         Location               Style  \\\n",
       "0   Get Together  NorthGate Brewing  Minneapolis, MN        American IPA   \n",
       "1  Maggie's Leap  NorthGate Brewing  Minneapolis, MN  Milk / Sweet Stout   \n",
       "2     Wall's End  NorthGate Brewing  Minneapolis, MN   English Brown Ale   \n",
       "3        Pumpion  NorthGate Brewing  Minneapolis, MN         Pumpkin Ale   \n",
       "4     Stronghold  NorthGate Brewing  Minneapolis, MN     American Porter   \n",
       "\n",
       "     Size    ABV  IBUs  \n",
       "0  16 oz.  4.50%  50.0  \n",
       "1  16 oz.  4.90%  26.0  \n",
       "2  16 oz.  4.80%  19.0  \n",
       "3  16 oz.  6.00%  38.0  \n",
       "4  16 oz.  6.00%  25.0  "
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "#!head -n5\n",
    "df = pd.read_csv(\"/home/abstech151/assignments/homework6/beer/craftcans.csv\", na_values=[\"???\", \"Does not apply\"])\n",
    "df.head(5)\n",
    "\n",
    "#df = pd.read_csv(\"beer/craftcans.csv\", na_values=[\"???\", \"Does not apply\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How many rows do you have in the data? What are the column types?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2416, 7)"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Beer', 'Brewery', 'Location', 'Style', 'Size', 'ABV', 'IBUs'], dtype='object')"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Beer         object\n",
       "Brewery      object\n",
       "Location     object\n",
       "Style        object\n",
       "Size         object\n",
       "ABV          object\n",
       "IBUs        float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 producers of cans of beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Brewery Vivant                62\n",
       "Oskar Blues Brewery           46\n",
       "Sun King Brewing Company      38\n",
       "Cigar City Brewing Company    25\n",
       "Sixpoint Craft Ales           24\n",
       "Hopworks Urban Brewery        23\n",
       "Stevens Point Brewery         22\n",
       "21st Amendment Brewery        20\n",
       "Great Crescent Brewery        20\n",
       "SanTan Brewing Company        19\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Brewery.value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is the most common ABV? (alcohol by volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.00%    215\n",
       "Name: ABV, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.value_counts().head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Oh, weird, ABV isn't a number. Convert it to a number for me, please.\n",
    "\n",
    "It's going to take a few steps!\n",
    "\n",
    "### First, let's just look at the ABV column by itself"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       4.50%\n",
      "1       4.90%\n",
      "2       4.80%\n",
      "3       6.00%\n",
      "4       6.00%\n",
      "        ...  \n",
      "2411    5.30%\n",
      "2412    9.90%\n",
      "2413    8.00%\n",
      "2414    8.70%\n",
      "2415    6.50%\n",
      "Name: ABV, Length: 2416, dtype: object\n"
     ]
    }
   ],
   "source": [
    "ABV=df.ABV\n",
    "print(ABV)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hm, `%` isn't part of  a number. Let's remove it.\n",
    "\n",
    "When you're confident you got it right, save the results back into the `ABV` column.\n",
    "\n",
    "- *Tip: In programming the easiest way to remove something is to *replacing it with nothing*.\n",
    "- *Tip: \"nothing\" might seem like `NaN` sinc we talked about it a lot in class, but in this case it isn't! It's just an empty string, like \"\"*\n",
    "- *Tip: `.replace` is used for replacing ENTIRE cells, while `.str.replace` is useful for replacing PARTS of cells (see my New York example)*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       True\n",
       "1       True\n",
       "2       True\n",
       "3       True\n",
       "4       True\n",
       "        ... \n",
       "2411    True\n",
       "2412    True\n",
       "2413    True\n",
       "2414    True\n",
       "2415    True\n",
       "Name: ABV, Length: 2416, dtype: object"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ABV.str.contains(\"%\", case=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.ABV=(df['ABV'].str[:-1].astype(float))\n",
    "#(df['returns'].str[:-1].astype(float))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2416, 7)"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maggie's Leap</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Pumpion</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>38.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Stronghold</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American Porter</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Beer            Brewery         Location               Style  \\\n",
       "0   Get Together  NorthGate Brewing  Minneapolis, MN        American IPA   \n",
       "1  Maggie's Leap  NorthGate Brewing  Minneapolis, MN  Milk / Sweet Stout   \n",
       "2     Wall's End  NorthGate Brewing  Minneapolis, MN   English Brown Ale   \n",
       "3        Pumpion  NorthGate Brewing  Minneapolis, MN         Pumpkin Ale   \n",
       "4     Stronghold  NorthGate Brewing  Minneapolis, MN     American Porter   \n",
       "\n",
       "     Size  ABV  IBUs  \n",
       "0  16 oz.  4.5  50.0  \n",
       "1  16 oz.  4.9  26.0  \n",
       "2  16 oz.  4.8  19.0  \n",
       "3  16 oz.  6.0  38.0  \n",
       "4  16 oz.  6.0  25.0  "
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now let's turn `ABV` into a numeric data type\n",
    "\n",
    "Save the results back into the `ABV` column (again), and then check `df.dtypes` to make sure it worked.\n",
    "\n",
    "- *Tip: We used `.astype(int)` during class, but this has a decimal in it...*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Beer         object\n",
       "Brewery      object\n",
       "Location     object\n",
       "Style        object\n",
       "Size         object\n",
       "ABV         float64\n",
       "IBUs        float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes\n",
    "#df.ABV.astype(float)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What's the ABV of the average beer look like?\n",
    "\n",
    "### Show me in two different ways: one command to show the `median`/`mean`/etc, and secondly show me a chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    2348.000000\n",
       "mean        5.977342\n",
       "std         1.354173\n",
       "min         0.100000\n",
       "25%         5.000000\n",
       "50%         5.600000\n",
       "75%         6.700000\n",
       "max        12.800000\n",
       "Name: ABV, dtype: float64"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.6"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
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
    "df.ABV.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We don't have ABV for all of the beers, how many are we missing them from?\n",
    "\n",
    "- *Tip: You can use `isnull()` or `notnull()` to see where a column is missing data.*\n",
    "- *Tip: You just want to count how many `True`s and `False`s there are.*\n",
    "- *Tip: It's a weird trick involving something we usually use to count things in a column*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "68"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.isnull().sum()\n",
    "#df.ABV.notnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Looking at location\n",
    "\n",
    "Brooklyn used to produce 80% of the country's beer! Let's see if it's still true."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Brooklyn, NY    38\n",
       "Name: Location, dtype: int64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Location.str.contains(\"Brooklyn, NY\", na=False)].Location.value_counts()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 cities in the US for canned craft beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Grand Rapids, MI    66\n",
       "Chicago, IL         55\n",
       "Portland, OR        52\n",
       "Indianapolis, IN    43\n",
       "San Diego, CA       42\n",
       "Boulder, CO         41\n",
       "Denver, CO          40\n",
       "Brooklyn, NY        38\n",
       "Seattle, WA         35\n",
       "Longmont, CO        33\n",
       "Name: Location, dtype: int64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Location.value_counts().head(10)\n",
    "#df.sort_values(by='Location', ascending=True).head(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beer from Brooklyn, NY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "115                              4Beans\n",
      "210                              Jammer\n",
      "246                             Abigale\n",
      "404                       Nomader Weiss\n",
      "421                                 Rad\n",
      "439                        Molotov Lite\n",
      "588                             Bengali\n",
      "713                       Sensi Harvest\n",
      "969                              Hi-Res\n",
      "987               KelSo Nut Brown Lager\n",
      "1057                      Global Warmer\n",
      "1074                 Autumnation (2013)\n",
      "1093               KelSo India Pale Ale\n",
      "1267                          The Crisp\n",
      "1268                       Sweet Action\n",
      "1269                      Righteous Ale\n",
      "1270                      Bengali Tiger\n",
      "1305                      KelSo Pilsner\n",
      "1365    Hipster Ale (Two Roads Brewing)\n",
      "1366                        Bikini Beer\n",
      "1373                East India Pale Ale\n",
      "1624                             3Beans\n",
      "1836                         Brownstone\n",
      "1857                Brooklyn Summer Ale\n",
      "1962    Hipster Ale (Westbrook Brewing)\n",
      "1970                             Apollo\n",
      "1971                          Harbinger\n",
      "1972                              Resin\n",
      "2027                East India Pale Ale\n",
      "2062                             Diesel\n",
      "2074       Autumnation (2011-12) (2011)\n",
      "2140                   The Crisp (2011)\n",
      "2141                Sweet Action (2011)\n",
      "2142               Righteous Ale (2011)\n",
      "2143               Bengali Tiger (2011)\n",
      "2219         Brooklyn Summer Ale (2011)\n",
      "2350            Brooklyn Lager (16 oz.)\n",
      "2351            Brooklyn Lager (12 oz.)\n",
      "Name: Beer, dtype: object\n"
     ]
    }
   ],
   "source": [
    "df.Brooklyn = df[(df.Location.str.contains(\"Brooklyn, NY\", na=False))]\n",
    "#df.Brooklyn.describe\n",
    "print(df.Brooklyn['Beer']) \n",
    "#df[df['Location']=='Brooklyn, NY']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What brewery in Brooklyn puts out the most cans of beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sixpoint Craft Ales    24\n",
       "Brooklyn Brewery        6\n",
       "Evil Twin Brewing       5\n",
       "KelSo Beer Company      3\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df.most_cans]].sort_values(by='Brewery', ascending=False)\n",
    "#df.Brooklyn.sort_values(by='Brewery', ascending=False).head(1)\n",
    "df[df['Location']=='Brooklyn, NY']['Brewery'].value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the five most popular styles of beer produced by Sixpoint?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      4\n",
       "Baltic Porter                     2\n",
       "Rye Beer                          2\n",
       "American Double / Imperial IPA    2\n",
       "Cream Ale                         2\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "is_Sixpoint = df.Brooklyn[df.Brooklyn['Brewery']=='Sixpoint Craft Ales']\n",
    "is_Sixpoint.sort_values(by='Style', ascending=False)\n",
    "is_Sixpoint.Style.value_counts().head(5)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the breweries in New York state.\n",
    "\n",
    "- *Tip: We want to match *part* of the `Location` column, but not all of it.*\n",
    "- *Tip: Watch out for `NaN` values! You might be close, but you'll need to pass an extra parameter to make it work without an error.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Sixpoint Craft Ales', 'Matt Brewing Company', 'Brooklyn Brewery',\n",
       "       'Evil Twin Brewing', 'Butternuts Beer and Ale',\n",
       "       'Blue Point Brewing Company', 'The Bronx Brewery', 'KelSo Beer Company',\n",
       "       'Montauk Brewing Company', 'Upstate Brewing Company', 'Chatham Brewing',\n",
       "       'Bomb Beer Company', 'Southampton Publick House',\n",
       "       'The Manhattan Brewing Company', 'Dundee Brewing Company',\n",
       "       'Newburgh Brewing Company'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_NY = df[df.Location.str.contains(\"NY\", na=False)]\n",
    "\n",
    "df_NY.Brewery.value_counts().index\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now *count* all of the breweries in New York state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df_NY.Brewery.value_counts()\n",
    "len(df_NY.Brewery.value_counts())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Measuring International Bitterness Units\n",
    "\n",
    "## Display all of the IPAs\n",
    "\n",
    "Include American IPAs, Imperial IPAs, and anything else with \"IPA in it.\"\n",
    "\n",
    "IPA stands for [India Pale Ale](https://www.bonappetit.com/story/ipa-beer-styles), and is probably the most popular kind of beer in the US for people who are drinking [craft beer](https://www.craftbeer.com/beer/what-is-craft-beer)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Citra Ass Down</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Rico Sauvin</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.6</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Pile of Face</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Habitus (2014)</td>\n",
       "      <td>Mike Hess Brewing Company</td>\n",
       "      <td>San Diego, CA</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Solis</td>\n",
       "      <td>Mike Hess Brewing Company</td>\n",
       "      <td>San Diego, CA</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.5</td>\n",
       "      <td>85.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Habitus</td>\n",
       "      <td>Mike Hess Brewing Company</td>\n",
       "      <td>San Diego, CA</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Beer                    Brewery         Location  \\\n",
       "0     Get Together          NorthGate Brewing  Minneapolis, MN   \n",
       "6   Citra Ass Down  Against the Grain Brewery   Louisville, KY   \n",
       "14     Rico Sauvin  Against the Grain Brewery   Louisville, KY   \n",
       "17    Pile of Face  Against the Grain Brewery   Louisville, KY   \n",
       "24  Habitus (2014)  Mike Hess Brewing Company    San Diego, CA   \n",
       "25           Solis  Mike Hess Brewing Company    San Diego, CA   \n",
       "27         Habitus  Mike Hess Brewing Company    San Diego, CA   \n",
       "\n",
       "                             Style    Size  ABV   IBUs  \n",
       "0                     American IPA  16 oz.  4.5   50.0  \n",
       "6   American Double / Imperial IPA  16 oz.  8.0   68.0  \n",
       "14  American Double / Imperial IPA  16 oz.  7.6   68.0  \n",
       "17                    American IPA  16 oz.  6.0   65.0  \n",
       "24  American Double / Imperial IPA  16 oz.  8.0  100.0  \n",
       "25                    American IPA  16 oz.  7.5   85.0  \n",
       "27  American Double / Imperial IPA  16 oz.  8.0  100.0  "
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Style.str.contains('IPA', na=False)].head(7)\n",
    "#df_IPA = df[df.Style.str.contains(\"IPA\")]\n",
    "#df.Style.str.contains('IPA').head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "IPAs are usually pretty hoppy and bitter. IBU stands for [International Bitterness Unit](http://www.thebrewenthusiast.com/ibus/), and while a lot of places like to brag about having the most bitter beer (it's an American thing!), IBUs don't necessary *mean anything*.\n",
    "\n",
    "Let's look at how different beers have different IBU measurements."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Try to get the average IBU measurement across all beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42.71316725978647"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.mean()\n",
    "#df.IBUs.value_counts()\n",
    "#lots of missing values, go back up to top and do na\n",
    "#df.IBUs.astype(int)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Oh no, it doesn't work!\n",
    "\n",
    "It looks like some of those values *aren't numbers*. There are two ways to fix this:\n",
    "\n",
    "1. Do the `.replace` and `np.nan` thing we did in class. Then convert the column to a number. This is boring.\n",
    "2. When you're reading in your csv, there [is an option called `na_values`](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.read_csv.html). You can give it a list of **numbers or strings to count as `NaN`**. It's a lot easier than doing the `np.nan` thing, although you'll need to go add it up top and run all of your cells again.\n",
    "\n",
    "- *Tip: Make sure you're giving `na_values` a LIST, not just a string*\n",
    "\n",
    "### Now try to get the average IBUs again"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42.71316725978647"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#import numpy as np\n",
    "#df.IBU = df.IBUs.replace('Does not apply', np.nan)\n",
    "df.IBUs.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.0     82\n",
       "35.0     60\n",
       "65.0     54\n",
       "30.0     53\n",
       "70.0     48\n",
       "         ..\n",
       "97.0      1\n",
       "91.0      1\n",
       "130.0     1\n",
       "118.0     1\n",
       "89.0      1\n",
       "Name: IBUs, Length: 107, dtype: int64"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.dtypes\n",
    "df.IBUs.value_counts()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Draw the distribution of IBU measurements, but with *twenty* bins instead of the default of 10\n",
    "\n",
    "- *Tip: Every time I ask for a distribution, I'm looking for a histogram*\n",
    "- *Tip: Use the `?` to get all of the options for building a histogram*\n",
    "- *Tip: Make sure your `matplotlib` thing is set up right!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
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
    "df.IBUs.hist(bins=20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hm, Interesting distribution. List all of the beers with IBUs above the 75th percentile\n",
    "\n",
    "- *Tip: There's a single that gives you the 25/50/75th percentile*\n",
    "- *Tip: You can just manually type the number when you list those beers*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    1405.000000\n",
       "mean       42.713167\n",
       "std        25.954066\n",
       "min         4.000000\n",
       "25%        21.000000\n",
       "50%        35.000000\n",
       "75%        64.000000\n",
       "max       138.000000\n",
       "Name: IBUs, dtype: float64"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Citra Ass Down</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>London Balling</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>English Barleywine</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>12.5</td>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Rico Sauvin</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.6</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Pile of Face</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Excess IPL</td>\n",
       "      <td>Jack's Abby Craft Lagers</td>\n",
       "      <td>Framingham, MA</td>\n",
       "      <td>American India Pale Lager</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.2</td>\n",
       "      <td>80.0</td>\n",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2408</th>\n",
       "      <td>Brew Free! or Die IPA</td>\n",
       "      <td>21st Amendment Brewery</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>7.0</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2410</th>\n",
       "      <td>Ten Fidy Imperial Stout</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Russian Imperial Stout</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>98.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.7</td>\n",
       "      <td>85.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2415</th>\n",
       "      <td>Dale's Pale Ale</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.5</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>346 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Beer                    Brewery           Location  \\\n",
       "6              Citra Ass Down  Against the Grain Brewery     Louisville, KY   \n",
       "7              London Balling  Against the Grain Brewery     Louisville, KY   \n",
       "14                Rico Sauvin  Against the Grain Brewery     Louisville, KY   \n",
       "17               Pile of Face  Against the Grain Brewery     Louisville, KY   \n",
       "21                 Excess IPL   Jack's Abby Craft Lagers     Framingham, MA   \n",
       "...                       ...                        ...                ...   \n",
       "2408    Brew Free! or Die IPA     21st Amendment Brewery  San Francisco, CA   \n",
       "2410  Ten Fidy Imperial Stout        Oskar Blues Brewery       Longmont, CO   \n",
       "2412       GUBNA Imperial IPA        Oskar Blues Brewery       Longmont, CO   \n",
       "2414        Gordon Ale (2009)        Oskar Blues Brewery       Longmont, CO   \n",
       "2415          Dale's Pale Ale        Oskar Blues Brewery       Longmont, CO   \n",
       "\n",
       "                               Style    Size   ABV   IBUs  \n",
       "6     American Double / Imperial IPA  16 oz.   8.0   68.0  \n",
       "7                 English Barleywine  16 oz.  12.5   80.0  \n",
       "14    American Double / Imperial IPA  16 oz.   7.6   68.0  \n",
       "17                      American IPA  16 oz.   6.0   65.0  \n",
       "21         American India Pale Lager  16 oz.   7.2   80.0  \n",
       "...                              ...     ...   ...    ...  \n",
       "2408                    American IPA  12 oz.   7.0   65.0  \n",
       "2410          Russian Imperial Stout  12 oz.   9.9   98.0  \n",
       "2412  American Double / Imperial IPA  12 oz.   9.9  100.0  \n",
       "2414  American Double / Imperial IPA  12 oz.   8.7   85.0  \n",
       "2415         American Pale Ale (APA)  12 oz.   6.5   65.0  \n",
       "\n",
       "[346 rows x 7 columns]"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.IBUs>64]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beers with IBUs below the 25th percentile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Sho'nuff</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>Belgian Pale Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.0</td>\n",
       "      <td>13.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Bloody Show</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Pilsner</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>17.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>The Brown Note</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.0</td>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>House Lager</td>\n",
       "      <td>Jack's Abby Craft Lagers</td>\n",
       "      <td>Framingham, MA</td>\n",
       "      <td>Keller Bier / Zwickel Bier</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>18.0</td>\n",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2372</th>\n",
       "      <td>Bombshell Blonde</td>\n",
       "      <td>Southern Star Brewing Company</td>\n",
       "      <td>Conroe, TX</td>\n",
       "      <td>American Blonde Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.0</td>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2385</th>\n",
       "      <td>Bikini Blonde Lager</td>\n",
       "      <td>Maui Brewing Company</td>\n",
       "      <td>Lahaina, HI</td>\n",
       "      <td>Munich Helles Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2396</th>\n",
       "      <td>Royal Weisse Ale</td>\n",
       "      <td>Sly Fox Brewing Company</td>\n",
       "      <td>Pottstown, PA</td>\n",
       "      <td>Hefeweizen</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.6</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2404</th>\n",
       "      <td>Hell</td>\n",
       "      <td>Surly Brewing Company</td>\n",
       "      <td>Brooklyn Center, MN</td>\n",
       "      <td>Keller Bier / Zwickel Bier</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.1</td>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2409</th>\n",
       "      <td>Hell or High Watermelon Wheat</td>\n",
       "      <td>21st Amendment Brewery</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>Fruit / Vegetable Beer</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>17.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>338 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                               Beer                        Brewery  \\\n",
       "2                        Wall's End              NorthGate Brewing   \n",
       "12                         Sho'nuff      Against the Grain Brewery   \n",
       "13                      Bloody Show      Against the Grain Brewery   \n",
       "18                   The Brown Note      Against the Grain Brewery   \n",
       "19                      House Lager       Jack's Abby Craft Lagers   \n",
       "...                             ...                            ...   \n",
       "2372               Bombshell Blonde  Southern Star Brewing Company   \n",
       "2385            Bikini Blonde Lager           Maui Brewing Company   \n",
       "2396               Royal Weisse Ale        Sly Fox Brewing Company   \n",
       "2404                           Hell          Surly Brewing Company   \n",
       "2409  Hell or High Watermelon Wheat         21st Amendment Brewery   \n",
       "\n",
       "                 Location                       Style    Size  ABV  IBUs  \n",
       "2         Minneapolis, MN           English Brown Ale  16 oz.  4.8  19.0  \n",
       "12         Louisville, KY            Belgian Pale Ale  16 oz.  4.0  13.0  \n",
       "13         Louisville, KY            American Pilsner  16 oz.  5.5  17.0  \n",
       "18         Louisville, KY           English Brown Ale  16 oz.  5.0  20.0  \n",
       "19         Framingham, MA  Keller Bier / Zwickel Bier  16 oz.  5.2  18.0  \n",
       "...                   ...                         ...     ...  ...   ...  \n",
       "2372           Conroe, TX         American Blonde Ale  12 oz.  5.0  20.0  \n",
       "2385          Lahaina, HI         Munich Helles Lager  12 oz.  4.5  18.0  \n",
       "2396        Pottstown, PA                  Hefeweizen  12 oz.  5.6  11.0  \n",
       "2404  Brooklyn Center, MN  Keller Bier / Zwickel Bier  16 oz.  5.1  20.0  \n",
       "2409    San Francisco, CA      Fruit / Vegetable Beer  12 oz.  4.9  17.0  \n",
       "\n",
       "[338 rows x 7 columns]"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.IBUs<21]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List the median IBUs of each type of beer. Graph it.\n",
    "\n",
    "Put the highest at the top, and the missing ones at the bottom.\n",
    "\n",
    "- Tip: Look at the options for `sort_values` to figure out the `NaN` thing. The `?` probably won't help you here."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Style'>"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x2160 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#got this from answer key!\n",
    "df.groupby(\"Style\")['IBUs'].median().sort_values(na_position='first').plot(kind='barh', figsize=(5, 30))"
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hmmmm, it looks like they are generally different styles. What are the most common 5 styles of high-IBU beer vs. low-IBU beer?\n",
    "\n",
    "- *Tip: You'll want to think about it in three pieces - filtering to only find the specific beers beers, then finding out what the most common styles are, then getting the top 5.*\n",
    "- *Tip: You CANNOT do this in one command. It's going to be one command for the high and one for the low.*\n",
    "- *Tip: \"High IBU\" means higher than 75th percentile, \"Low IBU\" is under 25th percentile*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      195\n",
       "American Double / Imperial IPA     72\n",
       "American Pale Ale (APA)            18\n",
       "American Black Ale                 15\n",
       "American Strong Ale                 9\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#high IBU\n",
    "df[df.IBUs > 64].Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American Pale Wheat Ale    43\n",
       "American Blonde Ale        36\n",
       "Fruit / Vegetable Beer     28\n",
       "Hefeweizen                 21\n",
       "Witbier                    20\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#low IBU\n",
    "df[df.IBUs < 21].Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of \"Witbier\", \"Hefeweizen\" and \"American Pale Wheat Ale\" styles\n",
    "\n",
    "I'm counting these as wheat beers. If you see any other wheat beer categories, feel free to include them. I want ONE measurement and ONE graph, not three separate ones. And 20 to 30 bins in the histogram, please.\n",
    "\n",
    "- *Tip: I hope that `isin` is in your toolbox*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    112.000000\n",
       "mean      18.982143\n",
       "std        9.616036\n",
       "min        6.000000\n",
       "25%       13.750000\n",
       "50%       18.000000\n",
       "75%       20.250000\n",
       "max       64.000000\n",
       "Name: IBUs, dtype: float64"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#from answer key\n",
    "df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Draw a histogram of the IBUs of those beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
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
    "df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.hist(bins=20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of any style with \"IPA\" in it (also draw a histogram)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    392.000000\n",
       "mean      71.948980\n",
       "std       19.545669\n",
       "min       30.000000\n",
       "25%       60.000000\n",
       "50%       70.000000\n",
       "75%       85.000000\n",
       "max      138.000000\n",
       "Name: IBUs, dtype: float64"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ", #need na=False\n",
    "df[df.Style.str.contains(\"IPA\", na=False)].IBUs.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
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
    "df[df.Style.str.contains(\"IPA\", na=False)].IBUs.describe().hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plot those two histograms on top of one another\n",
    "\n",
    "To plot two plots on top of one another, you do two steps.\n",
    "\n",
    "1. First, you make a plot using `plot` or `hist`, and you save it into a variable called `ax`.\n",
    "2. You draw your second graph using `plot` or `hist`, and send `ax=ax` to it as a parameter.\n",
    "\n",
    "It would look something like this:\n",
    "\n",
    "```python\n",
    "ax = df.plot(....)\n",
    "df.plot(ax=ax, ....)\n",
    "``` \n",
    "\n",
    "(...except totally different)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
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
    "#??? from answer key\n",
    "ax = df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.hist(alpha=0.5)\n",
    "df[df.Style.str.contains(\"IPA\", na=False)].IBUs.hist(ax=ax, alpha=0.5, bins=20)"
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Compare the ABV of wheat beers vs. IPAs : their IBUs were really different, but how about their alcohol percentage?\n",
    "\n",
    "Wheat beers might include witbier, hefeweizen, American Pale Wheat Ale, and anything else you think is wheaty. IPAs probably have \"IPA\" in their name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    560.000000\n",
       "mean       6.879286\n",
       "std        1.240232\n",
       "min        2.700000\n",
       "25%        6.200000\n",
       "50%        6.800000\n",
       "75%        7.500000\n",
       "max        9.900000\n",
       "Name: ABV, dtype: float64"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Style.str.contains(\"IPA\", na=False)].ABV.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    183.000000\n",
       "mean       5.043716\n",
       "std        0.809050\n",
       "min        3.700000\n",
       "25%        4.600000\n",
       "50%        5.000000\n",
       "75%        5.300000\n",
       "max        9.200000\n",
       "Name: ABV, dtype: float64"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df[df.Style.str.contains(\"Wheat\"| \"witbier\" | \"hefeweizen\", na=False)].ABV.describe()\n",
    "df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].ABV.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Good work!\n",
    "\n",
    "If you made it this far you deserve a drink."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Jesus. Computer science is really mature field. Who developed all of this?"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}