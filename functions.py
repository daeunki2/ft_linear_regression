# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: daeunki2 <daeunki2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/19 21:57:02 by daeunki2          #+#    #+#              #
#    Updated: 2026/09/19 21:58:27 by daeunki2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

def read_data(filename):
    mileages = []
    prices = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))

    return mileages, prices