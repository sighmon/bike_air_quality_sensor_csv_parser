# Clean the data by only taking the last sample when the CO heater has been on
# For mapping on http://www.gpsvisualizer.com/map_input?form=data

# See also the heatmap (that isn't all that useful for us)
# https://github.com/joyofdata/csv-heatmap

# To run in debug mode
# $ python -m pdb clean-data.py

import csv
import pdb
with open('latest.csv', mode='r') as infile:
  reader = csv.reader(infile)
  with open('latest-clean.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    rows_to_write = []
    mydict = {}
    writer.writerow(reader.next())
    # next(reader, None)

    last_row = None
    for rows in reader:

        # Reduce the accuracy of the GPS to three decimal places
        rows[2] = str(round(float(rows[2]), 3))
        rows[3] = str(round(float(rows[3]), 3))

        # For carbonmonoxide uncomment this if statement
        if (last_row != None) and (float(rows[8]) == 0) and (float(last_row[8]) == 1):
            # Only keep the row if the last one had the heaterOn and this one has the heaterOff
            rows_to_write.append(last_row)

        last_row = rows

        # For particles uncomment this if statement
        # if (float(rows[8]) == 1):
        #     # Only keep the row if the last one had the heaterOn and this one has the heaterOff
        #     rows_to_write.append(rows)

    for row in rows_to_write:
        # Add to the dictionary of lat,lon keys to average the data values for the same location
        lat, lon = float(row[2]), float(row[3])
        values = mydict.get((lat, lon))
        if values == None:
            values = [row]
        else:
          values.append(row)
        mydict[(lat,lon)] = values

    for key,value in mydict.iteritems():
    	# writer.writerow([sum(value)/len(value),key[0],key[1]])
        humidity, temperature, particles, carbonmonoxide = [],[],[],[]
        for val in value:
            humidity.append(float(val[4]))
            temperature.append(float(val[5]))
            particles.append(float(val[6]))
            carbonmonoxide.append(float(val[7]))

        # print(sum(carbonmonoxide)/len(carbonmonoxide))

        writer.writerow([value[0][0],value[0][1],key[0],key[1],sum(humidity)/len(humidity),sum(temperature)/len(temperature),sum(particles)/len(particles),sum(carbonmonoxide)/len(carbonmonoxide),value[0][8]])